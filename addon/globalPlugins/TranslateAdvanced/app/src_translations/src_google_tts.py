# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import wx
import urllib.request as urllibRequest
import urllib.parse
import threading
from time import sleep
from random import randint

# Carga traducción
addonHandler.initTranslation()

class TextToSpeechGoogle:
	"""
	Clase para manejar la conversión de texto a audio utilizando la API de Google Text-to-Speech.
	"""

	def __init__(self):
		"""
		Inicializa una instancia de TextToSpeechGoogle.
		"""
		self.audio_data = None
		self.detener_hilo_audio = threading.Event()  # Bandera para detener el hilo de audio
		self.opener = urllibRequest.build_opener()
		self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]

	def obtener_audio(self, texto, idioma, mostrar_progreso=False, ventana_padre=None, widget=None, max_length=200, IS_DIALOGO=True):
		"""
		Obtiene el audio del texto especificado utilizando la API de Google Text-to-Speech.

		:param texto: Texto a convertir a audio.
		:param idioma: Código de idioma para la conversión.
		:param mostrar_progreso: Indica si se debe mostrar el progreso de la conversión.
		:param ventana_padre: Referencia a la ventana principal para actualizar la barra de progreso.
		:param max_length: Longitud máxima de cada parte del texto para la solicitud de la API.
		:return: Datos de audio en formato binario.
		"""
		hilo_audio = self.AudioHilo(
			texto=texto,
			idioma=idioma,
			mostrar_progreso=mostrar_progreso,
			ventana_padre=ventana_padre,
			widget=widget,
			max_length=max_length,
			opener=self.opener,
			detener_hilo_audio=self.detener_hilo_audio
		)
		hilo_audio.start()
		hilo_audio.join()  # Esperar a que el hilo termine
		self.error = hilo_audio.error  # Actualizar el estado de error
		if self.error["success"]:
			msg = _("""Error al obtener el audio.

Error:

{}""").format(self.error["data"])
			if not IS_DIALOGO:
				logHandler.log.error(msg)
			return None
		return hilo_audio.audio_data

	def get_error(self):
		"""
		Obtiene el estado del error.

		:return: Estado del error.
		"""
		return self.error

	def stop(self):
		"""
		Cancela la obtención del audio.
		"""
		self.detener_hilo_audio.set()

	class AudioHilo(threading.Thread):
		"""
		Clase interna que extiende threading.Thread para manejar la conversión de texto a audio en un hilo separado.
		"""

		def __init__(self, texto, idioma, mostrar_progreso, ventana_padre, widget, max_length, opener, detener_hilo_audio):
			"""
			Inicializa el hilo de conversión de texto a audio.

			:param texto: Texto a convertir a audio.
			:param idioma: Código de idioma para la conversión.
			:param mostrar_progreso: Indica si se debe mostrar el progreso de la conversión.
			:param ventana_padre: Referencia a la ventana principal para actualizar la barra de progreso.
			:param max_length: Longitud máxima de cada parte del texto para la solicitud de la API.
			:param opener: Objeto opener para realizar las solicitudes HTTP.
			:param detener_hilo_audio: Bandera para detener el hilo de audio.
			"""
			super().__init__()
			self.texto = texto
			self.idioma = idioma
			self.mostrar_progreso = mostrar_progreso
			self.ventana_padre = ventana_padre
			self.widget = widget
			self.max_length = max_length
			self.opener = opener
			self.detener_hilo_audio = detener_hilo_audio
			self.audio_data = b""
			self.error = {"success": False, "data": None}

		def run(self):
			"""
			Ejecuta el proceso de conversión de texto a audio en el hilo.
			"""
			try:
				# Nueva lógica para dividir el texto sin cortar palabras
				partes = self._dividir_texto(self.texto, self.max_length)
				total_partes = len(partes)
				for i, parte in enumerate(partes):
					if self.detener_hilo_audio.is_set():
						self.error = {"success": True, "data": _("Proceso cancelado por el usuario")}
						return
					audio_parte = self._obtener_audio_parte(parte)
					self.audio_data += audio_parte
					if self.mostrar_progreso:
						self.widget(int((i + 1) / total_partes * 100))
					# Simular un comportamiento humano al hacer las solicitudes
					sleep(randint(1, 3))
			except Exception as e:
				self.error = {"success": True, "data": str(e)}
				return

		def _dividir_texto(self, texto, max_length):
			"""
			Divide el texto en partes que no excedan max_length y no corten palabras a la mitad.

			:param texto: Texto a dividir.
			:param max_length: Longitud máxima de cada parte del texto.
			:return: Lista de partes de texto.
			"""
			partes = []
			palabras = texto.split()
			parte_actual = ""
			for palabra in palabras:
				if len(parte_actual) + len(palabra) + 1 <= max_length:
					# Agregar la palabra a la parte actual
					if parte_actual:
						parte_actual += " "
					parte_actual += palabra
				else:
					# Añadir la parte actual a la lista de partes y resetear
					partes.append(parte_actual)
					parte_actual = palabra
			if parte_actual:
				partes.append(parte_actual)
			return partes

		def _obtener_audio_parte(self, texto):
			"""
			Obtiene el audio para una parte del texto utilizando la API de Google Text-to-Speech.

			:param texto: Parte del texto a convertir a audio.
			:return: Datos de audio en formato binario.
			"""
			url_audio = f"https://translate.google.com/translate_tts?ie=UTF-8&tl={self.idioma}&client=tw-ob&q={urllib.parse.quote(texto, encoding='utf-8', errors='surrogatepass')}"
			try:
				with urllibRequest.urlopen(url_audio) as response:
					return response.read()
			except Exception as e:
				msg = _("""Error al obtener el audio para una parte del texto.

Error:

{}""").format(str(e))
				self.error = {"success": True, "data": str(e)}
				return
