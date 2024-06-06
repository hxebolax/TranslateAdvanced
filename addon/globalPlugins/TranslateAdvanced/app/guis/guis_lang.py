# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import languageHandler
import gui
# Carga Python
import wx
# Carga personal
from ..managers.managers_dict import LanguageDictionary

# Carga traducción
addonHandler.initTranslation()

class DialogoLang(wx.Dialog):
	"""
	Diálogo para seleccionar el idioma de origen o destino, o cambiar el módulo de traducción.
	"""
	def __init__(self, parent, frame, option):
		"""
		Inicializa una instancia del diálogo de selección de idioma.

		:param parent: Ventana padre del diálogo.
		:param frame: Marco principal de la aplicación.
		:param option: Opción que determina el tipo de selección (origen, destino, cambiar traductor).
		"""
		super(DialogoLang, self).__init__(parent)

		self.frame = frame
		self.frame.gestor_settings.IS_WinON = True
		self.id = self.frame.gestor_settings.choiceOnline
		if self.id in [0, 1, 2, 3]: # Para Google
			self.datos = LanguageDictionary(self.frame.gestor_lang.obtener_idiomas("google"))
			self.idiomas_code = self.datos.get_keys()
			self.idiomas_name = self.datos.get_values()
			self.destino = self.frame.gestor_settings.choiceLangDestino_google
			self.name_traductor = "Google"
		elif self.id in [4, 5]: # Para DeepL
			self.datos = LanguageDictionary(self.frame.gestor_lang.obtener_idiomas("deepl"))
			self.idiomas_code = self.datos.get_keys()
			self.idiomas_name = self.datos.get_values()
			self.destino = self.frame.gestor_settings.choiceLangDestino_deepl
			self.name_traductor = "DeepL"
		elif self.id in [6]: # Para LibreTranslate
			self.datos = LanguageDictionary(self.frame.gestor_lang.obtener_idiomas("libretranslate"))
			self.idiomas_code = self.datos.get_keys()
			self.idiomas_name = self.datos.get_values()
			self.destino = self.frame.gestor_settings.choiceLangDestino_libretranslate
			self.name_traductor = "LibreTranslate"
		elif self.id in [7]: # Para Microsoft
			self.datos = LanguageDictionary(self.frame.gestor_lang.obtener_idiomas("microsoft"))
			self.idiomas_code = self.datos.get_keys()
			self.idiomas_name = self.datos.get_values()
			self.origen = self.frame.gestor_settings.choiceLangOrigen
			self.destino = self.frame.gestor_settings.choiceLangDestino_microsoft
			self.name_traductor = "Microsoft"

		self.option = option
		self.SetSize((300, 250))
		if self.option == 0: # Idiomas origen
			self.SetTitle(_("Seleccione un idioma de origen para el traductor de Microsoft"))
			self.idioma_config = self.origen
		elif self.option == 1: # Idiomas destino
			self.SetTitle(_("Seleccione un idioma de destino para el traductor {}").format(self.name_traductor))
			self.idioma_config = self.destino
		elif self.option == 2: # Cambiar traductor
			self.SetTitle(_("Elija un módulo de traducción"))

		self.CenterOnScreen()

		self.listBox = wx.ListBox(self, style=wx.LB_SINGLE)

		# Configura el layout.
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.listBox, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
		self.SetSizer(sizer)

		# Maneja el cierre con la tecla Escape y otras teclas.
		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)
		self.inicio()

	def descripcion_lenguaje(self, code):
		"""
		Devuelve la descripción del lenguaje basado en el código proporcionado.

		:param code: Código del lenguaje a describir.
		:return: Descripción del lenguaje.
		"""
		data = languageHandler.getLanguageDescription(code)
		if data is None:
			return self.idiomas_name[self.datos.get_index_by_key_or_value(code)]
		else:
			return data

	def inicio(self):
		"""
		Inicializa la lista de opciones en el ListBox según la opción seleccionada.
		"""
		if self.option in [0, 1]: # origen y destino
			self.listBox.Append([f"{self.descripcion_lenguaje(i)} - {i}" for i in self.idiomas_code])
			self.listBox.SetFocus()
			self.listBox.SetSelection(self.datos.get_index_by_key_or_value(self.idioma_config))
		elif self.option in [2]: # cambiar traductor
			self.listBox.Append(self.frame.gestor_settings.servers_names)
			self.listBox.SetFocus()
			self.listBox.SetSelection(self.frame.gestor_settings.choiceOnline)

	def ejecutarSeleccion(self):
		"""
		Ejecuta la acción seleccionada en el ListBox.
		"""
		if self.option == 0: # Idiomas origen
			self.frame.gestor_settings.choiceLangOrigen = self.idiomas_code[self.listBox.GetSelection()]
		elif self.option == 1: # Idiomas destino
			code = self.idiomas_code[self.listBox.GetSelection()]
			if self.id in [0, 1, 2, 3]: # Para Google
				self.frame.gestor_settings.choiceLangDestino_google = code
			elif self.id in [4, 5]: # Para DeepL
				self.frame.gestor_settings.choiceLangDestino_deepl = code
			elif self.id in [6]: # Para LibreTranslate
				self.frame.gestor_settings.choiceLangDestino_libretranslate = code
			elif self.id in [7]: # Para Microsoft
				self.frame.gestor_settings.choiceLangDestino_microsoft = code
		elif self.option == 2: # cambiar traductor
			self.frame.gestor_settings.choiceOnline = self.listBox.GetSelection()

		self.frame.gestor_settings.IS_WinON = False
		self.frame.gestor_settings.guardaConfiguracion()
		self.Close()

	def onKeyPress(self, event):
		"""
		Manejador de eventos para teclas presionadas en el diálogo.

		:param event: El evento de teclado.
		"""
		if event.GetKeyCode() == wx.WXK_RETURN:
			self.ejecutarSeleccion()
		elif event.GetKeyCode() == wx.WXK_ESCAPE:
			self.frame.gestor_settings.IS_WinON = False
			self.Close()
		event.Skip()
