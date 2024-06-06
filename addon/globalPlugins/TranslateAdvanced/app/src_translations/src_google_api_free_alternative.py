# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
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
import urllib.parse

# Carga traducción
addonHandler.initTranslation()

# Configuración para ignorar la verificación SSL
ssl._create_default_https_context = ssl._create_unverified_context

class TranslatorGoogleApiFreeAlternative:
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
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
		self.url = 'https://translate.googleapis.com/translate_a/single'
		self.opener = urllibRequest.build_opener()
		self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]

	@staticmethod
	def rshift(val, n):
		"""
		Realiza un desplazamiento a la derecha.

		:param val: Valor a desplazar.
		:param n: Número de posiciones.
		:return: Valor desplazado.
		"""
		return (val % 0x100000000) >> n

	def getTk(self, text):
		"""
		Calcula el token de traducción (tk) para Google Translate.

		:param text: Texto a traducir.
		:return: Token de traducción (tk).
		"""
		def RL(a, b):
			"""
			Función auxiliar para el cálculo del token.

			:param a: Valor inicial.
			:param b: Cadena de operaciones.
			:return: Valor modificado.
			"""
			for d in range(0, len(b) - 2, 3):
				c = b[d + 2]
				if 'a' <= c:
					c = ord(c[0]) - 87
				else:
					c = int(c)
				if b[d + 1] == '+':
					a = TranslatorGoogleApiFreeAlternative.rshift(a, c)
				else:
					a = a << c
				a = a + c & 4294967295 if b[d] == '+' else a ^ c
			return a

		b = 406644
		b1 = 3293161072

		jd = "."
		Zb = "+-a^+6"
		Yb = "+-3^+b+-f"

		a = []
		for i in range(len(text)):
			k = ord(text[i])
			if 128 > k:
				a.append(k)
			else:
				if 2048 > k:
					a.append(k >> 6 | 192)
				else:
					if 55296 == (k & 64512) and i + 1 < len(text) and 56320 == (ord(text[i + 1]) & 64512):
						k = 65536 + ((k & 1023) << 10) + (ord(text[i + 1]) & 1023)
						a.append(k >> 18 | 240)
						a.append(k >> 12 & 63 | 128)
						i += 1
					else:
						a.append(k >> 12 | 224)
						a.append(k >> 6 & 63 | 128)
				a.append(k & 63 | 128)

		res = b
		for d in a:
			res += d
			res = RL(res, Zb)
		res = RL(res, Yb)
		res ^= b1 or 0
		if 0 > res:
			res = (res & 2147483647) + 2147483648
		res %= 1000000
		return str(res) + jd + str(res ^ b)

	def buildUrl(self, text, tk, sl, tl):
		"""
		Construye la URL para la solicitud de traducción.

		:param text: Texto a traducir.
		:param tk: Token de traducción.
		:param sl: Idioma de origen.
		:param tl: Idioma de destino.
		:return: URL completa para la solicitud de traducción.
		"""
		baseUrl = 'https://translate.googleapis.com/translate_a/single'
		baseUrl += '?client=gtx&'  # Uso de client=gtx para simplificar la solicitud
		baseUrl += 'sl=' + sl + '&'
		baseUrl += 'tl=' + tl + '&'
		baseUrl += 'hl=zh-CN&'
		baseUrl += 'dt=at&'
		baseUrl += 'dt=bd&'
		baseUrl += 'dt=ex&'
		baseUrl += 'dt=ld&'
		baseUrl += 'dt=md&'
		baseUrl += 'dt=qca&'
		baseUrl += 'dt=rw&'
		baseUrl += 'dt=rm&'
		baseUrl += 'dt=ss&'
		baseUrl += 'dt=t&'
		baseUrl += 'ie=UTF-8&'
		baseUrl += 'oe=UTF-8&'
		baseUrl += 'source=btn&'
		baseUrl += 'ssel=0&'
		baseUrl += 'tsel=0&'
		baseUrl += 'kc=1&'
		baseUrl += 'tk=' + str(tk) + '&'
		content = urllib.parse.quote(text)
		baseUrl += 'q=' + content
		return baseUrl

	def getHtml(self, url):
		"""
		Realiza la solicitud HTTP y obtiene la respuesta en formato JSON.

		:param url: URL de la solicitud.
		:return: Respuesta en formato JSON.
		"""
		try:
			response = self.opener.open(url)
			return json.load(response)
		except Exception as e:
			msg = \
