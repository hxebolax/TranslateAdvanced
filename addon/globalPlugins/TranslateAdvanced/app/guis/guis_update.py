# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import languageHandler
# Carga Python
import wx

# Carga traducción
addonHandler.initTranslation()

class UpdateDialog(wx.Dialog):
	def __init__(self, frame, updates):
		"""
		Inicializa el cuadro de diálogo con la información de actualizaciones.

		:param frame: El padre del diálogo.
		:param updates: Diccionario con la información de nuevos idiomas y actualizaciones.
		"""
		super(UpdateDialog, self).__init__(None, title=_("Actualizaciones de Idiomas"))
		self.frame = frame
		self.frame.gestor_settings.IS_WinON = True

		self.updates = updates
		self.InitUI()
		self.SetSize((400, 300))
		self.SetTitle(_("Actualizaciones de Idiomas"))

	def InitUI(self):
		"""
		Inicializa la interfaz de usuario del diálogo.
		"""
		panel = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)

		new_langs = self.updates.get('nuevos', {})
		update_langs = self.updates.get('actualizaciones', {})

		new_langs_msg = ""
		update_langs_msg = ""

		if new_langs:
			new_langs_msg = _("Nuevos idiomas disponibles:") + "\n" + "\n".join(f"- {self.descripcion_lenguaje(lang)}" for lang in new_langs.keys())
		if update_langs:
			update_langs_msg = _("Idiomas con actualizaciones:") + "\n" + "\n".join(f"- {self.descripcion_lenguaje(lang)}" for lang in update_langs.keys())

		msg = "\n\n".join(filter(None, [new_langs_msg, update_langs_msg]))
		msg += "\n\n" + _("Si continúa con la instalación, cuando se termine el proceso NVDA se reiniciará.\n\n¿Desea continuar?")

		st = wx.StaticText(panel, label=msg)
		vbox.Add(st, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)

		hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.btn_install = wx.Button(panel, label=_('&Instalar'))
		self.btn_skip = wx.Button(panel, label=_('&Omitir'))
		
		self.btn_install.Bind(wx.EVT_BUTTON, self.OnInstall)
		self.btn_skip.Bind(wx.EVT_BUTTON, self.OnSkip)

		hbox.Add(self.btn_install, flag=wx.RIGHT, border=5)
		hbox.Add(self.btn_skip)

		vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
		panel.SetSizer(vbox)
		self.CenterOnScreen()		

	def descripcion_lenguaje(self, code):
		"""
		Devuelve la descripción del lenguaje basado en el código proporcionado.

		:param code: Código del lenguaje a describir.
		:return: Descripción del lenguaje.
		"""
		return languageHandler.getLanguageDescription(code)

	def OnInstall(self, event):
		"""
		Maneja el evento de clic en el botón "Instalar".
		"""
		self.frame.gestor_settings.IS_WinON = False
		self.EndModal(wx.ID_OK)

	def OnSkip(self, event):
		"""
		Maneja el evento de clic en el botón "Omitir".
		"""
		self.frame.gestor_settings.IS_WinON = False
		self.EndModal(wx.ID_CANCEL)
