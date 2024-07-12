# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import wx
import json

# Carga traducción
addonHandler.initTranslation()

class AyudaDialogo(wx.Dialog):
	"""
	Clase que representa el diálogo de ayuda.
	"""
	def __init__(self, parent, titulo, mensaje):
		"""
		Inicializa el diálogo de ayuda.

		:param parent: El widget padre del diálogo.
		:param titulo: El título del diálogo.
		:param mensaje: El mensaje de ayuda a mostrar.
		"""
		super(AyudaDialogo, self).__init__(parent, title=titulo, size=(300, 200))
		panel = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)

		txt = wx.StaticText(panel, label=mensaje)
		vbox.Add(txt, flag=wx.ALL | wx.EXPAND, border=10)

		okButton = wx.Button(panel, label=_('&Aceptar'))
		okButton.Bind(wx.EVT_BUTTON, self.onClose)
		vbox.Add(okButton, flag=wx.ALL | wx.CENTER, border=10)

		panel.SetSizer(vbox)
		self.CenterOnScreen()

	def onClose(self, event):
		"""
		Maneja el evento de cierre del diálogo.

		:param event: El evento de cierre.
		"""
		self.Destroy()

class AdministradorAyuda:
	"""
	Clase que administra las ayudas de los widgets.
	"""
	def __init__(self):
		"""
		Inicializa el administrador de ayudas.
		"""
		self.ayudas = {}

	def agregar_ayuda(self, widget, mensaje_ayuda):
		"""
		Agrega un mensaje de ayuda para un widget.

		:param widget: El widget al que se le agregará la ayuda.
		:param mensaje_ayuda: El mensaje de ayuda.
		"""
		self.ayudas[widget] = mensaje_ayuda
		widget.Bind(wx.EVT_SET_FOCUS, self.onFocus)

	def mostrar_ayuda(self, widget):
		"""
		Muestra el diálogo de ayuda para el widget dado.

		:param widget: El widget para el cual se mostrará la ayuda.
		"""
		mensaje_ayuda = self.ayudas.get(widget, _("No hay ayuda disponible para este widget."))
		dialogo = AyudaDialogo(widget, _("Ayuda"), mensaje_ayuda)
		dialogo.ShowModal()

	def onFocus(self, event):
		"""
		Maneja el evento de enfoque del widget y muestra la ayuda si se presiona F1.

		:param event: El evento de enfoque.
		"""
		widget = event.GetEventObject()
		widget.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
		event.Skip()

	def onKeyPress(self, event):
		"""
		Maneja el evento de presión de teclas.

		:param event: El evento de presión de tecla.
		"""
		if event.ControlDown() and event.GetKeyCode() == ord('H'):
			widget = event.GetEventObject()
			self.mostrar_ayuda(widget)
		else:
			event.Skip()

	def ayuda_existe(self, widget):
		"""
		Verifica si existe una ayuda para un widget.

		:param widget: widget.
		:return: True si existe una ayuda, False en caso contrario.
		"""
		return widget in self.ayudas
