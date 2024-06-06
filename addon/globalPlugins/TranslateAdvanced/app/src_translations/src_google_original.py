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

# Carga traducción
addonHandler.initTranslation()

class TranslatorGoogle:
	"""
	Clase para manejar la traducción de texto usando Google Translate.
	"""

	def __init__(self):
		"""
		Inicializa una instancia del traductor de Google Translate.
		"""
		self.agent = {'User-Agent': (
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; "
			".NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"
		)}
		self.html_entities = self._load_html_entities()

	def _load_html_entities(self):
		"""
		Carga todas las entidades HTML estándar y sus correspondientes caracteres.

		:return: Un diccionario con las entidades HTML como claves y los caracteres correspondientes como valores.
		"""
		return {
			'&Aacute;': 'Á', '&aacute;': 'á', '&Acirc;': 'Â', '&acirc;': 'â', '&acute;': '´',
			'&AElig;': 'Æ', '&aelig;': 'æ', '&Agrave;': 'À', '&agrave;': 'à', '&alefsym;': 'ℵ',
			'&Alpha;': 'Α', '&alpha;': 'α', '&amp;': '&', '&and;': '∧', '&ang;': '∠',
			'&Aring;': 'Å', '&aring;': 'å', '&asymp;': '≈', '&Atilde;': 'Ã', '&atilde;': 'ã',
			'&Auml;': 'Ä', '&auml;': 'ä', '&bdquo;': '„', '&Beta;': 'Β', '&beta;': 'β',
			'&brvbar;': '¦', '&bull;': '•', '&cap;': '∩', '&Ccedil;': 'Ç', '&ccedil;': 'ç',
			'&cedil;': '¸', '&cent;': '¢', '&Chi;': 'Χ', '&chi;': 'χ', '&circ;': 'ˆ',
			'&clubs;': '♣', '&cong;': '≅', '&copy;': '©', '&crarr;': '↵', '&cup;': '∪',
			'&curren;': '¤', '&dagger;': '†', '&Dagger;': '‡', '&darr;': '↓', '&dArr;': '⇓',
			'&deg;': '°', '&Delta;': 'Δ', '&delta;': 'δ', '&diams;': '♦', '&divide;': '÷',
			'&Eacute;': 'É', '&eacute;': 'é', '&Ecirc;': 'Ê', '&ecirc;': 'ê', '&Egrave;': 'È',
			'&egrave;': 'è', '&empty;': '∅', '&emsp;': ' ', '&ensp;': ' ', '&Epsilon;': 'Ε',
			'&epsilon;': 'ε', '&equiv;': '≡', '&Eta;': 'Η', '&eta;': 'η', '&ETH;': 'Ð',
			'&eth;': 'ð', '&Euml;': 'Ë', '&euml;': 'ë', '&euro;': '€', '&exist;': '∃',
			'&fnof;': 'ƒ', '&forall;': '∀', '&frac12;': '½', '&frac14;': '¼', '&frac34;': '¾',
			'&frasl;': '⁄', '&Gamma;': 'Γ', '&gamma;': 'γ', '&ge;': '≥', '&harr;': '↔',
			'&hArr;': '⇔', '&hearts;': '♥', '&hellip;': '…', '&Iacute;': 'Í', '&iacute;': 'í',
			'&Icirc;': 'Î', '&icirc;': 'î', '&iexcl;': '¡', '&Igrave;': 'Ì', '&igrave;': 'ì',
			'&image;': 'ℑ', '&infin;': '∞', '&int;': '∫', '&Iota;': 'Ι', '&iota;': 'ι',
			'&iquest;': '¿', '&isin;': '∈', '&Iuml;': 'Ï', '&iuml;': 'ï', '&Kappa;': 'Κ',
			'&kappa;': 'κ', '&Lambda;': 'Λ', '&lambda;': 'λ', '&lang;': '〈', '&laquo;': '«',
			'&larr;': '←', '&lArr;': '⇐', '&lceil;': '⌈', '&ldquo;': '“', '&le;': '≤',
			'&lfloor;': '⌊', '&lowast;': '∗', '&loz;': '◊', '&lrm;': '\u200e', '&lsaquo;': '‹',
			'&lsquo;': '‘', '&macr;': '¯', '&mdash;': '—', '&micro;': 'µ', '&middot;': '·',
			'&minus;': '−', '&Mu;': 'Μ', '&mu;': 'μ', '&nabla;': '∇', '&nbsp;': ' ',
			'&ndash;': '–', '&ne;': '≠', '&ni;': '∋', '&not;': '¬', '&notin;': '∉',
			'&nsub;': '⊄', '&Ntilde;': 'Ñ', '&ntilde;': 'ñ', '&Nu;': 'Ν', '&nu;': 'ν',
			'&Oacute;': 'Ó', '&oacute;': 'ó', '&Ocirc;': 'Ô', '&ocirc;': 'ô', '&OElig;': 'Œ',
			'&oelig;': 'œ', '&Ograve;': 'Ò', '&ograve;': 'ò', '&oline;': '‾', '&Omega;': 'Ω',
			'&omega;': 'ω', '&Omicron;': 'Ο', '&omicron;': 'ο', '&oplus;': '⊕', '&or;': '∨',
			'&ordf;': 'ª', '&ordm;': 'º', '&Oslash;': 'Ø', '&oslash;': 'ø', '&Otilde;': 'Õ',
			'&otilde;': 'õ', '&otimes;': '⊗', '&Ouml;': 'Ö', '&ouml;': 'ö', '&para;': '¶',
			'&part;': '∂', '&permil;': '‰', '&perp;': '⊥', '&Phi;': 'Φ', '&phi;': 'φ',
			'&Pi;': 'Π', '&pi;': 'π', '&piv;': 'ϖ', '&plusmn;': '±', '&pound;': '£',
			'&prime;': '′', '&Prime;': '″', '&prod;': '∏', '&prop;': '∝', '&Psi;': 'Ψ',
			'&psi;': 'ψ', '&radic;': '√', '&rang;': '〉', '&raquo;': '»', '&rarr;': '→',
			'&rArr;': '⇒', '&rceil;': '⌉', '&rdquo;': '”', '&real;': 'ℜ', '&reg;': '®',
			'&rfloor;': '⌋', '&Rho;': 'Ρ', '&rho;': 'ρ', '&rlm;': '\u200f', '&rsaquo;': '›',
			'&rsquo;': '’', '&sbquo;': '‚', '&Scaron;': 'Š', '&scaron;': 'š', '&sdot;': '⋅',
			'&sect;': '§', '&shy;': '\u00ad', '&Sigma;': 'Σ', '&sigma;': 'σ', '&sigmaf;': 'ς',
			'&sim;': '∼', '&spades;': '♠', '&sub;': '⊂', '&sube;': '⊆', '&sum;': '∑',
			'&sup;': '⊃', '&sup1;': '¹', '&sup2;': '²', '&sup3;': '³', '&supe;': '⊇',
			'&szlig;': 'ß', '&Tau;': 'Τ', '&tau;': 'τ', '&there4;': '∴', '&Theta;': 'Θ',
			'&theta;': 'θ', '&thetasym;': 'ϑ', '&thinsp;': ' ', '&THORN;': 'Þ', '&thorn;': 'þ',
			'&tilde;': '˜', '&times;': '×', '&trade;': '™', '&Uacute;': 'Ú', '&uacute;': 'ú',
			'&uarr;': '↑', '&uArr;': '⇑', '&Ucirc;': 'Û', '&ucirc;': 'û', '&Ugrave;': 'Ù',
			'&ugrave;': 'ù', '&uml;': '¨', '&upsih;': 'ϒ', '&Upsilon;': 'Υ', '&upsilon;': 'υ',
			'&Uuml;': 'Ü', '&uuml;': 'ü', '&weierp;': '℘', '&Xi;': 'Ξ', '&xi;': 'ξ',
			'&Yacute;': 'Ý', '&yacute;': 'ý', '&yen;': '¥', '&Yuml;': 'Ÿ', '&yuml;': 'ÿ',
			'&Zeta;': 'Ζ', '&zeta;': 'ζ', '&zwj;': '\u200d', '&zwnj;': '\u200c'
		}

	def unescape(self, text):
		"""
		Desescapa las entidades HTML en un texto dado.

		:param text: El texto a desescapar.
		:return: El texto desescapado.
		"""
		for entity, char in self.html_entities.items():
			text = text.replace(entity, char)
		return text

	def translate_google(self, to_translate, to_language="auto", from_language="auto"):
		"""
		Traduce un texto usando Google Translate.

		:param to_translate: El texto a traducir.
		:param to_language: El idioma al que traducir (por defecto "auto").
		:param from_language: El idioma desde el que traducir (por defecto "auto").
		:return: El texto traducido.
		"""
		base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
		to_translate = urllib.parse.quote(to_translate)
		link = base_link % (to_language, from_language, to_translate)
		request = urllib.request.Request(link, headers=self.agent)
		try:
			with urllib.request.urlopen(request) as response:
				raw_data = response.read()
		except Exception as e:
			msg = \
_("""Error en la traducción.

Error:

{}""").format(str(e))
			logHandler.log.error(msg)
			return to_translate  # Devolver el texto original en caso de error
		
		data = raw_data.decode("utf-8")
		expr = r'class="result-container">(.*?)<'
		re_result = re.findall(expr, data)
		
		if not re_result:
			result = ""
		else:
			result = self.unescape(re_result[0])
		
		return result