_("""Error al obtener la respuesta.

Error:

{}""").format(str(e))
			logHandler.log.error(msg)
			return None

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

	def translate_google_api_free(self, lang_from, lang_to, text, lang_swap=None, chunksize=3000, mostrar_progreso=False):
		"""
		Traduce el texto de un idioma a otro utilizando la API de Google Translate.

		:param lang_from: Idioma de origen.
		:param lang_to: Idioma de destino.
		:param text: Texto a traducir.
		:param lang_swap: Idioma alternativo si el idioma detectado es igual al idioma de destino.
		:param chunksize: Tamaño máximo de cada parte del texto.
		:param mostrar_progreso: Mostrar el progreso de la traducción.
		:return: Traducción del texto.
		"""
		traductor = self.TraductorHilo(
			lang_from=lang_from,
			lang_to=lang_to,
			text=text,
			lang_swap=lang_swap,
			chunksize=chunksize,
			split_reg=self.split_reg,
			lang_conversion_dic=self.lang_conversion_dic,
			mostrar_progreso=mostrar_progreso,
			getTk=self.getTk,
			buildUrl=self.buildUrl,
			getHtml=self.getHtml,
			dividir_chunks=self.dividir_chunks
		)
		traductor.start()
		traductor.join()  # Esperar a que el hilo termine
		if traductor.error["success"]:
			msg = \
_("""Error en la traducción.

Error:

{}""").format(traductor.error["data"])
			logHandler.log.error(msg)
			return text

		return traductor.translation

	class TraductorHilo(threading.Thread):
		"""
		Clase interna que extiende threading.Thread para manejar la traducción en un hilo separado.
		"""

		def __init__(
			self,
			lang_from,
			lang_to,
			text,
			lang_swap,
			chunksize,
			split_reg,
			lang_conversion_dic,
			mostrar_progreso,
			getTk,
			buildUrl,
			getHtml,
			dividir_chunks
		):
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
			self.first_chunk = True
			self._stop_event = threading.Event()
			self.mostrar_progreso = mostrar_progreso
			self.total_chunks = sum(1 for _ in self.split_reg.finditer(text))
			self.processed_chunks = 0
			self.getTk = getTk
			self.buildUrl = buildUrl
			self.getHtml = getHtml
			self.dividir_chunks = dividir_chunks

		def stop(self):
			"""
			Detiene el hilo de traducción.
			"""
			self._stop_event.set()

		def run(self):
			"""
			Ejecuta el proceso de traducción en el hilo.
			"""
			chunks = list(self.dividir_chunks(self.text, self.chunksize))
			self.total_chunks = len(chunks)
			for chunk in chunks:
				# Simular un comportamiento humano al hacer las solicitudes
				if not self.first_chunk:
					sleep(randint(1, 10))
				tk = self.getTk(chunk)
				url = self.buildUrl(chunk, tk, self.lang_from, self.lang_to)
				try:
					response = self.getHtml(url)
					if response is None:
						raise Exception(_("Respuesta vacía o inválida"))
					# Verifica la estructura de la respuesta y accede correctamente
					if isinstance(response, list) and len(response) > 0 and isinstance(response[0], list):
						translated_chunk = ''.join([item[0] for item in response[0] if item[0]])
					else:
						raise Exception(_("Estructura de respuesta inesperada"))
					self.lang_detected = response[2]
					self.lang_detected = self.lang_conversion_dic.get(self.lang_detected, self.lang_detected)
					if self.first_chunk and self.lang_from == "auto" and self.lang_detected == self.lang_to and self.lang_swap is not None:
						self.lang_to = self.lang_swap
						self.first_chunk = False
						tk = self.getTk(chunk)
						url = self.buildUrl(chunk, tk, self.lang_from, self.lang_to)
						response = self.getHtml(url)
						if response is None:
							raise Exception(_("Respuesta vacía o inválida después de cambiar el idioma de destino"))
						if isinstance(response, list) and len(response) > 0 and isinstance(response[0], list):
							translated_chunk = ''.join([item[0] for item in response[0] if item[0]])
						else:
							raise Exception(_("Estructura de respuesta inesperada después de cambiar el idioma de destino"))
				except Exception as e:
					# Si ocurre un error, detener el proceso de traducción
					self.error = {"success": True, "data": str(e)}
					return
				self.translation += translated_chunk
				self.processed_chunks += 1
				self.first_chunk = False
				if self.mostrar_progreso:
					print(f"Progreso de la traducción: {self.get_progreso():.2f}%")

		def get_progreso(self):
			"""
			Obtiene el progreso de la traducción en porcentaje.

			:return: Progreso de la traducción en porcentaje.
			"""
			if self.total_chunks == 0:
				return 100
			return (self.processed_chunks / self.total_chunks) * 100
