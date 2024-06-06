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
import json

# Carga traducción
addonHandler.initTranslation()

class TranslatorLibreTranslate:
	"""
	Clase que maneja traducciones utilizando la API de LibreTranslate.
	Puede utilizar tanto la versión gratuita como la de pago de la API.
	"""
	
	def __init__(self):
		"""
		Inicializa una instancia del traductor LibreTranslate.
		"""
		pass
	
	def translate_libretranslate(self, text, api_key, source_lang="auto", target_lang="es", api_url="https://translate.nvda.es/translate"):
		"""
		Traduce un texto utilizando la API de LibreTranslate.
		
		:param text: Texto a traducir.
		:param api_key: Clave de API de LibreTranslate.
		:param source_lang: Código del idioma de origen (por defecto 'auto').
		:param target_lang: Código del idioma de destino (por defecto 'es').
		:param api_url: URL de la API de LibreTranslate (por defecto "https://translate.nvda.es/translate").
		:return: Texto traducido.
		"""
		if not api_key:
			msg = \
_("""Error en la traducción.

Error:

Se requiere una clave de API para LibreTranslate.""")
			logHandler.log.error(msg)
			return text
		
		# Endpoint y parámetros de la solicitud
		url = api_url
		params = {
			"q": text,
			"source": source_lang,
			"target": target_lang,
			"format": "text",
			"api_key": api_key
		}
		
		data = json.dumps(params).encode("utf-8")
		headers = {
			"Content-Type": "application/json",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
		}
		req = urllib.request.Request(url, data=data, headers=headers, method="POST")
		
		# Realiza la solicitud y maneja la respuesta
		try:
			with urllib.request.urlopen(req) as response:
				response_data = response.read().decode()
				response_json = json.loads(response_data)
				return response_json.get('translatedText', text)
		except urllib.request.HTTPError as e:
			msg = \
_("""Error en la traducción.

Error:

{}

{}""").format(e.code, e.reason)
			logHandler.log.error(msg)
			return text
		except Exception as e:
			msg = \
_("""Error en la traducción.

Error:

{}""").format(str(e))
			logHandler.log.error(msg)
			return text
