# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import urllib.request
import urllib.error
import json
import time
import random
import gzip
from io import BytesIO

# Carga traducción
addonHandler.initTranslation()

class TranslatorDeepLFree:
	"""
	Clase para utilizar el servicio gratuito de traducción de DeepL.
	"""
	def __init__(self):
		"""
		Inicializa una instancia del traductor gratuito DeepL.
		"""
		self.source_lang = None
		self.target_lang = None
		self.endpoint = 'https://www2.deepl.com/jsonrpc?client=chrome-extension,1.5.1'

	def _vars(self, text):
		"""
		Genera variables únicas necesarias para la solicitud.

		:param text: Texto a traducir.
		:return: uid y timestamp.
		"""
		uid = random.randint(1000000000, 9999999999)
		count_i = text.count('i')
		ts = int(time.time() * 1000)
		if count_i > 0:
			count_i += 1
			ts = ts - ts % count_i + count_i
		return uid, ts

	def get_headers(self):
		"""
		Genera los encabezados necesarios para la solicitud.

		:return: Diccionario con los encabezados.
		"""
		return {
			'Accept': '*/*',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9',
			'Authorization': 'None',
			'Authority': 'www2.deepl.com',
			'Content-Type': 'application/json; charset=utf-8',
			'User-Agent': 'DeepLBrowserExtension/1.5.1 Mozilla/5.0 (Macintosh; '
						'Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
						'like Gecko) Chrome/114.0.0.0 Safari/537.36',
			'Origin': 'chrome-extension://cofdbpoegempjloogbagkncekinflcnj',
			'Referer': 'https://www.deepl.com/',
		}

	def get_body(self, text):
		"""
		Genera el cuerpo de la solicitud.

		:param text: Texto a traducir.
		:return: Cuerpo de la solicitud en formato JSON.
		"""
		regional_variant = {}
		target_lang = self._get_target_code()
		if '-' in target_lang:
			portions = target_lang.split('-')
			variant = '-'.join([portions[0].lower(), portions[1]])
			regional_variant['regionalVariant'] = variant
			target_lang = portions[0]
		uid, ts = self._vars(text)

		body = json.dumps({
			'jsonrpc': '2.0',
			'method': 'LMT_handle_texts',
			'params': {
				'commonJobParams': regional_variant,
				'texts': [{'text': text}],
				'splitting': 'newlines',
				'lang': {
					'source_lang_user_selected': self._get_source_code(),
					'target_lang': target_lang,
				},
				'timestamp': ts
			},
			'id': uid
		}, separators=',:')

		if (uid + 3) % 13 == 0 or (uid + 5) % 29 == 0:
			return body.replace('"method":"', '"method" : "')
		return body.replace('"method":"', '"method": "')

	def get_result(self, response):
		"""
		Extrae el resultado de la traducción de la respuesta.

		:param response: Respuesta de la solicitud HTTP.
		:return: Texto traducido.
		"""
		return json.loads(response)['result']['texts'][0]['text']

	def _get_source_code(self):
		"""
		Obtiene el código del idioma de origen.

		:return: Código del idioma de origen.
		"""
		return self.source_lang if self.source_lang else 'auto'

	def _get_target_code(self):
		"""
		Obtiene el código del idioma de destino.

		:return: Código del idioma de destino.
		"""
		return self.target_lang

	def translate(self, text):
		"""
		Traduce un texto utilizando la API gratuita de DeepL.

		:param text: Texto a traducir.
		:return: Texto traducido.
		"""
		headers = self.get_headers()
		body = self.get_body(text).encode('utf-8')
		request = urllib.request.Request(self.endpoint, data=body, headers=headers, method='POST')
		try:
			with urllib.request.urlopen(request, timeout=10) as response:
				# Comprueba si la respuesta está comprimida y descomprímela si es necesario
				if response.info().get('Content-Encoding') == 'gzip':
					buf = BytesIO(response.read())
					with gzip.GzipFile(fileobj=buf) as f:
						result = f.read().decode('utf-8')
				else:
					result = response.read().decode('utf-8')
				return self.get_result(result)
		except urllib.error.HTTPError as e:
			error_message = e.read().decode('utf-8')
			logHandler.log.error(_("Error HTTP: {0} - {1}").format(e.code, error_message))
			return text
		except urllib.error.URLError as e:
			logHandler.log.error(_("Error de red: {0}").format(e.reason))
			return text
		except Exception as e:
			logHandler.log.error(_("Error inesperado: {0}").format(str(e)))
			return text
