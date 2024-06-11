# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import globalVars
import logHandler
import braille
from speech import *
# Carga estándar

import re
# Carga personal
from ..src_translations.src_google_original import TranslatorGoogle
from ..src_translations.src_google_alternative import TranslatorGooglealternative
from ..src_translations.src_google_api_free import TranslatorGoogleApiFree
from ..src_translations.src_google_api_free_alternative import TranslatorGoogleApiFreeAlternative
from ..src_translations.src_deepl_original import TranslatorDeepL
from ..src_translations.src_libretranslate_original import TranslatorLibreTranslate
from ..src_translations.src_microsoft_api_free import TranslatorMicrosoftApiFree

# Carga traducción
addonHandler.initTranslation()

class GestorTranslate(
	TranslatorGoogle, 
	TranslatorGooglealternative, 
	TranslatorDeepL,
	TranslatorLibreTranslate,
	TranslatorMicrosoftApiFree,
):
	"""
	Clase que gestiona la traducción de texto y el manejo del historial de traducción.
	"""
	def __init__(self, frame):
		"""
		Inicializa la clase con el marco de la aplicación.

		:param frame: El marco principal de la aplicación.
		"""
		super().__init__()
		self.frame = frame

	def get_choice_lang_destino(self):
		"""
		Devuelve el contenido de la variable choiceLangDestino correspondiente según el valor de choiceOnline.

		Returns:
			El contenido de la variable choiceLangDestino correspondiente o None si choiceOnline no es válido.
		"""
		value = self.frame.gestor_settings.choiceOnline
		if value in [0, 1, 2, 3]:
			return self.frame.gestor_settings.choiceLangDestino_google
		elif value in [4, 5]:
			return self.frame.gestor_settings.choiceLangDestino_deepl
		elif value == 6:
			return self.frame.gestor_settings.choiceLangDestino_libretranslate
		elif value == 7:
			return self.frame.gestor_settings.choiceLangDestino_microsoft

	def get_api(self):
		"""
		Obtiene la clave y, en algunos casos, la URL de la API según la configuración seleccionada.

		Dependiendo del valor de `choiceOnline` en `gestor_settings`, esta función retorna la clave de 
		acceso a la API correspondiente y, si aplica, la URL de la API.

		Returns:
			tuple: Una tupla que contiene la clave de la API y la URL (si aplica). Si no se encuentra 
			la configuración de la API correspondiente, retorna (None, None).

		Condiciones:
			- Si `choiceOnline` es 4, se usa la API gratuita de DeepL.
				- Si `api_deepl` es None, retorna (None, None).
				- En caso contrario, retorna la clave de la API y None.
			- Si `choiceOnline` es 5, se usa la API profesional de DeepL.
				- Si `api_deepl_pro` es None, retorna (None, None).
				- En caso contrario, retorna la clave de la API y None.
			- Si `choiceOnline` es 6, se usa la API de LibreTranslate.
				- Si `api_libretranslate` es None, retorna (None, None).
				- En caso contrario, retorna la clave de la API y la URL de la API.

		"""
		value = self.frame.gestor_settings.choiceOnline
		if value == 4:
			if self.frame.gestor_settings.api_deepl is None:
				return None, None
			else:
				return self.frame.gestor_apis.get_api("deepL_free", self.frame.gestor_settings.api_deepl)["key"], None
		elif value == 5:
			if self.frame.gestor_settings.api_deepl_pro is None:
				return None, None
			else:
				return self.frame.gestor_apis.get_api("deepL_pro", self.frame.gestor_settings.api_deepl_pro)["key"], None
		elif value == 6:
			if self.frame.gestor_settings.api_libretranslate is None:
				return None, None
			else:
				return self.frame.gestor_apis.get_api("libre_translate", self.frame.gestor_settings.api_libretranslate)["key"],  self.frame.gestor_apis.get_api("libre_translate", self.frame.gestor_settings.api_libretranslate)["url"]

	def procesar_listas(self, origen, destino):
		"""
		Procesa dos listas para unificar sus cadenas de texto, eliminar los espacios al final de cada cadena,
		y omitir los elementos que no son cadenas de texto.

		Parámetros:
		origen (list): La lista origen que contiene cadenas de texto y otros tipos de datos.
		destino (list): La lista destino que contiene cadenas de texto y otros tipos de datos.

		Retorna:
		dict: Un diccionario con 'origen' y 'destino' como claves y las listas procesadas como valores.
		"""
		def procesar_lista(lista):
			"""
			Procesa una lista para unificar sus cadenas de texto, eliminar los espacios al final de cada cadena,
			y omitir los elementos que no son cadenas de texto.

			Parámetros:
			lista (list): La lista que contiene cadenas de texto y otros tipos de datos.

			Retorna:
			str: Una cadena de texto unificada sin espacios al final.
			"""
			# Crear una lista para almacenar los textos procesados
			lista_textos = []

			# Recorrer cada elemento en la lista
			for elemento in lista:
				# Verificar si el elemento es una cadena de texto
				if isinstance(elemento, str):
					# Eliminar los espacios al final y añadir a la lista de textos
					lista_textos.append(elemento.rstrip())

			# Unir todos los elementos de texto en una sola cadena con un espacio entre ellos
			texto_unido = ' '.join(lista_textos)

			return texto_unido

		# Procesar las listas origen y destino
		origen_procesado = procesar_lista(origen)
		destino_procesado = procesar_lista(destino)

		# Devolver un diccionario con las listas procesadas
		return {'origen': origen_procesado, 'destino': destino_procesado}

	def translate_file(self, text, func_progress):
		"""
		Traduce el contenido de un archivo de texto.

		:param text: El texto a traducir.
		:param func_progress: Función para mostrar el progreso de la traducción.
		:return: El texto traducido.
		"""
		prepared = text
		translated = TranslatorGoogleApiFree().translate_google_api_free(lang_from='auto', lang_to=self.frame.gestor_settings.choiceLangDestino_google, text=prepared, chunksize=3000, mostrar_progreso=True, widget=func_progress)
		return translated

	def translate(self, text):
		"""
		Traduce un texto dado según la configuración actual.

		:param text: El texto a traducir.
		:return: El texto traducido.
		"""
		try:
			appName = "{}_{}".format(globalVars.focusObject.appModule.appName, self.get_choice_lang_destino())
		except:
			appName = "__global__"

		if not self.frame.gestor_settings._enableTranslation:
			return text

		if self.frame.gestor_settings.chkCache:
			appTable = self.frame.gestor_settings._translationCache.get(appName, None)
			if appTable is None:
				self.frame.gestor_settings._translationCache[appName] = {}
			translated = self.frame.gestor_settings._translationCache[appName].get(text, None)
			if translated and translated != text:
				return translated

		try:
			if self.frame.gestor_settings._enableTranslation:
				id = self.frame.gestor_settings.choiceOnline
				if id == 0: # Google 1
					prepared = text.encode('utf8', ':/')
					translated = self.translate_google(prepared, to_language=self.frame.gestor_settings.choiceLangDestino_google)
				elif id == 1: # Google 2
					prepared = text.encode('utf8', ':/')
					translated = self.translate_google_alternative(prepared, target=self.frame.gestor_settings.choiceLangDestino_google)
				elif id == 2: # Google 3
					prepared = text
					translated = TranslatorGoogleApiFree().translate_google_api_free(lang_from='auto', lang_to=self.frame.gestor_settings.choiceLangDestino_google, text=prepared, chunksize=3000, mostrar_progreso=False)
				elif id == 3: # Google 4 API con Toquen
					prepared = text
					translated = TranslatorGoogleApiFreeAlternative().translate_google_api_free(lang_from='auto', lang_to=self.frame.gestor_settings.choiceLangDestino_google, text=prepared, chunksize=3000, mostrar_progreso=False)
				elif id == 4: # DeepL Free
					api_key, url = self.get_api()
					if api_key is None:
						logHandler.log.error(_("No tiene ninguna API configurada para el servicio que tiene seleccionado."))

						return text
					prepared = text.encode('utf8', ':/')
					datos = self.translate_deepl(prepared, api_key, use_free_api=True,  source_lang="auto", target_lang=self.frame.gestor_settings.choiceLangDestino_deepl)
					if isinstance(datos, bytes):
						translated =  datos.decode('utf-8')
					elif isinstance(datos, str):
						translated = datos
					else:
						translated = text
				elif id == 5: # DeepL Pro
					api_key, url = self.get_api()
					if api_key is None:
						logHandler.log.error(_("No tiene ninguna API configurada para el servicio que tiene seleccionado."))
						return text
					prepared = text.encode('utf8', ':/')
					datos = self.translate_deepl(prepared, api_key, use_free_api=False,  source_lang="auto", target_lang=self.frame.gestor_settings.choiceLangDestino_deepl)
					if isinstance(datos, bytes):
						translated =  datos.decode('utf-8')
					elif isinstance(datos, str):
						translated = datos
					else:
						translated = text
				elif id == 6: # LibreTranslate
					api_key, url = self.get_api()
					if api_key is None:
						logHandler.log.error(_("No tiene ninguna API configurada para el servicio que tiene seleccionado."))
						return text
					if url is None:
						logHandler.log.error(_("No tiene ninguna API configurada para el servicio que tiene seleccionado."))
						return text
					prepared = text
					translated = self.translate_libretranslate(prepared, api_key, source_lang="auto", target_lang=self.frame.gestor_settings.choiceLangDestino_libretranslate, api_url=url)
				elif id == 7: # Microsoft
					prepared = text
					translated = self.translate_microsoft_api_free(self.frame.gestor_settings.choiceLangOrigen, self.frame.gestor_settings.choiceLangDestino_microsoft, prepared)
		except Exception as e:
			msg = \
