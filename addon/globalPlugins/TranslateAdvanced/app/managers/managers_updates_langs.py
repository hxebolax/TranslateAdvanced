# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import os
import json
import urllib.request
import zipfile

# Carga traducción
addonHandler.initTranslation()

class GestorRepositorios:
	"""
	Clase para gestionar la descarga y actualización de idiomas desde un repositorio de GitHub.
	"""
	def __init__(self, frame, github_repo, rama='master', local_dir='.', json_file='languages.json'):

		self.frame = frame
		self.github_repo = github_repo
		self.rama = rama
		self.local_dir = local_dir
		self.json_file = json_file
		if not os.path.exists(self.json_file):
			with open(self.json_file, 'w') as file:
				json.dump({}, file, indent='\t')

	def cargar_idiomas_locales(self):
		"""
		Carga el archivo de idiomas JSON local.
		
		:return: Diccionario de resultado con success y data
		"""
		try:
			with open(self.json_file, 'r') as file:
				idiomas = json.load(file)
			return {'success': True, 'data': idiomas}
		except Exception as e:
			msg = _("Error al cargar idiomas locales: {}").format(str(e))
			logHandler.log.error(msg)
			return {'success': False, 'data': msg}

	def guardar_idiomas_locales(self, idiomas):
		"""
		Guarda el diccionario de idiomas en el archivo JSON local.
		
		:param idiomas: Diccionario de idiomas a guardar
		:return: Diccionario de resultado con success y data
		"""
		try:
			with open(self.json_file, 'w') as file:
				json.dump(idiomas, file, indent='\t')
			return {'success': True, 'data': _('Idiomas guardados exitosamente.')}
		except Exception as e:
			msg = _("Error al guardar idiomas locales: {}").format(str(e))
			logHandler.log.error(msg)
			return {'success': False, 'data': msg}

	def obtener_idiomas_remotos(self):
		"""
		Obtiene la lista de idiomas y versiones desde el repositorio de GitHub.
		
		:return: Diccionario de resultado con success y data
		"""
		try:
			url = f"https://raw.githubusercontent.com/{self.github_repo}/{self.rama}/translates/languages.json"
			req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
			with urllib.request.urlopen(req) as response:
				if response.status == 200:
					idiomas = json.loads(response.read().decode())
					return {'success': True, 'data': idiomas}
				else:
					msg = _("Error al obtener idiomas remotos: {}").format(response.status)
					logHandler.log.error(msg)
					return {'success': False, 'data': msg}
		except Exception as e:
			msg = _("Error al obtener idiomas remotos: {}").format(str(e))
			logHandler.log.error(msg)
			return {'success': False, 'data': msg}
	def comprobar_nuevos_y_actualizaciones(self):
		"""
		Comprueba si hay nuevos idiomas y actualizaciones en el repositorio de GitHub.
		
		:return: Diccionario de resultado con success y data
		"""
		result_locales = self.cargar_idiomas_locales()
		if not result_locales['success']:
			return result_locales['data']

		result_remotos = self.obtener_idiomas_remotos()
		if not result_remotos['success']:
			return result_remotos['data']

		idiomas_locales = result_locales['data']
		idiomas_remotos = result_remotos['data']
		nuevos_idiomas = {idioma: version for idioma, version in idiomas_remotos.items() if idioma not in idiomas_locales}
		idiomas_para_actualizar = {idioma: version for idioma, version in idiomas_remotos.items() if idioma in idiomas_locales and idiomas_locales[idioma] < version}
		
		if nuevos_idiomas or idiomas_para_actualizar:
			return {'success': True, 'data': {'nuevos': nuevos_idiomas, 'actualizaciones': idiomas_para_actualizar}}
		else:
			return {'success': False, 'data': _('No hay actualizaciones ni nuevos idiomas disponibles.')}

	def descargar_zip(self, idioma, widget_progreso=None):
		"""
		Descarga el archivo .zip de un idioma desde el repositorio de GitHub.
		
		:param idioma: Código del idioma a descargar
		:param widget_progreso: Widget de wxPython para mostrar el progreso de la descarga
		:return: Diccionario de resultado con success y data
		"""
		try:
			url = f"https://github.com/{self.github_repo}/raw/{self.rama}/translates/{idioma}.zip"
			ruta_zip = os.path.join(self.local_dir, f"{idioma}.zip")
			req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
			with urllib.request.urlopen(req) as response:
				total_size = int(response.headers['Content-Length'])
				bytes_descargados = 0
				block_size = 1024
				with open(ruta_zip, 'wb') as file:
					while True:
						buffer = response.read(block_size)
						if not buffer:
							break
						file.write(buffer)
						bytes_descargados += len(buffer)
						if widget_progreso:
							widget_progreso.SetValue(bytes_descargados / total_size * 100)
			return {'success': True, 'data': msg}
		except Exception as e:
			msg = _("Error al descargar el archivo .zip de {}: {}").format(idioma, str(e))
			logHandler.log.error(msg)
			return {'success': False, 'data': msg}

	def descomprimir_zip(self, idioma, ruta_destino=None, widget_progreso=None):
		"""
		Descomprime el archivo .zip de un idioma en una ruta específica.
		
		:param idioma: Código del idioma a descomprimir
		:param ruta_destino: Ruta donde se descomprimirá el contenido (por defecto, el directorio de descompresión predeterminado)
		:param widget_progreso: Widget de wxPython para mostrar el progreso de la descompresión
		:return: Diccionario de resultado con success y data
		"""
		if ruta_destino is None:
			ruta_destino = self.local_dir
		
		try:
			ruta_zip = os.path.join(self.local_dir, f"{idioma}.zip")
			with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
				archivos = zip_ref.namelist()
				total_files = len(archivos)
				for i, archivo in enumerate(archivos):
					zip_ref.extract(archivo, ruta_destino)
					if widget_progreso:
						widget_progreso.SetValue((i + 1) / total_files * 100)
			os.remove(ruta_zip)
			return {'success': True, 'data': msg}
		except Exception as e:
			msg = _("Error al descomprimir el archivo .zip de {}: {}").format(idioma, str(e))
			logHandler.log.error(msg)
			return {'success': False, 'data': msg}

	def actualizar_idioma_local(self, idioma, version):
		"""
		Actualiza la versión de un idioma en el archivo JSON local.
		
		:param idioma: Código del idioma a actualizar
		:param version: Nueva versión del idioma
		:return: Diccionario de resultado con success y data
		"""
		try:
			result = self.cargar_idiomas_locales()
			if not result['success']:
				return result

			idiomas_locales = result['data']
			idiomas_locales[idioma] = version
			result = self.guardar_idiomas_locales(idiomas_locales)
			if result['success']:
				return {'success': True, 'data': msg}
			else:
				return result
		except Exception as e:
			msg = _("Error al actualizar el idioma local {}: {}").format(idioma, str(e))
			logHandler.log.error(msg)
			return {'success': False, 'data': msg}

	def obtener_lista_idiomas(self, idiomas_dict):
		"""
		Obtiene una lista de idiomas a partir de un diccionario de idiomas y versiones.
		
		:param idiomas_dict: Diccionario de idiomas y versiones
		:return: Lista de idiomas
		"""
		return list(idiomas_dict.keys())

	def obtener_lista_versiones(self, idiomas_dict):
		"""
		Obtiene una lista de versiones a partir de un diccionario de idiomas y versiones.
		
		:param idiomas_dict: Diccionario de idiomas y versiones
		:return: Lista de versiones
		"""
		return list(idiomas_dict.values())
