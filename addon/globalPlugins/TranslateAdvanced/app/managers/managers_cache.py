# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
# Carga Python
import os
import json
import codecs
import re

# Carga traducción
addonHandler.initTranslation()

class LocalCacheHandler:
	"""
	Clase para manejar la carga y almacenamiento de la caché local de traducciones.

	Esta clase proporciona métodos para cargar y guardar una caché de traducciones
	almacenada localmente en formato JSON.
	"""

	def __init__(self, settings, logHandler):
		"""
		Inicializa el manejador de la caché local.

		Args:
			settings: Un objeto de configuración que incluye la ruta de la caché y la caché de traducción.
			logHandler: Manejador de registro para registrar errores y operaciones.
		"""
		self.settings = settings
		self.logHandler = logHandler

	def loadLocalCache(self):
		"""
		Carga la caché de traducciones desde archivos JSON en el directorio especificado.

		Los errores durante la creación del directorio o la lectura de archivos se registran.
		"""
		path = self.settings.dir_cache
		if not os.path.exists(path):
			try:
				os.mkdir(path)
			except Exception as e:
				self.logHandler.log.error(_("Fallo al crear la ruta de almacenamiento: {path} ({e})").format(path=path, e=e))
				return

		for entry in os.listdir(path):
			m = re.match("(.*)\.json$", entry)
			if m:
				appName = m.group(1)
				try:
					with codecs.open(os.path.join(path, entry), "r", "utf-8") as cacheFile:
						values = json.load(cacheFile)
						self.settings._translationCache[appName] = values
				except Exception as e:
					self.logHandler.log.error(_("No se puede leer o decodificar datos desde {path}: {e}").format(path=path, e=e))
					continue

	def saveLocalCache(self):
		"""
		Guarda la caché de traducciones en archivos JSON en el directorio especificado.

		Se capturan y registran errores durante el guardado de los datos.
		"""
		path = self.settings.dir_cache
		for appName, data in self.settings._translationCache.items():
			file = os.path.join(path, f"{appName}.json")
			try:
				with codecs.open(file, "w", "utf-8") as cacheFile:
					json.dump(data, cacheFile, ensure_ascii=False)
			except Exception as e:
				self.logHandler.log.error(_("Fallo al guardar la caché de traducción para {appName} en {file}: {e}").format(appName=appName, file=file, e=e))