_("""Error en la traducción.

Error:

{}""").format(str(e))
			logHandler.log.error(msg)
			return text

		if not translated:
			translated = text
		else:
			if self.frame.gestor_settings.chkCache:
				self.frame.gestor_settings._translationCache[appName][text] = translated

		return translated

	def speak(self, speechSequence: SpeechSequence, priority: Spri = None):
		"""
		Genera una secuencia de habla y la traduce si es necesario.

		:param speechSequence: La secuencia de texto a hablar.
		:param priority: La prioridad de la secuencia de habla (opcional).
		:return: None
		"""
		if not self.frame.gestor_settings._enableTranslation:
			return self.frame.gestor_settings._nvdaSpeak(speechSequence=speechSequence, priority=priority)

		newSpeechSequence = []
		newSpeechSequenceOrigen = []
		newSpeechSequenceDestino = []

		for val in speechSequence:
			if isinstance(val, str):
				v = self.translate(val)
				newSpeechSequence.append(v if v is not None else val)
				newSpeechSequenceOrigen.append(val)
				newSpeechSequenceDestino.append(v)
			else:
				newSpeechSequence.append(val)

		self.frame.gestor_settings._nvdaSpeak(speechSequence=newSpeechSequence, priority=priority)

		temp = self.procesar_listas(newSpeechSequenceOrigen, newSpeechSequenceDestino)
		if temp['origen'] not in self.frame.gestor_settings.historialOrigen:
			self.frame.gestor_settings.historialOrigen.appendleft(temp['origen'])
			self.frame.gestor_settings.historialDestino.appendleft(temp['destino'])
			self.frame.gestor_settings._lastTranslatedText = temp['destino']
			braille.handler.message(self.frame.gestor_settings._lastTranslatedText)

