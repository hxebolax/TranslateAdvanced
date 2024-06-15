# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import languageHandler
import core
# Carga Python
import wx
import threading

# Carga traducción
addonHandler.initTranslation()

class ProgresoDescargaInstalacion(wx.Dialog):
	def __init__(self, frame, updates):
		"""
		Inicializa el cuadro de diálogo de progreso de descarga e instalación.

		:param frame: El padre del diálogo.
		:param updates: Diccionario con la información de nuevos idiomas y actualizaciones.
		"""
		super(ProgresoDescargaInstalacion, self).__init__(None, title=_("Progreso de Descarga e Instalación"))
		
		self.frame = frame
		self.frame.gestor_settings.IS_WinON = True
		self.updates = updates
		self.gestor_repositorios = self.frame.gestor_repositorio
		self.errores = []
		self.InitUI()
		self.SetSize((400, 200))
		self.SetTitle(_("Progreso de Descarga e Instalación"))

	def InitUI(self):
		"""
		Inicializa la interfaz de usuario del diálogo.
		"""
		panel = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		self.label = wx.StaticText(panel, label=_("Iniciando..."))
		vbox.Add(self.label, flag=wx.ALL | wx.EXPAND, border=10)
		
		self.progress = wx.Gauge(panel, range=100)
		vbox.Add(self.progress, flag=wx.ALL | wx.EXPAND, border=10)
		
		panel.SetSizer(vbox)
		self.CenterOnScreen()
		
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		
		# Inicia el proceso de descarga e instalación en un hilo separado
		threading.Thread(target=self.iniciar_descarga_instalacion, daemon=True).start()

	def descripcion_lenguaje(self, code):
		"""
		Devuelve la descripción del lenguaje basado en el código proporcionado.

		:param code: Código del lenguaje a describir.
		:return: Descripción del lenguaje.
		"""
		return languageHandler.getLanguageDescription(code)

	def iniciar_descarga_instalacion(self):
		"""
		Inicia el proceso de descarga e instalación de los idiomas.
		"""
		todos_idiomas = {**self.updates['nuevos'], **self.updates['actualizaciones']}
		total_idiomas = len(todos_idiomas)
		
		for idx, (idioma, version) in enumerate(todos_idiomas.items()):
			self.label.SetLabel(_("Descargando {}...").format(self.descripcion_lenguaje(idioma)))
			self.progress.SetValue(int((idx / total_idiomas) * 100))
			
			resultado_descarga = self.gestor_repositorios.descargar_zip(idioma, self.progress)
			if not resultado_descarga['success']:
				self.errores.append((self.descripcion_lenguaje(idioma), resultado_descarga['data']))
				continue
			
			self.label.SetLabel(_("Instalando {}...").format(self.descripcion_lenguaje(idioma)))
			resultado_descomprimir = self.gestor_repositorios.descomprimir_zip(idioma, widget_progreso=self.progress)
			if not resultado_descomprimir['success']:
				self.errores.append((self.descripcion_lenguaje(idioma), resultado_descomprimir['data']))
				continue
			
			# Actualizar el JSON local
			resultado_actualizar = self.gestor_repositorios.actualizar_idioma_local(idioma, version)
			if not resultado_actualizar['success']:
				self.errores.append((self.descripcion_lenguaje(idioma), resultado_actualizar['data']))
				continue

		self.progress.SetValue(100)
		self.mostrar_resultado()

	def mostrar_resultado(self):
		"""
		Muestra el resultado final del proceso, indicando si hubo errores.
		"""
		total_idiomas = len({**self.updates['nuevos'], **self.updates['actualizaciones']})
		if self.errores:
			if len(self.errores) >=total_idiomas:
				mensajes_error = "\n".join([_("Error en {}: {}").format(self.descripcion_lenguaje(idioma), error) for idioma, error in self.errores])
				wx.MessageBox(
					_("El proceso ha finalizado con errores en los siguientes idiomas:\n\n{}").format(mensajes_error) + 
					_("\n\nNVDA no se reiniciará, pulse Ctrl + C para copiar el contenido de este dialogo y podérselo enviar al autor del complemento."),
					_("Errores"),
					wx.OK | wx.ICON_ERROR
				)
				self.frame.gestor_settings.IS_WinON = False
				self.EndModal(wx.ID_OK)
				return
			mensajes_error = "\n".join([_("Error en {}: {}").format(self.descripcion_lenguaje(idioma), error) for idioma, error in self.errores])
			wx.MessageBox(_("El proceso ha finalizado con errores en los siguientes idiomas:\n\n{}").format(mensajes_error) + _("\n\nNVDA se reiniciará cuando pulse aceptar."), _("Errores"), wx.OK | wx.ICON_ERROR)
		else:
			wx.MessageBox(_("Todos los idiomas se han actualizado correctamente.") + _("\n\nNVDA se reiniciará cuando pulse aceptar."), _("Éxito"), wx.OK | wx.ICON_INFORMATION)
		self.frame.gestor_settings.IS_WinON = False
		self.EndModal(wx.ID_OK)
		core.restart()

	def OnClose(self, event):
		"""
		Maneja el evento de cerrar el diálogo.
		"""
		return
