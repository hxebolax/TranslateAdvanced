# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import json
import os

# Carga traducción
addonHandler.initTranslation()

class APIManager:
	"""
	Gestiona las operaciones de lectura y escritura en el archivo JSON para las claves API.
	"""
	def __init__(self, filepath):
		self.filepath = filepath
		if not os.path.exists(filepath):
			self.data = {
				"deepL_free": [],
				"deepL_pro": [],
				"libre_translate": []
			}
			self.save()
		else:
			self.load()

	def load(self):
		"""
		Carga los datos desde el archivo JSON.
		"""
		try:
			with open(self.filepath, 'r', encoding='utf-8') as file:
				self.data = json.load(file)
		except (FileNotFoundError, json.JSONDecodeError) as e:
			logHandler.log.error(_("Error al cargar el archivo JSON: {0}").format(e))
			self.data = {
				"deepL_free": [],
				"deepL_pro": [],
				"libre_translate": []
			}

	def save(self):
		"""
		Guarda los datos en el archivo JSON.
		"""
		try:
			with open(self.filepath, 'w', encoding='utf-8') as file:
				json.dump(self.data, file, ensure_ascii=False, indent=4)
		except IOError as e:
			logHandler.log.error(_("Error al guardar el archivo JSON: {0}").format(e))

	def add_api(self, service, name, key, url=None):
		"""
		Añade una nueva clave API.

		:param service: Nombre del servicio (deepL_free, deepL_pro, libre_translate).
		:param name: Nombre descriptivo de la clave.
		:param key: Clave API.
		:param url: URL del servicio (solo para libre_translate).
		"""
		if service not in self.data:
			logHandler.log.error(_("Servicio desconocido: {0}").format(service))
			return
		entry = {"name": name, "key": key}
		if url:
			entry["url"] = url
		self.data[service].append(entry)
		self.save()

	def edit_api(self, service, index, name, key, url=None):
		"""
		Edita una clave API existente.

		:param service: Nombre del servicio (deepL_free, deepL_pro, libre_translate).
		:param index: Índice de la clave a editar.
		:param name: Nombre descriptivo de la clave.
		:param key: Clave API.
		:param url: URL del servicio (solo para libre_translate).
		"""
		if service not in self.data:
			logHandler.log.error(_("Servicio desconocido: {0}").format(service))
			return
		if index < 0 or index >= len(self.data[service]):
			logHandler.log.error(_("Índice fuera de rango: {0}").format(index))
			return
		entry = {"name": name, "key": key}
		if url:
			entry["url"] = url
		self.data[service][index] = entry
		self.save()

	def delete_api(self, service, index):
		"""
		Elimina una clave API.

		:param service: Nombre del servicio (deepL_free, deepL_pro, libre_translate).
		:param index: Índice de la clave a eliminar.
		"""
		if service not in self.data:
			logHandler.log.error(_("Servicio desconocido: {0}").format(service))
			return
		if index < 0 or index >= len(self.data[service]):
			logHandler.log.error(_("Índice fuera de rango: {0}").format(index))
			return
		try:
			del self.data[service][index]
			self.save()
		except IndexError as e:
			logHandler.log.error(_("Error al eliminar la clave API: {0}").format(e))

	def get_apis(self, service):
		"""
		Obtiene todas las claves API de un servicio.

		:param service: Nombre del servicio (deepL_free, deepL_pro, libre_translate).
		:return: Lista de claves API.
		"""
		if service not in self.data:
			logHandler.log.error(_("Servicio desconocido: {0}").format(service))
			return []
		return self.data[service]

	def get_api(self, service, index):
		"""
		Obtiene una clave API específica.

		:param service: Nombre del servicio (deepL_free, deepL_pro, libre_translate).
		:param index: Índice de la clave.
		:return: Clave API.
		"""
		if service not in self.data:
			logHandler.log.error(_("Servicio desconocido: {0}").format(service))
			return None
		if index < 0 or index >= len(self.data[service]):
			logHandler.log.error(_("Índice fuera de rango: {0}").format(index))
			return None
		try:
			return self.data[service][index]
		except IndexError as e:
			logHandler.log.error(_("Error al obtener la clave API: {0}").format(e))
			return None
