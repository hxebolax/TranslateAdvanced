# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler

# Carga traducción
addonHandler.initTranslation()

class TraductorIdiomas:
	"""
	Clase para manejar los idiomas soportados por diferentes servicios de traducción.
	"""
	def __init__(self, frame):

		self.frame = frame
		self.idiomas_traductores = {
			"google": {
				"af": "Afrikaans",
				"sq": "Albanian",
				"am": "Amharic",
				"ar": "Arabic",
				"hy": "Armenian",
				"az": "Azerbaijani",
				"eu": "Basque",
				"be": "Belarusian",
				"bn": "Bengali",
				"bs": "Bosnian",
				"bg": "Bulgarian",
				"ca": "Catalan",
				"ceb": "Cebuano",
				"zh-CN": "Chinese (Simplified)",
				"zh-TW": "Chinese (Traditional)",
				"co": "Corsican",
				"hr": "Croatian",
				"cs": "Czech",
				"da": "Danish",
				"nl": "Dutch",
				"en": "English",
				"eo": "Esperanto",
				"et": "Estonian",
				"fi": "Finnish",
				"fr": "French",
				"fy": "Frisian",
				"gl": "Galician",
				"ka": "Georgian",
				"de": "German",
				"el": "Greek",
				"gu": "Gujarati",
				"ht": "Haitian Creole",
				"ha": "Hausa",
				"haw": "Hawaiian",
				"he": "Hebrew",
				"hi": "Hindi",
				"hmn": "Hmong",
				"hu": "Hungarian",
				"is": "Icelandic",
				"ig": "Igbo",
				"id": "Indonesian",
				"ga": "Irish",
				"it": "Italian",
				"ja": "Japanese",
				"jw": "Javanese",
				"kn": "Kannada",
				"kk": "Kazakh",
				"km": "Khmer",
				"rw": "Kinyarwanda",
				"ko": "Korean",
				"ku": "Kurdish (Kurmanji)",
				"ky": "Kyrgyz",
				"lo": "Lao",
				"la": "Latin",
				"lv": "Latvian",
				"lt": "Lithuanian",
				"lb": "Luxembourgish",
				"mk": "Macedonian",
				"mg": "Malagasy",
				"ms": "Malay",
				"ml": "Malayalam",
				"mt": "Maltese",
				"mi": "Maori",
				"mr": "Marathi",
				"mn": "Mongolian",
				"my": "Myanmar (Burmese)",
				"ne": "Nepali",
				"no": "Norwegian",
				"ny": "Nyanja (Chichewa)",
				"or": "Odia (Oriya)",
				"ps": "Pashto",
				"fa": "Persian",
				"pl": "Polish",
				"pt": "Portuguese",
				"pa": "Punjabi",
				"ro": "Romanian",
				"ru": "Russian",
				"sm": "Samoan",
				"gd": "Scots Gaelic",
				"sr": "Serbian",
				"st": "Sesotho",
				"sn": "Shona",
				"sd": "Sindhi",
				"si": "Sinhala",
				"sk": "Slovak",
				"sl": "Slovenian",
				"so": "Somali",
				"es": "Spanish",
				"su": "Sundanese",
				"sw": "Swahili",
				"sv": "Swedish",
				"tg": "Tajik",
				"ta": "Tamil",
				"tt": "Tatar",
				"te": "Telugu",
				"th": "Thai",
				"tr": "Turkish",
				"tk": "Turkmen",
				"uk": "Ukrainian",
				"ur": "Urdu",
				"ug": "Uyghur",
				"uz": "Uzbek",
				"vi": "Vietnamese",
				"cy": "Welsh",
				"xh": "Xhosa",
				"yi": "Yiddish",
				"yo": "Yoruba",
				"zu": "Zulu"
			},
			"deepl": {
				"bg": "Bulgarian",
				"cs": "Czech",
				"da": "Danish",
				"de": "German",
				"el": "Greek",
				"en": "English",
				"es": "Spanish",
				"et": "Estonian",
				"fi": "Finnish",
				"fr": "French",
				"hu": "Hungarian",
				"id": "Indonesian",
				"it": "Italian",
				"ja": "Japanese",
				"ko": "Korean",
				"lt": "Lithuanian",
				"lv": "Latvian",
				"nl": "Dutch",
				"pl": "Polish",
				"pt": "Portuguese",
				"ro": "Romanian",
				"ru": "Russian",
				"sk": "Slovak",
				"sl": "Slovenian",
				"sv": "Swedish",
				"tr": "Turkish",
				"uk": "Ukrainian",
				"zh": "Chinese (Simplified)"
			},
			"libretranslate": {
				"ar": "Arabic",
				"zh": "Chinese",
				"cs": "Czech",
				"da": "Danish",
				"nl": "Dutch",
				"en": "English",
				"fi": "Finnish",
				"fr": "French",
				"de": "German",
				"el": "Greek",
				"hi": "Hindi",
				"hu": "Hungarian",
				"id": "Indonesian",
				"ga": "Irish",
				"it": "Italian",
				"ja": "Japanese",
				"ko": "Korean",
				"fa": "Persian",
				"pl": "Polish",
				"pt": "Portuguese",
				"ru": "Russian",
				"es": "Spanish",
				"sv": "Swedish",
				"tr": "Turkish",
				"uk": "Ukrainian",
				"vi": "Vietnamese"
			},
			"microsoft": {
				"af": "Afrikaans",
				"ar": "Arabic",
				"bn": "Bangla",
				"bs": "Bosnian (Latin)",
				"bg": "Bulgarian",
				"yue": "Cantonese (Traditional)",
				"ca": "Catalan",
				"zh-Hans": "Chinese Simplified",
				"zh-Hant": "Chinese Traditional",
				"hr": "Croatian",
				"cs": "Czech",
				"da": "Danish",
				"nl": "Dutch",
				"en": "English",
				"et": "Estonian",
				"fj": "Fijian",
				"fil": "Filipino",
				"fi": "Finnish",
				"fr": "French",
				"de": "German",
				"el": "Greek",
				"ht": "Haitian Creole",
				"he": "Hebrew",
				"hi": "Hindi",
				"mww": "Hmong Daw",
				"hu": "Hungarian",
				"is": "Icelandic",
				"id": "Indonesian",
				"it": "Italian",
				"ja": "Japanese",
				"sw": "Kiswahili",
				"tlh-Latn": "Klingon (Latin)",
				"tlh-Piqd": "Klingon (pIqaD)",
				"ko": "Korean",
				"lv": "Latvian",
				"lt": "Lithuanian",
				"mg": "Malagasy",
				"ms": "Malay",
				"mt": "Maltese",
				"yua": "Mayan",
				"no": "Norwegian",
				"otq": "Querétaro Otomi",
				"fa": "Persian",
				"pl": "Polish",
				"pt": "Portuguese (Brazil)",
				"pt-PT": "Portuguese (Portugal)",
				"pa": "Punjabi",
				"ro": "Romanian",
				"ru": "Russian",
				"sm": "Samoan",
				"sr-Cyrl": "Serbian (Cyrillic)",
				"sr-Latn": "Serbian (Latin)",
				"sk": "Slovak",
				"sl": "Slovenian",
				"es": "Spanish",
				"sv": "Swedish",
				"ty": "Tahitian",
				"ta": "Tamil",
				"te": "Telugu",
				"th": "Thai",
				"to": "Tongan",
				"tr": "Turkish",
				"uk": "Ukrainian",
				"ur": "Urdu",
				"vi": "Vietnamese",
				"cy": "Welsh",
				"yua": "Yucatec Maya"
			}
		}

	def obtener_idiomas(self, traductor):
		"""
		Obtiene los idiomas soportados por el traductor especificado.

		:param traductor: Nombre del traductor (google, deepl, libretranslate, microsoft).
		:return: Diccionario de idiomas soportados por el traductor.
		"""
		return self.idiomas_traductores.get(traductor, {})

	def listar_idiomas(self, traductor):
		"""
		Lista los idiomas soportados por el traductor especificado.

		:param traductor: Nombre del traductor (google, deepl, libretranslate, microsoft).
		:return: Lista de idiomas soportados por el traductor.
		"""
		idiomas = self.obtener_idiomas(traductor)
		return [f"{codigo}: {nombre}" for codigo, nombre in idiomas.items()]

# Ejemplo de uso
#if __name__ == "__main__":
#	traductor_idiomas = TraductorIdiomas()

	# Imprimir los idiomas soportados por cada traductor
#	for traductor in ["google", "deepl", "libretranslate", "microsoft"]:
#		print(f"Idiomas soportados por {traductor.capitalize()}:")
#		for idioma in traductor_idiomas.listar_idiomas(traductor):
#			print(idioma)
		print()
