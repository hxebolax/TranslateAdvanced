# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import ssl
import urllib.request as urllibRequest
import urllib.parse

# Carga traducción
addonHandler.initTranslation()

# Configuración para ignorar la verificación SSL
ssl._create_default_https_context = ssl._create_unverified_context

class TranslatorMicrosoftApiFree:
	"""
	Clase para manejar la traducción de texto utilizando la API gratuita de Microsoft Translator.
	"""
	def __init__(self):
		"""
		Inicializa una instancia del traductor Microsoft Translator.
		"""
		pass

	def translate_microsoft_api_free(self, lang_from, lang_to, text, url="http://api.microsofttranslator.com/v2/ajax.svc/TranslateArray2?"):
		"""
		Traduce el texto de un idioma a otro utilizando la API gratuita de Microsoft Translator.

		:param lang_from: Idioma de origen.
		:param lang_to: Idioma de destino.
		:param text: Texto a traducir.
		:param url:  Url de la API.
		:return: Traducción del texto.
		"""
		data = {
			'from': '"' + lang_from + '"',
			'to': '"' + lang_to + '"',
			'texts': '["' + text + '"]',
			'options': "{}",
			'oncomplete': 'onComplete_3',
			'onerror': 'onError_3',
			'_': '1430745999189'
		}
		data = urllib.parse.urlencode(data).encode('utf-8')
		strUrl = url + data.decode() + "&appId=%223DAEE5B978BA031557E739EE1E2A68CB1FAD5909%22"

		try:
			request = urllibRequest.Request(strUrl)
			response = urllibRequest.urlopen(request)
			str_data = response.read().decode('utf-8')
			if '"TranslateApiException:' in str_data:
				raise ValueError(str_data)
			if '"TranslatedText":' not in str_data:
				raise ValueError(_("La respuesta no contiene {}").format('TranslatedText'))
			tmp, str_data = str_data.split('"TranslatedText":')
			translate_data = str_data[1:str_data.find('"', 1)]
		except Exception as e:
			msg = _("""Error en la traducción.

Error:

{}""").format(str(e))
			logHandler.log.error(msg)
			return text

		return translate_data
