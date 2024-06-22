# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import languageHandler
import config
import globalVars
import logHandler
# Carga Python
import os
from collections import deque

# Carga traducción
addonHandler.initTranslation()

class GestorSettings:
	"""
	Clase que encapsula la gestión y configuración de TranslateAdvanced.
	"""
	def __init__(self, frame):
		"""
		Inicializa la clase con el marco de la aplicación.

		:param frame: El marco principal de la aplicación.
		"""
		self.frame = frame
		self.dir_root = os.path.join(addonHandler.getCodeAddon().path, "globalPlugins", "TranslateAdvanced")
		self.dir_root_config = globalVars.appArgs.configPath
		self.dir_cache = os.path.join(self.dir_root_config, "TranslateAdvancedCache")
		self.file_api = os.path.join(os.environ['USERPROFILE'], "apis.json")
		self.historialOrigen = deque(maxlen=500)
		self.historialDestino = deque(maxlen=500)
		self._translationCache = {}

		self.IS_WinON = False
		self.is_active_translate = False
		self._enableTranslation = False
		self.servers_names = [
			_("Traductor Google (WEB 1)"),
			_("Traductor Google (WEB 2)"),
			_("Traductor Google (API Free 1)"),
			_("Traductor Google (API Free 2)"),
			_("Traductor DeepL (Free)"),
			_("Traductor DeepL (API Free *)"),
			_("Traductor DeepL (API Pro *)"),
			_("Traductor LibreTranslate (API *)"),
			_("Traductor Microsoft Bing (API Free)"),
		]
		self.service_map_selection = {
			_("Traductor Google (WEB 1)"): 0,
			_("Traductor Google (WEB 2)"): 1,
			_("Traductor Google (API Free 1)"): 2,
			_("Traductor Google (API Free 2)"): 3,
			_("Traductor DeepL (API Free *)"): 4,
			_("Traductor DeepL (API Pro *)"): 5,
			_("Traductor LibreTranslate (API *)"): 6,
			_("Traductor Microsoft Bing (API Free)"): 7,
			_("Traductor DeepL (Free)"): 8,
		}
		self.service_map = {
			_("Traductor DeepL (API Free *)"): "deepL_free",
			_("Traductor DeepL (API Pro *)"): "deepL_pro",
			_("Traductor LibreTranslate (API *)"): "libre_translate"
		}

		self._nvdaSpeak = None
		self._nvdaGetPropertiesSpeech = None
		self._lastTranslatedText = None
		self.ultimo_texto = None
		# Configuración a guardar
		self.choiceOnline = None
		self.choiceLangOrigen = None
		self.choiceLangDestino_google = None
		self.choiceLangDestino_deepl = None
		self.choiceLangDestino_libretranslate = None
		self.choiceLangDestino_microsoft = None
		self.chkCache = None
		self.chkResults = None
		self.api_deepl = None
		self.api_deepl_pro = None
		self.api_libretranslate = None
		self.api_libretranslate_url = None

		self.initConfiguration()
		self.setup()

	def initConfiguration(self):
		"""
		Inicializa la configuración de NVDA para TranslateAdvanced.
		"""
		confspec = {
			"choiceOnline": "integer(default=0, min=0, max=8)",
			"choiceLangOrigen": "string(default=en)",
			"choiceLangDestino_google": f"string(default={self.obtenerLenguaje()})",
			"choiceLangDestino_deepl": f"string(default={self.obtenerLenguaje()})",
			"choiceLangDestino_libretranslate": f"string(default={self.obtenerLenguaje()})",
			"choiceLangDestino_microsoft": f"string(default={self.obtenerLenguaje()})",
			"chkCache": "boolean(default=False)",
			"chkResults": "boolean(default=False)",
			"api_deepl": "string(default=None)",
			"api_deepl_pro": "string(default=None)",
			"api_libretranslate": "string(default=None)",
			"api_libretranslate_url": "string(default=None)",
		}
		config.conf.spec['TranslateAdvanced'] = confspec

	def getConfig(self, key):
		"""
		Obtiene un valor de configuración.

		:param key: La clave de configuración a obtener.
		:return: El valor de la configuración solicitada.
		"""
		return config.conf["TranslateAdvanced"][key]

	def setConfig(self, key, value):
		"""
		Establece un valor de configuración.

		:param key: La clave de configuración a establecer.
		:param value: El valor de configuración a establecer.
		"""
		try:
			config.conf.profiles[0]["TranslateAdvanced"][key] = value
		except:
			config.conf["TranslateAdvanced"][key] = value

	def setup(self):
		"""
		Configura la aplicación con los valores de configuración iniciales.
		"""
		self.choiceOnline = self.getConfig("choiceOnline")
		self.choiceLangOrigen = self.getConfig("choiceLangOrigen")
		self.choiceLangDestino_google = self.getConfig("choiceLangDestino_google")
		self.choiceLangDestino_deepl = self.getConfig("choiceLangDestino_deepl")
		self.choiceLangDestino_libretranslate = self.getConfig("choiceLangDestino_libretranslate")
		self.choiceLangDestino_microsoft = self.getConfig("choiceLangDestino_microsoft")
		self.chkCache = self.getConfig("chkCache")
		self.chkResults = self.getConfig("chkResults")
		self.api_deepl = self.convertir_valor(self.getConfig("api_deepl"))
		self.api_deepl_pro = self.convertir_valor(self.getConfig("api_deepl_pro"))
		self.api_libretranslate = self.convertir_valor(self.getConfig("api_libretranslate"))
		self.api_libretranslate_url = self.getConfig("api_libretranslate_url")

	def guardaConfiguracion(self):
		"""
		Guarda la configuración actual de la aplicación.
		"""
		self.setConfig("choiceOnline", self.choiceOnline)
		self.setConfig("choiceLangOrigen", self.choiceLangOrigen)
		self.setConfig("choiceLangDestino_google", self.choiceLangDestino_google)
		self.setConfig("choiceLangDestino_deepl", self.choiceLangDestino_deepl)
		self.setConfig("choiceLangDestino_libretranslate", self.choiceLangDestino_libretranslate)
		self.setConfig("choiceLangDestino_microsoft", self.choiceLangDestino_microsoft)
		self.setConfig("chkCache", self.chkCache)
		self.setConfig("chkResults", self.chkResults)
		self.setConfig("api_deepl", self.convertir_valor(self.api_deepl))
		self.setConfig("api_deepl_pro", self.convertir_valor(self.api_deepl_pro))
		self.setConfig("api_libretranslate", self.convertir_valor(self.api_libretranslate))
		self.setConfig("api_libretranslate_url", self.api_libretranslate_url)

	def obtenerLenguaje(self):
		"""
		Obtiene el lenguaje configurado para NVDA.

		:return: El código del lenguaje configurado.
		"""
		try:
			language = config.conf["general"]["language"]
		except:
			language = None
		if language is None or language == 'Windows':
			try:
				language = languageHandler.getWindowsLanguage()[:2]
			except:
				language = 'en'
		return language

	def convertir_valor(self, valor):
		"""
		Convierte diferentes tipos de valores según las siguientes reglas:
		- Si el valor es la cadena 'None', lo convierte a None.
		- Si el valor es None, lo deja como None.
		- Si el valor es una cadena que representa un número, lo convierte a int.
		- Si el valor es un número, lo deja como está.
		
		Parámetros:
		valor (object): El valor que se quiere convertir.
		
		Retorna:
		object: El valor convertido según las reglas descritas.
		"""
		if valor == "None":
			return None
		elif valor is None:
			return None
		elif isinstance(valor, str) and valor.isdigit():
			return int(valor)
		elif isinstance(valor, int):
			return valor
		else:
			raise ValueError("El valor no es un tipo esperado.")
