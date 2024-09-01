# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
import gui
import ui
# Carga Python
import wx
# Carga personal
from ..utils.utils_nvda import mute

# Carga traducción
addonHandler.initTranslation()

class DialogHistory(wx.Dialog):
	"""
	Diálogo para mostrar y gestionar el historial de traducciones.
	"""
	def __init__(self, parent, frame):
		super(DialogHistory, self).__init__(parent, -1)

		self.frame = frame
		self.frame.gestor_settings.IS_WinON = True
		self.SetSize((800, 600))
		self.SetTitle(_("Historial de Traductor Avanzado"))

		self.historialOrigen = list(self.frame.gestor_settings.historialOrigen)
		self.historialDestino = list(self.frame.gestor_settings.historialDestino)
		self.historialFiltradoOrigen = []
		self.historialFiltradoDestino = []
		self.ordenInverso = False

		self.panelGeneral = wx.Panel(self, wx.ID_ANY)
		self.sizerGeneral = wx.BoxSizer(wx.VERTICAL)
		
		# Crear widgets
		self.crearWidgets()
		
		# Configurar sizer y layout
		self.panelGeneral.SetSizer(self.sizerGeneral)
		self.Layout()
		self.CenterOnScreen()
		
		# Configurar eventos
		self.configurarEventos()
		
		# Inicializar contenido
		self.inicializarContenido()
		
		# Agregar ayudas a los widgets
		self.agregar_ayudas()

	def crearWidgets(self):
		"""
		Crea los widgets de la ventana.
		"""
		self.labelBuscar = wx.StaticText(self.panelGeneral, wx.ID_ANY, _("&Buscar:"))
		self.sizerGeneral.Add(self.labelBuscar, 0, wx.EXPAND, 0)

		self.campoBuscar = wx.TextCtrl(self.panelGeneral, wx.ID_ANY)
		self.sizerGeneral.Add(self.campoBuscar, 0, wx.EXPAND, 0)

		self.labelListaOriginal = wx.StaticText(self.panelGeneral, wx.ID_ANY, _("&Lista texto original:"))
		self.sizerGeneral.Add(self.labelListaOriginal, 0, wx.EXPAND, 0)

		self.listboxOriginal = wx.ListBox(self.panelGeneral, wx.ID_ANY)
		self.sizerGeneral.Add(self.listboxOriginal, 1, wx.EXPAND, 0)

		self.labelTextoOrigen = wx.StaticText(self.panelGeneral, wx.ID_ANY, _("Texto &original:"))
		self.sizerGeneral.Add(self.labelTextoOrigen, 0, wx.EXPAND, 0)

		self.textoOrigen = wx.TextCtrl(self.panelGeneral, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
		self.sizerGeneral.Add(self.textoOrigen, 0, wx.EXPAND, 0)

		self.labelTextoTraducido = wx.StaticText(self.panelGeneral, wx.ID_ANY, _("Texto &traducido:"))
		self.sizerGeneral.Add(self.labelTextoTraducido, 0, wx.EXPAND, 0)

		self.textoTraducido = wx.TextCtrl(self.panelGeneral, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
		self.sizerGeneral.Add(self.textoTraducido, 0, wx.EXPAND, 0)

		self.sizerBotones = wx.BoxSizer(wx.HORIZONTAL)
		self.sizerGeneral.Add(self.sizerBotones, 0, wx.EXPAND, 0)

		self.buttonCopiar = wx.Button(self.panelGeneral, 101, _("&Copiar al portapapeles"))
		self.sizerBotones.Add(self.buttonCopiar, 2, wx.CENTRE, 0)

		self.buttonBorrar = wx.Button(self.panelGeneral, 102, _("Borrar &historial"))
		self.sizerBotones.Add(self.buttonBorrar, 2, wx.CENTRE, 0)

		self.buttonAlternar = wx.Button(self.panelGeneral, 103, _("&Alternar orden"))
		self.sizerBotones.Add(self.buttonAlternar, 2, wx.CENTRE, 0)

		self.buttonCerrar = wx.Button(self.panelGeneral, 104, _("Cerrar"))
		self.sizerBotones.Add(self.buttonCerrar, 2, wx.CENTRE, 0)

	def configurarEventos(self):
		"""
		Configuración de eventos para los widgets.
		"""
		self.Bind(wx.EVT_BUTTON, self.onBoton)
		self.listboxOriginal.Bind(wx.EVT_KEY_UP, self.onListboxKeyUp)
		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyVentanaDialogo)
		self.Bind(wx.EVT_CLOSE, self.onCerrar)
		self.campoBuscar.Bind(wx.EVT_TEXT, self.onBuscar)

	def inicializarContenido(self):
		"""
		Inicializa el contenido de la ventana.
		"""
		self.listboxOriginal.Clear()
		if self.ordenInverso:
			self.listboxOriginal.Append(self.historialDestino)
		else:
			self.listboxOriginal.Append(self.historialOrigen)
		if self.listboxOriginal.GetCount() > 0:
			self.listboxOriginal.SetSelection(0)
		self.listboxOriginal.SetFocus()
		self.actualizarEstado()

	def actualizarEstado(self):
		"""
		Actualiza el estado de los textos originales y traducidos según la selección.
		"""
		indice = self.listboxOriginal.GetSelection()
		if indice != wx.NOT_FOUND:
			if self.campoBuscar.GetValue():  # Usar los resultados filtrados si hay una búsqueda en curso
				if self.ordenInverso:
					if indice < len(self.historialFiltradoDestino) and indice < len(self.historialFiltradoOrigen):
						self.textoOrigen.SetValue(self.historialFiltradoDestino[indice])
						self.textoTraducido.SetValue(self.historialFiltradoOrigen[indice])
				else:
					if indice < len(self.historialFiltradoOrigen) and indice < len(self.historialFiltradoDestino):
						self.textoOrigen.SetValue(self.historialFiltradoOrigen[indice])
						self.textoTraducido.SetValue(self.historialFiltradoDestino[indice])
			else:  # Usar los resultados originales si no hay búsqueda
				if self.ordenInverso:
					if indice < len(self.historialDestino) and indice < len(self.historialOrigen):
						self.textoOrigen.SetValue(self.historialDestino[indice])
						self.textoTraducido.SetValue(self.historialOrigen[indice])
				else:
					if indice < len(self.historialOrigen) and indice < len(self.historialDestino):
						self.textoOrigen.SetValue(self.historialOrigen[indice])
						self.textoTraducido.SetValue(self.historialDestino[indice])
			self.textoOrigen.SetInsertionPoint(0)
			self.textoTraducido.SetInsertionPoint(0)

	def onBuscar(self, event):
		"""
		Maneja el evento de búsqueda y actualiza la lista y los campos de texto.
		"""
		busqueda = self.campoBuscar.GetValue().lower()
		if self.ordenInverso:
			filtrado_destino = [item for item in self.historialDestino if busqueda in item.lower()]
			filtrado_origen = [self.historialOrigen[self.historialDestino.index(item)] for item in filtrado_destino]
		else:
			filtrado_origen = [item for item in self.historialOrigen if busqueda in item.lower()]
			filtrado_destino = [self.historialDestino[self.historialOrigen.index(item)] for item in filtrado_origen]
		
		self.listboxOriginal.Clear()
		if filtrado_origen:
			self.listboxOriginal.Append(filtrado_destino if self.ordenInverso else filtrado_origen)
			self.listboxOriginal.SetSelection(0)
			self.historialFiltradoOrigen = filtrado_origen
			self.historialFiltradoDestino = filtrado_destino
		else:
			self.listboxOriginal.Append([_("No se encontró nada.")])
			self.listboxOriginal.SetSelection(0)
			self.textoOrigen.SetValue("")
			self.textoTraducido.SetValue("")
			self.historialFiltradoOrigen = []
			self.historialFiltradoDestino = []
		self.actualizarEstado()

	def onListboxKeyUp(self, event):
		"""
		Manejo del evento de tecla en la lista.
		"""
		tecla = event.GetKeyCode()
		if self.listboxOriginal.GetSelection() != wx.NOT_FOUND:
			if tecla == wx.WXK_F1:
				if self.listboxOriginal.GetString(self.listboxOriginal.GetSelection()) == _("No se encontró nada."): return
				msg = _("Se encuentra en la posición {} de {}").format(self.listboxOriginal.GetSelection() + 1, self.listboxOriginal.GetCount())
				ui.message(msg)
			else:
				self.actualizarEstado()
		event.Skip()

	def onBoton(self, event):
		"""
		Manejo del evento de botones.
		"""
		id = event.GetId()
		if id == 101:  # Copiar
			self.mostrarMenuCopiar()
		elif id == 102:  # Borrar
			self.borrarHistorial()
		elif id == 103:  # Alternar orden
			self.alternarOrden()
		elif id == 104:  # Cerrar
			self.onCerrar(None)

	def mostrarMenuCopiar(self):
		"""
		Muestra el menú para copiar al portapapeles.
		"""
		if self.listboxOriginal.GetString(self.listboxOriginal.GetSelection()) == _("No se encontró nada."):
			msg = _("No se encontró nada para poder ser copiado.")
			gui.messageBox(msg, _("Información"), wx.ICON_INFORMATION)
			return

		menu = wx.Menu()
		menu.Append(1, _("Copiar texto &original"))
		menu.Append(2, _("Copiar texto &traducido"))
		menu.Append(3, _("&Copiar origen y traducido"))
		menu.Bind(wx.EVT_MENU, self.onCopiarPortapapeles)
		self.buttonCopiar.PopupMenu(menu)

	def borrarHistorial(self):
		"""
		Borra el historial de traducciones.
		"""
		self.frame.gestor_settings.historialOrigen.clear()
		self.frame.gestor_settings.historialDestino.clear()
		self.onCerrar(None)

	def onCopiarPortapapeles(self, event):
		"""
		Maneja la copia al portapapeles según la opción seleccionada.
		"""
		id = event.GetId()
		if id == 1:  # Copiar texto origen
			msg = _("Copiado texto origen")
			self.frame.gestor_portapapeles.set_clipboard_text(self.textoTraducido.GetValue() if self.ordenInverso else self.textoOrigen.GetValue())
		elif id == 2:  # Copiar texto traducido
			msg = _("Copiado texto traducido")
			self.frame.gestor_portapapeles.set_clipboard_text(self.textoOrigen.GetValue() if self.ordenInverso else self.textoTraducido.GetValue())
		elif id == 3:  # Copiar origen y traducido
			msg = _("Copiado texto origen y traducido")
			self.frame.gestor_portapapeles.set_clipboard_text("{}\n{}".format(self.textoTraducido.GetValue() if self.ordenInverso else self.textoOrigen.GetValue(), self.textoOrigen.GetValue() if self.ordenInverso else self.textoTraducido.GetValue()))
		mute(0.3, msg)

	def alternarOrden(self):
		"""
		Alterna el orden de los campos origen y destino.
		"""
		self.ordenInverso = not self.ordenInverso
		if self.ordenInverso:
			self.labelListaOriginal.SetLabel(_("&Lista texto traducido:"))
			self.labelTextoOrigen.SetLabel(_("Texto &traducido:"))
			self.labelTextoTraducido.SetLabel(_("Texto &original:"))
		else:
			self.labelListaOriginal.SetLabel(_("&Lista texto original:"))
			self.labelTextoOrigen.SetLabel(_("Texto &original:"))
			self.labelTextoTraducido.SetLabel(_("Texto &traducido:"))
		
		# Actualizar ayudas según el nuevo orden
		self.actualizar_ayudas()

		self.campoBuscar.SetValue("")  # Limpiar el campo de búsqueda al alternar
		self.historialFiltradoOrigen = []
		self.historialFiltradoDestino = []
		self.inicializarContenido()  # Volver a cargar el contenido con el nuevo orden

	def actualizar_ayudas(self):
		"""
		Actualiza los textos de ayuda según el estado de orden inverso.
		"""
		if self.ordenInverso:
			self.SetHelp(self.textoOrigen, _("Muestra el texto traducido seleccionado. Este campo es de solo lectura."))
			self.SetHelp(self.textoTraducido, _("Muestra el texto original seleccionado. Este campo es de solo lectura."))
		else:
			self.SetHelp(self.textoOrigen, _("Muestra el texto original seleccionado. Este campo es de solo lectura."))
			self.SetHelp(self.textoTraducido, _("Muestra el texto traducido seleccionado. Este campo es de solo lectura."))

	def SetHelp(self, widget, text):
		"""
		Establece un mensaje de ayuda para un widget específico.

		:param widget: El widget al cual se le asignará el mensaje de ayuda.
		:param text: El texto del mensaje de ayuda que se mostrará cuando el widget reciba el enfoque y se presione Ctrl+H.
		"""
		self.frame.gestor_ayuda.agregar_ayuda(widget, text)

	def agregar_ayudas(self):
		"""
		Establece los textos de ayuda para todos los widgets de la interfaz.
		"""
		self.SetHelp(self.campoBuscar, _("Introduce el texto que deseas buscar en el historial."))
		self.SetHelp(self.listboxOriginal, _("Lista de textos originales o traducidos, dependiendo del orden seleccionado. Si pulsamos F1 nos dirá en la posición que nos encontramos de la lista."))
		self.actualizar_ayudas()  # Establece las ayudas iniciales según el estado por defecto
		self.SetHelp(self.buttonCopiar, _("Presiona este botón para copiar el texto seleccionado al portapapeles."))
		self.SetHelp(self.buttonBorrar, _("Presiona este botón para borrar todo el historial de traducciones."))
		self.SetHelp(self.buttonAlternar, _("Presiona este botón para alternar el orden entre texto original y texto traducido."))
		self.SetHelp(self.buttonCerrar, _("Presiona este botón para cerrar la ventana del historial."))

	def onKeyVentanaDialogo(self, event):
		"""
		Maneja el evento de teclas en la ventana de diálogo.
		"""
		if event.ControlDown() and event.GetKeyCode() == ord('H'):
			widget_focused = wx.Window.FindFocus()
			if widget_focused:
				if self.frame.gestor_ayuda.ayuda_existe(widget_focused):
					self.frame.gestor_ayuda.mostrar_ayuda(widget_focused)
				else:
					wx.MessageBox(_("No hay ayuda disponible para este elemento."), _("Ayuda"), wx.OK | wx.ICON_INFORMATION)
			else:
				wx.MessageBox(_("No hay un elemento enfocado."), _("Ayuda"), wx.OK | wx.ICON_INFORMATION)
		elif event.GetKeyCode() == wx.WXK_ESCAPE:  # Pulsamos ESC y cerramos la ventana
			self.onCerrar(None)
		else:
			event.Skip()

	def onCerrar(self, event):
		"""
		Maneja el cierre de la ventana.
		"""
		self.frame.gestor_settings.IS_WinON = False
		if self.IsModal():
			self.EndModal(wx.ID_OK)
		else:
			self.Close()
