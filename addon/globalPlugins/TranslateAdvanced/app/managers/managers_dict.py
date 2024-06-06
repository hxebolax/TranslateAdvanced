# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler

# Carga traducción
addonHandler.initTranslation()

class LanguageDictionary:
	"""
	Clase para manejar el diccionario de idiomas y proporcionar funciones útiles para acceder a claves y valores.
	"""

	def __init__(self, lang_dict):
		"""
		Inicializa la clase con un diccionario de idiomas.

		:param lang_dict: Diccionario de idiomas.
		"""
		self.lang_dict = lang_dict
		self.keys_list = list(lang_dict.keys())
		self.values_list = list(lang_dict.values())

	def get_keys(self):
		"""
		Obtiene todas las claves del diccionario de idiomas.

		:return: Lista de claves.
		"""
		return self.keys_list

	def get_values(self):
		"""
		Obtiene todos los valores del diccionario de idiomas.

		:return: Lista de valores.
		"""
		return self.values_list

	def get_key_by_index(self, index):
		"""
		Obtiene la clave correspondiente a un índice dado.

		:param index: Índice de la clave.
		:return: Clave correspondiente al índice.
		"""
		try:
			return self.keys_list[index]
		except IndexError:
			logHandler.log.error(_("Índice fuera de rango: {index}").format(index=index))
			return None

	def get_value_by_index(self, index):
		"""
		Obtiene el valor correspondiente a un índice dado.

		:param index: Índice del valor.
		:return: Valor correspondiente al índice.
		"""
		try:
			return self.values_list[index]
		except IndexError:
			logHandler.log.error(_("Índice fuera de rango: {index}").format(index=index))
			return None

	def get_index_by_key_or_value(self, key_or_value):
		"""
		Obtiene el índice correspondiente a una clave o un valor dado.

		:param key_or_value: Clave o valor a buscar.
		:return: Índice correspondiente a la clave o el valor, o None si no se encuentra.
		"""
		if key_or_value in self.lang_dict:
			return self.keys_list.index(key_or_value)
		elif key_or_value in self.lang_dict.values():
			return self.values_list.index(key_or_value)
		else:
			logHandler.log.error(_("Clave o valor no encontrado: {key_or_value}").format(key_or_value=key_or_value))
			return None
