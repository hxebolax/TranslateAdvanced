# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import urllib.parse
import urllib.request
import re
import html

# Carga traducción
addonHandler.initTranslation()

class TranslatorGoogle:
	"""
	Clase para manejar la traducción de texto usando Google Translate.
	"""

	def __init__(self):
		"""
		Inicializa una instancia del traductor de Google Translate.
		"""
		self.agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

	def translate_google(self, to_translate, to_language="auto", from_language="auto"):
		"""
		Traduce un texto usando Google Translate.

		:param to_translate: El texto a traducir.
		:param to_language: El idioma al que traducir (por defecto "auto").
		:param from_language: El idioma desde el que traducir (por defecto "auto").
		:return: El texto traducido.
		"""
		base_link = "https://translate.google.com/m?sl=%s&tl=%s&q=%s"
		to_translate_encoded = urllib.parse.quote(to_translate)
		link = base_link % (from_language, to_language, to_translate_encoded)
		request = urllib.request.Request(link, headers=self.agent)
		try:
			with urllib.request.urlopen(request) as response:
				raw_data = response.read()
		except Exception as e:
			msg = _("""Error en la traducción.

Error:

{}""").format(str(e))
			logHandler.log.error(msg)
			return to_translate  # Devolver el texto original en caso de error
		
		data = raw_data.decode("utf-8")
		expr = r'class="result-container">(.*?)</div>'
		re_result = re.findall(expr, data)
		
		if not re_result:
			result = ""
		else:
			result = html.unescape(re_result[0])
		
		return result
