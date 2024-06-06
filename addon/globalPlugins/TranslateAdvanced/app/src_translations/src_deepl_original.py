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

class TranslatorDeepL:
	"""
	Clase que maneja traducciones utilizando la API de DeepL.
	Puede utilizar tanto la versión gratuita como la de pago de la API.
	"""
	
	def __init__(self):
		"""
		Inicializa una instancia del traductor DeepL.
		"""
		pass
	
	def translate_deepl(self, text, api_key, use_free_api=True, source_lang="auto", target_lang="es"):
		"""
		Traduce un texto utilizando la API de DeepL.
		
		:param text: Texto a traducir.
		:param api_key: Clave de API de DeepL.
		:param use_free_api: Indica si se debe usar la API gratuita (por defecto) o la de pago.
		:param source_lang: Código del idioma de origen (por defecto 'auto').
		:param target_lang: Código del idioma de destino (por defecto 'es').
		:return: Texto traducido.
		"""
		if not api_key:
			raise ValueError(_("Se requiere una clave de API para DeepL."))
		
		self.api_key = api_key
		self.base_url = "https://api-free.deepl.com/v2" if use_free_api else "https://api.deepl.com/v2"

		# Endpoint y parámetros de la solicitud
		url = f"{self.base_url}/translate"
		params = {
			"auth_key": self.api_key,
			"text": text,
			"target_lang": target_lang
		}
		if source_lang.lower() != "auto":
			params["source_lang"] = source_lang
		
		data = urllib.parse.urlencode(params).encode("utf-8")
		headers = {
			"Content-Type": "application/x-www-form-urlencoded"
		}
		req = urllib.request.Request(url, data=data, headers=headers, method="POST")
		
		# Realiza la solicitud y maneja la respuesta
		try:
			with urllib.request.urlopen(req) as response:
				response_data = response.read().decode()
				response_json = json.loads(response_data)
				return response_json['translations'][0]['text']
		except urllib.request.HTTPError as e:
			logHandler.log.error(_("Error en la traducción: {0} {1}").format(e.code, e.reason))
			return text
		except Exception as e:
			logHandler.log.error(_("Error en la traducción: {0}").format(str(e)))
			return text
	
	def get_usage(self, api_key):
		"""
		Obtiene el uso actual de la API de DeepL.
		
		:param api_key: Clave de API de DeepL.
		:return: Información del uso de la API de DeepL.
		"""
		self.api_key = api_key
		# Endpoint y parámetros de la solicitud
		url = f"{self.base_url}/usage"
		params = {
			"auth_key": self.api_key
		}
		headers = {
			"Content-Type": "application/x-www-form-urlencoded"
		}
		url_with_params = f"{url}?{urllib.parse.urlencode(params)}"
		req = urllib.request.Request(url_with_params, headers=headers, method="GET")
		
		# Realiza la solicitud y maneja la respuesta
		try:
			with urllib.request.urlopen(req) as response:
				response_data = response.read().decode()
				response_json = json.loads(response_data)
				usage_info = _("DeepL - uso: {0} / {1}").format(response_json['character_count'], response_json['character_limit'])
				return usage_info
		except Exception as e:
			logHandler.log.error(_("Error obteniendo uso de DeepL: {0}").format(str(e)))
			return _("Error obteniendo uso de DeepL: {0}").format(str(e))
