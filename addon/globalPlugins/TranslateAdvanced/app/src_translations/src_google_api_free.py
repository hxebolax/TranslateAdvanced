# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Agradecimientos a los autores originales Alexy Sadovoy, ruslan, beqa, Mesar Hameed, Alberto Buffolino y otros contribuidores de NVDA
# por su trabajo en el complemento "Instant Translate". Este módulo se basa en su excelente trabajo y ha sido adaptado
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import os
import re
import ssl
import threading
from time import sleep
from random import randint, choice
import json
import urllib.request as urllibRequest

# Carga traducción
addonHandler.initTranslation()

# Configuración para ignorar la verificación SSL
ssl._create_default_https_context = ssl._create_unverified_context

class TranslatorGoogleApiFree:
	"""
	Clase para manejar la traducción de texto utilizando la API de Google Translate.
	"""

	def __init__(self):
		"""
		Inicializa una instancia del traductor de Google Translate.
		"""
		self.arabic_breaks = u'[،؛؟]'
		self.chinese_breaks = u'[　-〿︐-︟︰-﹯！-｠]'
		self.latin_breaks = r'[.,!?;:]'
		self.split_reg = re.compile(u"{arabic}|{chinese}|{latin}".format(arabic=self.arabic_breaks, chinese=self.chinese_breaks, latin=self.latin_breaks))
		self.lang_conversion_dic = {'iw': 'he', 'jw': 'jv'}
		self.error = {"success": False, "data": None}
		self.traductor_hilo = None

	def dividir_chunks(self, text, chunksize):
		"""
		Divide el texto en partes más pequeñas basándose en signos de puntuación.

		:param text: Texto a dividir.
		:param chunksize: Tamaño máximo de cada parte.
		:return: Generador que produce partes del texto.
		"""
		pos = 0
		potential_pos = 0
		for split_mark in self.split_reg.finditer(text):
			if (split_mark.start() - pos + 1) < chunksize:
				potential_pos = split_mark.start()
				continue
			else:
				yield text[pos:potential_pos + 1]
				pos = potential_pos + 1
				potential_pos = split_mark.start()
		yield text[pos:]

	def translate_google_api_free(self, lang_from, lang_to, text, lang_swap=None, chunksize=3000, mostrar_progreso=False, widget=None, IS_DIALOGO=False):
		"""
		Traduce el texto de un idioma a otro utilizando la API de Google Translate.

		:param lang_from: Idioma de origen.
		:param lang_to: Idioma de destino.
		:param text: Texto a traducir.
		:param lang_swap: Idioma alternativo si el idioma detectado es igual al idioma de destino.
		:param chunksize: Tamaño máximo de cada parte del texto.
		:param mostrar_progreso: Mostrar el progreso de la traducción.
		:param widget: Función para actualizar el progreso.
		:param IS_DIALOGO: Si es llamado desde un dialogo.
		:return: Traducción del texto.
		"""
		self.traductor_hilo = self.TraductorHilo(lang_from, lang_to, text, lang_swap, chunksize, self.split_reg, self.lang_conversion_dic, mostrar_progreso, widget)
		self.traductor_hilo.start()
		self.traductor_hilo.join()  # Esperar a que el hilo termine
		self.error = self.traductor_hilo.error  # Actualizar el estado de error
		if self.error["success"]:
			msg = _("""Error en la traducción.

Error:

{}""").format(self.error["data"])
			if not IS_DIALOGO:
				logHandler.log.error(msg)
			return text
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

		def __init__(self, lang_from, lang_to, text, lang_swap, chunksize, split_reg, lang_conversion_dic, mostrar_progreso, widget):
			"""
			Inicializa el hilo de traducción.

			:param lang_from: Idioma de origen.
			:param lang_to: Idioma de destino.
			:param text: Texto a traducir.
			:param lang_swap: Idioma alternativo si el idioma detectado es igual al idioma de destino.
			:param chunksize: Tamaño máximo de cada parte del texto.
			:param split_reg: Expresión regular para dividir el texto.
			:param lang_conversion_dic: Diccionario de conversión de códigos de idioma.
			:param mostrar_progreso: Mostrar el progreso de la traducción.
			:param widget: Función para actualizar el progreso.
			"""
			super().__init__()
			self.lang_from = lang_from
			self.lang_to = lang_to
			self.text = text
			self.lang_swap = lang_swap
			self.chunksize = chunksize
			self.split_reg = split_reg
			self.lang_conversion_dic = lang_conversion_dic
			self.translation = ''
			self.lang_detected = ''
			self.error = {"success": False, "data": None}
			self.opener = urllibRequest.build_opener()
			self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
			self.first_chunk = True
			self._stop_event = threading.Event()
			self.mostrar_progreso = mostrar_progreso
			self.widget = widget
			self.total_chunks = sum(1 for _ in self.split_reg.finditer(text))
			self.processed_chunks = 0
			self.url_templates = [
				"https://translate.googleapis.com/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.googleapis.mirror.nvdadr.com/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.com/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.co.in/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.co.uk/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.com.au/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.ca/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.de/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.es/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.fr/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.it/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.nl/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.pt/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1",
				"https://translate.google.ru/translate_a/single?client=gtx&sl={lang_from}&tl={lang_to}&dt=t&q={text}&dj=1"
			]

		def stop(self):
			"""
			Detiene el hilo de traducción.
			"""
			self._stop_event.set()

		def run(self):
			"""
			Ejecuta el proceso de traducción en el hilo.
			"""
			url_template = choice(self.url_templates)
			chunks = list(TranslatorGoogleApiFree.dividir_chunks(self, self.text, self.chunksize))
			self.total_chunks = len(chunks)
			for chunk in chunks:
				# Simular un comportamiento humano al hacer las solicitudes
				if not self.first_chunk:
					sleep(randint(1, 10))
				if self._stop_event.is_set():
					self.error = {"success": True, "data": _("Proceso cancelado por el usuario")}
					return
				url = url_template.format(lang_from=self.lang_from, lang_to=self.lang_to, text=urllibRequest.quote(chunk.encode('utf-8')))
				try:
					response = json.load(self.opener.open(url))
					self.lang_detected = response['src']
					self.lang_detected = self.lang_conversion_dic.get(self.lang_detected, self.lang_detected)
					if self.first_chunk and self.lang_from == "auto" and self.lang_detected == self.lang_to and self.lang_swap is not None:
						self.lang_to = self.lang_swap
						self.first_chunk = False
						url = url_template.format(lang_from=self.lang_from, lang_to=self.lang_to, text=urllibRequest.quote(chunk.encode('utf-8')))
						response = json.load(self.opener.open(url))
				except Exception as e:
					# Si ocurre un error, detener el proceso de traducción
					self.error = {"success": True, "data": str(e)}
					return
				self.translation += "".join(sentence["trans"] for sentence in response["sentences"])
				self.processed_chunks += 1
				self.first_chunk = False
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
