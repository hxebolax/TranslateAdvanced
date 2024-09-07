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
		self.required_services = ["deepL_free", "deepL_pro", "libre_translate", "openai"]
		if not os.path.exists(filepath):
			self.data = {service: [] for service in self.required_services}
			self.save()
		else:
			self.load()
			self.ensure_services_exist()

	def load(self):
		"""
		Carga los datos desde el archivo JSON.
		"""
		try:
			with open(self.filepath, 'r', encoding='utf-8') as file:
				self.data = json.load(file)
		except (FileNotFoundError, json.JSONDecodeError) as e:
			logHandler.log.error(_("Error al cargar el archivo JSON: {0}").format(e))
			self.data = {service: [] for service in self.required_services}

	def save(self):
		"""
		Guarda los datos en el archivo JSON.
		"""
		try:
			with open(self.filepath, 'w', encoding='utf-8') as file:
				json.dump(self.data, file, ensure_ascii=False, indent=4)
		except IOError as e:
			logHandler.log.error(_("Error al guardar el archivo JSON: {0}").format(e))

	def ensure_services_exist(self):
		"""
		Asegura que todos los servicios requeridos existan en los datos.
		Si algún servicio no existe, lo añade con una lista vacía.
		"""
		changed = False
		for service in self.required_services:
			if service not in self.data:
				self.data[service] = []
				changed = True
		if changed:
			self.save()

	def add_api(self, service, name, key, url=None):
		"""
		Añade una nueva clave API.

		:param service: Nombre del servicio (deepL_free, deepL_pro, libre_translate, openai).
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

		:param service: Nombre del servicio (deepL_free, deepL_pro, libre_translate, openai).
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

		:param service: Nombre del servicio (deepL_free, deepL_pro, libre_translate, openai).
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

		:param service: Nombre del servicio (deepL_free, deepL_pro, libre_translate, openai).
		:return: Lista de claves API.
		"""
		if service not in self.data:
			logHandler.log.error(_("Servicio desconocido: {0}").format(service))
			return []
		return self.data[service]

	def get_api(self, service, index):
		"""
		Obtiene una clave API específica.

		:param service: Nombre del servicio (deepL_free, deepL_pro, libre_translate, openai).
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
