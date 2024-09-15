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

class TranslatorGooglealternative:
	"""
	Clase que maneja traducciones utilizando la interfaz web de Google Translate.
	"""
	
	def __init__(self):
		"""
		Inicializa una instancia del traductor de Google.
		"""
		pass
	
	def translate_google_alternative(self, text, source="auto", target="en"):
		"""
		Traduce un texto utilizando Google Translate.
		
		:param text: Texto a traducir.
		:param source: Idioma de origen para la traducción.
		:param target: Idioma de destino para la traducción.
		:return: Texto traducido.
		"""
		base_url = "https://translate.google.com/m"
		params = {
			"sl": source,
			"tl": target,
			"ie": "UTF-8",
			"prev": "_m",
			"q": text
		}
		url = f"{base_url}?{urllib.parse.urlencode(params)}"
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

		req = urllib.request.Request(url, headers=headers)
		try:
			with urllib.request.urlopen(req) as response:
				response_data = response.read().decode()
				translated_text = self._extract_translation(response_data)
				return translated_text
		except urllib.error.HTTPError as e:
			logHandler.log.error(_("Error en la traducción: {0} {1}").format(e.code, e.reason))
			return _("Error en la traducción: {0} {1}").format(e.code, e.reason)
		except Exception as e:
			logHandler.log.error(_("Error en la traducción: {0}").format(str(e)))
			return _("Error en la traducción: {0}").format(str(e))

	def _extract_translation(self, response_data):
		"""
		Extrae la traducción del HTML de respuesta.
		
		:param response_data: Datos de respuesta en formato HTML.
		:return: Texto traducido.
		"""
		try:
			# Buscar la traducción en el HTML usando expresiones regulares
			match = re.search(r'class="result-container">(.*?)</div>', response_data)
			if match:
				return html.unescape(match.group(1))
			else:
				logHandler.log.error(_("Error al extraer la traducción: no se encontró el texto traducido."))
				return _("Error al extraer la traducción: no se encontró el texto traducido.")
		except Exception as e:
			logHandler.log.error(_("Error al analizar la respuesta de la traducción: {0}").format(str(e)))
			return _("Error al analizar la respuesta de la traducción: {0}").format(str(e))
