# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import json
import base64
from datetime import datetime
from urllib.parse import urlencode
from urllib.request import urlopen, Request

# Carga traducción
addonHandler.initTranslation()

class TranslatorMicrosoftApiFree:
	"""
	Clase para manejar la traducción de texto utilizando la API gratuita de Microsoft Translator.
	"""

	name = 'MicrosoftEdge(Free)'
	alias = 'Microsoft Edge (Free)'
	free = True
	endpoint = 'https://api-edge.cognitive.microsofttranslator.com/translate'
	need_api_key = False
	access_info = None

	def __init__(self):
		"""
		Inicializa una instancia del traductor Microsoft Translator.
		"""
		pass

	def _parse_jwt(self, token):
		"""
		Parsea el token JWT para obtener la fecha de expiración y el token.
		
		:param token: El token JWT.
		:return: Un diccionario con el token y la fecha de expiración.
		"""
		parts = token.split(".")
		if len(parts) <= 1:
			raise Exception('Failed to get APP key due to an invalid Token.')
		base64_url = parts[1]
		if not base64_url:
			raise Exception('Failed to get APP key due to an invalid Base64 URL.')
		base64_url = base64_url.replace('-', '+').replace('_', '/')
		json_payload = base64.b64decode(base64_url + '===').decode('utf-8')
		parsed = json.loads(json_payload)
		expired_date = datetime.fromtimestamp(parsed['exp'])
		return {'Token': token, 'Expire': expired_date}

	def _get_app_key(self):
		"""
		Obtiene la clave de aplicación (app key) para la autenticación.

		:return: El token de la aplicación.
		"""
		if not self.access_info or datetime.now() > self.access_info['Expire']:
			auth_url = 'https://edge.microsoft.com/translate/auth'
			response = urlopen(auth_url)
			app_key = response.read().decode('utf-8').strip()
			self.access_info = self._parse_jwt(app_key)
		else:
			app_key = self.access_info['Token']
		return app_key

	def get_endpoint(self, to_lang, from_lang=None):
		"""
		Obtiene el endpoint de la API con los parámetros adecuados.

		:param to_lang: El código del idioma objetivo.
		:param from_lang: El código del idioma fuente.
		:return: El endpoint de la API con los parámetros.
		"""
		query = {
			'to': to_lang,
			'api-version': '3.0',
			'includeSentenceLength': True,
		}
		if from_lang:
			query['from'] = from_lang
		return f'{self.endpoint}?{urlencode(query)}'

	def get_headers(self):
		"""
		Obtiene los encabezados necesarios para la solicitud.

		:return: Los encabezados de la solicitud.
		"""
		return {
			'Content-Type': 'application/json',
			'Authorization': f'Bearer {self._get_app_key()}'
		}

	def get_body(self, text):
		"""
		Genera el cuerpo de la solicitud.

		:param text: El texto a traducir.
		:return: El cuerpo de la solicitud en formato JSON.
		"""
		return json.dumps([{'text': text}])

	def translate_microsoft_api_free(self, lang_from, lang_to, text):
		"""
		Traduce el texto de un idioma a otro utilizando la API gratuita de Microsoft Translator.

		:param lang_from: Idioma de origen.
		:param lang_to: Idioma de destino.
		:param text: Texto a traducir.
		:return: Traducción del texto.
		"""
		try:
			endpoint = self.get_endpoint(lang_to, lang_from)
			headers = self.get_headers()
			body = self.get_body(text)
			request = Request(endpoint, data=body.encode('utf-8'), headers=headers)
			response = urlopen(request)

			if response.status != 200:
				raise Exception(f'Error en la traducción: {response.read().decode("utf-8")}')

			translate_data = json.loads(response.read().decode('utf-8'))[0]['translations'][0]['text']

		except Exception as e:
			msg = f"""Error en la traducción.

Error:

{str(e)}"""
			logHandler.log.error(msg)
			return text  # Devuelve el texto original en caso de error

		return translate_data
