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

class DetectorDeIdioma:
	"""
	Clase para detectar el idioma de un texto usando el raspado web de Google Translate.
	"""
	
	def __init__(self):
		"""
		Inicializa la clase con la URL base de la API de Google Translate.
		"""
		self.url_base = 'https://translate.googleapis.com/translate_a/single'
	
	def detectar_idioma(self, texto):
		"""
		Detecta el idioma de un texto dado.
		
		Args:
			texto (str): El texto del cual se desea detectar el idioma.
		
		Returns:
			dict: Un diccionario con el éxito de la operación y el idioma detectado o el texto original en caso de error.
		"""
		try:
			# Limitar el texto a 5000 caracteres si es necesario
			texto_limited = texto[:5000]
			
			# Codificar los parámetros para la solicitud
			parametros = {
				'client': 'gtx',
				'sl': 'auto',  # Detectar idioma automáticamente
				'dt': 't',  # Tipo de respuesta
				'q': texto_limited,
				'tl': 'en'  # Traducir a inglés (aunque solo nos interesa la detección del idioma)
			}
			url_parametros = urllib.parse.urlencode(parametros, encoding='utf-8', errors='surrogatepass')
			url_completa = f"{self.url_base}?{url_parametros}"
			
			# Realizar la solicitud GET a Google Translate
			with urllib.request.urlopen(url_completa) as response:
				response_data = response.read().decode('utf-8', 'surrogatepass')
			
			# Parsear la respuesta JSON
			data = json.loads(response_data)
			
			# Verificar si el idioma detectado está presente en la respuesta
			if data and len(data) > 2 and data[2]:
				idioma_detectado = data[2]  # El idioma detectado está en la tercera posición
				return {"success": True, "data": idioma_detectado}
			else:
				logHandler.log.error(_("No se pudo detectar el idioma"))
				return {"success": False, "data": texto}
		
		except urllib.error.URLError as e:
			logHandler.log.error(_("Error de conexión: {0}").format(e.reason))
			return {"success": False, "data": texto}
		except urllib.error.HTTPError as e:
			logHandler.log.error(_("Error HTTP: {0} {1}").format(e.code, e.reason))
			return {"success": False, "data": texto}
		except Exception as e:
			logHandler.log.error(_("Ocurrió un error inesperado: {0}").format(str(e)))
			return {"success": False, "data": texto}
