# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import gui
# Carga Python
import wx

# Carga traducción
addonHandler.initTranslation()

class DialogResults(wx.Dialog):
	"""
	Un diálogo que muestra los resultados en un TextBox de solo lectura.
	"""
	def __init__(self, parent, title, message):
		"""
		Inicializa el diálogo de resultados.

		:param parent: El panel padre.
		:param title: El título del diálogo.
		:param message: El mensaje a mostrar en el TextBox.
		"""
		super(DialogResults, self).__init__(parent, title=title, size=(800, 600))

		self.InitUI(message)

	def InitUI(self, message):
		"""
		Inicializa la interfaz de usuario del diálogo.

		:param message: El mensaje a mostrar en el TextBox.
		"""
		panel = wx.Panel(self)
		textBox = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
		textBox.SetValue(message)
		textBox.SetInsertionPoint(0)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(textBox, 1, wx.ALL | wx.EXPAND, 5)
		panel.SetSizer(sizer)
		
		dialogSizer = wx.BoxSizer(wx.VERTICAL)
		dialogSizer.Add(panel, 1, wx.EXPAND | wx.ALL, 5)
		self.SetSizer(dialogSizer)
		self.Layout()
		self.CenterOnScreen()
		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)

	def onKeyPress(self, event):
		"""
		Manejador de eventos para teclas presionadas en el diálogo.

		Args:
			event: El evento de teclado.
		"""
		if event.GetKeyCode() == wx.WXK_ESCAPE:
			self.Close()
		event.Skip()
