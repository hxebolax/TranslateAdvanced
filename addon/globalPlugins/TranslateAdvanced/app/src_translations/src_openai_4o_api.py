# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import json
import urllib.request
import urllib.error
import threading
from urllib.parse import quote

# Carga traducción
addonHandler.initTranslation()

class TranslatorOpenAI:
	"""
	Clase para manejar la traducción de texto utilizando la API de OpenAI.
	"""

	def __init__(self):
		"""
		Inicializa una instancia del traductor de OpenAI.

		"""
		self.error = {"success": False, "data": None}
		self.traductor_hilo = None

	def estimate_tokens(self, text):
		"""
		Estima el número de tokens que se utilizarán para el texto proporcionado.

		:param text: Texto para el que se estimarán los tokens.
		:return: Número estimado de tokens.
		"""
		characters_per_token = 4
		extra_tokens = 10

		if not text.isascii():
			characters_per_token = 5

		approx_tokens = len(text) / characters_per_token
		total_tokens = int(approx_tokens) + extra_tokens
		return total_tokens

	def split_text(self, text, max_tokens):
		"""
		Divide el texto en partes más pequeñas que no excedan el límite de tokens del modelo.

		:param text: Texto a dividir.
		:param max_tokens: Máximo de tokens permitidos por el modelo.
		:return: Lista de partes del texto.
		"""
		parts = []
		current_part = ""

		for word in text.split():
			estimated_tokens = TranslatorOpenAI.estimate_tokens(self, current_part + " " + word)
			if estimated_tokens < max_tokens:
				current_part += " " + word
			else:
				parts.append(current_part.strip())
				current_part = word
		
		if current_part:
			parts.append(current_part.strip())
		
		return parts

	def translate_openai(self, api_key, text, target_language="es", mostrar_progreso=False, widget=None):
		"""
		Traduce el texto de un idioma a otro utilizando la API de OpenAI.

		:param api_key: Clave de la API de OpenAI.
		:param text: Texto a traducir.
		:param target_language: Idioma de destino.
		:param mostrar_progreso: Mostrar el progreso de la traducción.
		:param widget: Función para actualizar el progreso.
		:return: Traducción del texto.
		"""
		self.models = {
			"gpt4o-mini": {
				"model": "gpt-4o-mini",
				"endpoint": "https://api.openai.com/v1/chat/completions",
				"max_tokens": 16384
			}
		}

		self.traductor_hilo = self.TraductorHilo(text, target_language, self.models, api_key, mostrar_progreso, widget)
		self.traductor_hilo.start()
		self.traductor_hilo.join()  # Esperar a que el hilo termine
		self.error = self.traductor_hilo.error  # Actualizar el estado de error
		if self.error["success"]:
			msg = \
_("""Error en la traducción.

Error:

{}""").format(self.error["data"])
			logHandler.log.error(msg)
			return text  # Devuelve el texto original si hay un error
		return self.traductor_hilo.translation

	def get_error(self):
		"""
		Obtiene el estado del error.

		:return: Estado del error.
		"""
		return self.error

	def stop(self):
		"""
		Detiene el hilo de traducción.
		"""
		if self.traductor_hilo:
			self.traductor_hilo.stop()

	class TraductorHilo(threading.Thread):
		"""
		Clase interna que extiende threading.Thread para manejar la traducción en un hilo separado.
		"""

		def __init__(self, text, target_language, models, api_key, mostrar_progreso, widget):
			"""
			Inicializa el hilo de traducción.

			:param text: Texto a traducir.
			:param target_language: Idioma de destino.
			:param models: Diccionario de modelos de OpenAI.
			:param api_key: Clave de la API de OpenAI.
			:param mostrar_progreso: Mostrar el progreso de la traducción.
			:param widget: Función para actualizar el progreso.
			"""
			super().__init__()
			self.text = text
			self.target_language = target_language
			self.models = models
			self.api_key = api_key
			self.translation = ''
			self.error = {"success": False, "data": None}
			self.opener = urllib.request.build_opener()
			self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
			self._stop_event = threading.Event()
			self.mostrar_progreso = mostrar_progreso
			self.widget = widget
			self.total_chunks = 0
			self.processed_chunks = 0

		def stop(self):
			"""
			Detiene el hilo de traducción.
			"""
			self._stop_event.set()

		def run(self):
			"""
			Ejecuta el proceso de traducción en el hilo.
			"""
			model_abbr = "gpt4o-mini"
			model_info = self.models[model_abbr]
			chunks = TranslatorOpenAI.split_text(self, self.text, model_info["max_tokens"] // 2)  # Dividir texto basado en tokens
			self.total_chunks = len(chunks)

			for chunk in chunks:
				if self._stop_event.is_set():
					self.error = {"success": True, "data": _("Proceso cancelado por el usuario")}
					return

				estimated_tokens = TranslatorOpenAI.estimate_tokens(self, chunk)
				max_tokens = model_info["max_tokens"] - estimated_tokens

				if max_tokens <= 0:
					self.error = {"success": True, "data": _("El texto excede el límite de tokens permitido.")}
					return

				model = model_info["model"]
				endpoint = model_info["endpoint"]

				headers = {
					"Content-Type": "application/json",
					"Authorization": f"Bearer {self.api_key}"
				}

				data = {
					"model": model,
					"messages": [
						{"role": "user", "content": f"Translate the following text exactly as is to the language specified by the ISO 639-1 code '{self.target_language}'. Do not change proper names, idioms, or provide explanations: '{chunk}'"}
					],
					"max_tokens": max_tokens
				}

				request_data = json.dumps(data).encode('utf-8')

				req = urllib.request.Request(endpoint, data=request_data, headers=headers)

				try:
					with urllib.request.urlopen(req) as response:
						response_data = response.read().decode('utf-8')
						response_json = json.loads(response_data)
						self.translation += response_json['choices'][0]['message']['content'].strip() + " "
				except urllib.error.HTTPError as e:
					error_message = e.read().decode('utf-8')
					error_json = json.loads(error_message)
					self.error = {"success": True, "data": error_json.get('error', {}).get('message', 'Unknown error')}
					return
				except Exception as e:
					self.error = {"success": True, "data": str(e)}
					return
				
				self.processed_chunks += 1
				if self.mostrar_progreso:
					self.widget(self.get_progreso())

		def get_progreso(self):
			"""
			Obtiene el progreso de la traducción en porcentaje.

			:return: Progreso de la traducción en porcentaje.
			"""
			if self.total_chunks == 0:
				return 100
			return (self.processed_chunks / self.total_chunks) * 100
