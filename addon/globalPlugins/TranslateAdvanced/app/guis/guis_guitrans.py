# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
#
# Carga NVDA
import addonHandler
import languageHandler
import gui
import ui
import api
import core
import watchdog
from keyboardHandler import KeyboardInputGesture
# Carga Python
import wx
import time
# Carga personal
from ..managers.managers_dict import LanguageDictionary
from ..src_translations.src_detect import DetectorDeIdioma
from .guis_progress import ProgressDialog
from .guis_player import ReproductorWav
from ..utils.utils_network import check_internet_connection

# Carga traducción
addonHandler.initTranslation()

class TranslateDialog(wx.Dialog):
	def __init__(self, parent, frame, texto_a_traducir=None):
		super(TranslateDialog, self).__init__(parent, title=_("Interfaz de traducción"), size=(800, 600))

		self.frame = frame
		self.frame.gestor_ayuda.ayudas = {}
		self.frame.gestor_settings.IS_WinON = True
		self.texto_a_traducir = texto_a_traducir
		self.idioma_origen_defecto = self.frame.gestor_settings.guiLang_origen
		self.idioma_destino_defecto = self.frame.gestor_settings.guiLang_destino
		self.texto_traducido_anterior = "" # Variable para almacenar el texto traducido anteriormente
		self.texto_destino_anterior = ""  # Variable para almacenar el texto traducido previamente en destino
		self.audio_obtenido = None  # Variable para almacenar el audio obtenido previamente
		self.lang_anterior = ""

		# Variables para datos de lenguaje
		self.datos = LanguageDictionary(self.frame.gestor_lang.obtener_idiomas("google"))
		self.idiomas_code = self.datos.get_keys()
		self.idiomas_name = self.datos.get_values()

		# Variables varias
		self.num_caracteres = 0
		self.InitUI()
		self.configurarEventos()
		self.inicio()

	def InitUI(self):
		"""
		Inicializa la interfaz de usuario.
		"""
		panel = wx.Panel(self)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		label_origen = wx.StaticText(panel, label=_("Texto origen (Alt+1):"))
		hbox1.Add(label_origen, flag=wx.RIGHT, border=8)
		self.texto_origen = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
		hbox1.Add(self.texto_origen, proportion=1, flag=wx.EXPAND)
		vbox.Add(hbox1, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		label_destino = wx.StaticText(panel, label=_("Texto destino (Alt+2):"))
		hbox2.Add(label_destino, flag=wx.RIGHT, border=8)
		self.texto_destino = wx.TextCtrl(panel, style=wx.TE_READONLY | wx.TE_MULTILINE)
		hbox2.Add(self.texto_destino, proportion=1, flag=wx.EXPAND)
		vbox.Add(hbox2, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		label_idioma_origen = wx.StaticText(panel, label=_("Idioma origen (Alt+3):"))
		hbox3.Add(label_idioma_origen, flag=wx.RIGHT, border=8)
		self.choice_origen = wx.Choice(panel, choices=[_("Auto Detectar - auto")] + [f"{self.descripcion_lenguaje(i) if self.descripcion_lenguaje(i) else self.idiomas_name[self.idiomas_code.index(i)]} - {i}" for i in self.idiomas_code])
		self.choice_origen.SetStringSelection(_("Auto Detectar - auto"))
		hbox3.Add(self.choice_origen, flag=wx.RIGHT, border=10)
		label_idioma_destino = wx.StaticText(panel, label=_("Idioma destino (Alt+4):"))
		hbox3.Add(label_idioma_destino, flag=wx.RIGHT, border=8)
		self.choice_destino = wx.Choice(panel, choices=[f"{self.descripcion_lenguaje(i) if self.descripcion_lenguaje(i) else self.idiomas_name[self.idiomas_code.index(i)]} - {i}" for i in self.idiomas_code])
		hbox3.Add(self.choice_destino, flag=wx.RIGHT, border=10)
		vbox.Add(hbox3, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		self.boton_traducir = wx.Button(panel, label=_('&Traducir'))
		hbox4.Add(self.boton_traducir, flag=wx.RIGHT, border=10)
		self.boton_escuchar = wx.Button(panel, label=_('&Escuchar'))
		hbox4.Add(self.boton_escuchar, flag=wx.RIGHT, border=10)
		self.boton_intercambiar = wx.Button(panel, label=_('&Intercambiar'))
		hbox4.Add(self.boton_intercambiar, flag=wx.RIGHT, border=10)
		self.boton_limpiar = wx.Button(panel, label=_('&Limpiar'))
		hbox4.Add(self.boton_limpiar, flag=wx.RIGHT, border=10)
		self.boton_pegar = wx.Button(panel, label=_('&Pegar al foco'))
		hbox4.Add(self.boton_pegar, flag=wx.RIGHT, border=10)
		self.boton_cerrar = wx.Button(panel, label=_('&Cerrar'))
		hbox4.Add(self.boton_cerrar, flag=wx.RIGHT, border=10)
		vbox.Add(hbox4, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		label_contador = wx.StaticText(panel, label=_('Caracteres (Alt+5):'))
		hbox5.Add(label_contador, flag=wx.RIGHT, border=8)
		self.contador_caracteres = wx.TextCtrl(panel, style=wx.TE_READONLY | wx.TE_MULTILINE)
		hbox5.Add(self.contador_caracteres, proportion=1, flag=wx.EXPAND)
		vbox.Add(hbox5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

		panel.SetSizer(vbox)

		self.CenterOnScreen()

		# Crear IDs para los aceleradores
		self.accel_id_texto_origen = wx.NewIdRef()
		self.accel_id_texto_destino = wx.NewIdRef()
		self.accel_id_idioma_origen = wx.NewIdRef()
		self.accel_id_idioma_destino = wx.NewIdRef()
		self.accel_id_contador_caracteres = wx.NewIdRef()

		# Configuración de aceleradores
		accel_tbl = wx.AcceleratorTable([
			(wx.ACCEL_ALT, ord('1'), self.accel_id_texto_origen),
			(wx.ACCEL_ALT, ord('2'), self.accel_id_texto_destino),
			(wx.ACCEL_ALT, ord('3'), self.accel_id_idioma_origen),
			(wx.ACCEL_ALT, ord('4'), self.accel_id_idioma_destino),
			(wx.ACCEL_ALT, ord('5'), self.accel_id_contador_caracteres),
		])
		self.SetAcceleratorTable(accel_tbl)

		# Asignar los IDs al método de enfoque
		self.Bind(wx.EVT_MENU, self.enfocar_control, id=self.accel_id_texto_origen)
		self.Bind(wx.EVT_MENU, self.enfocar_control, id=self.accel_id_texto_destino)
		self.Bind(wx.EVT_MENU, self.enfocar_control, id=self.accel_id_idioma_origen)
		self.Bind(wx.EVT_MENU, self.enfocar_control, id=self.accel_id_idioma_destino)
		self.Bind(wx.EVT_MENU, self.enfocar_control, id=self.accel_id_contador_caracteres)

		self.agregar_ayudas()

	def configurarEventos(self):
		"""
		Configuración de eventos para los widgets.
		"""
		self.choice_origen.Bind(wx.EVT_CHOICE, self.actualizar_idiomas_destino)
		self.choice_destino.Bind(wx.EVT_CHOICE, self.actualizar_idiomas_origen)
		self.boton_traducir.Bind(wx.EVT_BUTTON, self.traducir)
		self.boton_escuchar.Bind(wx.EVT_BUTTON, self.escuchar_traduccion)
		self.boton_intercambiar.Bind(wx.EVT_BUTTON, self.intercambiar_idiomas)
		self.boton_limpiar.Bind(wx.EVT_BUTTON, self.limpiar)
		self.boton_pegar.Bind(wx.EVT_BUTTON, self.pegar)
		self.boton_cerrar.Bind(wx.EVT_BUTTON, self.cerrar_dialogo)
		self.texto_origen.Bind(wx.EVT_TEXT, self.actualizar_contador_caracteres)
		# Bind para detectar la presión de teclas
		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)
		self.Bind(wx.EVT_CLOSE, self.cerrar_dialogo)

	def inicio(self):
		if self.idioma_origen_defecto == "auto":
			self.choice_origen.SetSelection(0)
		else:
			self.choice_origen.SetSelection(self.idiomas_code.index(self.idioma_origen_defecto) + 1)
		self.choice_destino.SetSelection(self.idiomas_code.index(self.idioma_destino_defecto))
		if self.texto_a_traducir:
			self.texto_origen.SetValue(self.texto_a_traducir)
		self.actualizar_contador_caracteres(None)
		self.actualizar_idiomas_origen(None)
		self.actualizar_idiomas_destino(None)

	def descripcion_lenguaje(self, code):
		"""
		Devuelve la descripción del lenguaje basado en el código proporcionado.

		:param code: Código del lenguaje a describir.
		:return: Descripción del lenguaje.
		"""
		return languageHandler.getLanguageDescription(code)

	def enfocar_control(self, event):
		"""
		Enfoca el control correspondiente en función del ID del evento.
		"""
		event_id = event.GetId()
		if event_id == self.accel_id_texto_origen:
			self.texto_origen.SetFocus()
		elif event_id == self.accel_id_texto_destino:
			self.texto_destino.SetFocus()
		elif event_id == self.accel_id_idioma_origen:
			self.choice_origen.SetFocus()
		elif event_id == self.accel_id_idioma_destino:
			self.choice_destino.SetFocus()
		elif event_id == self.accel_id_contador_caracteres:
			self.contador_caracteres.SetFocus()

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
		self.SetHelp(self.texto_origen, _("Introduce el texto que deseas traducir. Puedes escribir o pegar el texto aquí."))
		self.SetHelp(self.texto_destino, _("El resultado de la traducción se mostrará aquí. Este campo es de solo lectura."))
		self.SetHelp(self.choice_origen, _("Selecciona el idioma de origen para la traducción."))
		self.SetHelp(self.choice_destino, _("Selecciona el idioma de destino para la traducción."))
		self.SetHelp(self.boton_traducir, _("Presiona este botón para traducir el texto de origen al idioma de destino."))
		self.SetHelp(self.boton_escuchar, _("Presiona este botón para escuchar la traducción."))
		self.SetHelp(self.boton_intercambiar, _("Intercambia los idiomas de origen y destino."))
		self.SetHelp(self.boton_limpiar, _("Limpia los campos de texto de origen y destino."))
		self.SetHelp(self.boton_pegar, _("Pega al foco lo que haya en el cuadro de texto destino. Se pegara en la ventana que tengamos detrás de esta, siempre y cuando dicha ventana sea cuadro de texto que permita pegar texto en ella. Podemos usar también F3."))
		self.SetHelp(self.boton_cerrar, _("Cierra la ventana de traducción."))
		self.SetHelp(self.contador_caracteres, _("Muestra el número de caracteres en el campo de texto de origen."))

	def actualizar_contador_caracteres(self, event):
		"""
		Actualiza el contador de caracteres cuando el texto de origen cambia.

		:param event: Evento de cambio de texto.
		"""
		self.num_caracteres = len(self.texto_origen.GetValue())
		if self.num_caracteres == 0:
			self.contador_caracteres.SetValue(f'0')
		else:
			self.contador_caracteres.SetValue(f'{self.num_caracteres}')

	def actualizar_idiomas_destino(self, event):
		"""
		Actualiza los idiomas en el Choice de destino para excluir el seleccionado en el Choice de origen.
		"""
		idioma_origen = self.choice_origen.GetStringSelection().split(' - ')[-1]
		seleccion_actual = self.choice_destino.GetStringSelection()

		idiomas_destino = [f"{self.descripcion_lenguaje(i) if self.descripcion_lenguaje(i) else self.idiomas_name[self.idiomas_code.index(i)]} - {i}" for i in self.idiomas_code if i != idioma_origen]
		self.choice_destino.Clear()
		self.choice_destino.AppendItems(idiomas_destino)
		
		if seleccion_actual and seleccion_actual.split(' - ')[-1] != idioma_origen:
			self.choice_destino.SetStringSelection(seleccion_actual)
		else:
			self.choice_destino.SetSelection(0)

	def actualizar_idiomas_origen(self, event):
		"""
		Actualiza los idiomas en el Choice de origen para excluir el seleccionado en el Choice de destino, excepto "Auto Detectar".
		"""
		idioma_destino = self.choice_destino.GetStringSelection().split(' - ')[-1]
		seleccion_actual = self.choice_origen.GetStringSelection()

		idiomas_origen = [_("Auto Detectar - auto")] + [f"{self.descripcion_lenguaje(i) if self.descripcion_lenguaje(i) else self.idiomas_name[self.idiomas_code.index(i)]} - {i}" for i in self.idiomas_code if i != idioma_destino]
		self.choice_origen.Clear()
		self.choice_origen.AppendItems(idiomas_origen)

		if seleccion_actual and seleccion_actual.split(' - ')[-1] != idioma_destino:
			self.choice_origen.SetStringSelection(seleccion_actual)
		else:
			self.choice_origen.SetSelection(0)

	def traducir(self, event):
		"""
		Maneja el evento de traducción del texto.

		:param event: Evento de botón.
		"""
		if not check_internet_connection():
			msg = \
_("""No se a encontrado conexión a internet.

Si esta conectado por Wifi puede que NVDA iniciara antes que se conectara.

Si esta conectado por cable compruebe su conexión y asegúrese que todo esta correcto.

Espere unos segundos.""")
			gui.messageBox(msg, _("Información"), wx.ICON_INFORMATION)
			return
		if not self.texto_origen.GetValue().strip():
			msg = \
_("""El cuadro de texto de origen está vacío. Por favor, escribe algo.""")
			gui.messageBox(msg, _("Advertencia"), wx.ICON_WARNING)
			return

		if self.texto_origen.GetValue().strip() == self.texto_traducido_anterior.strip() and self.choice_destino.GetStringSelection().split(' - ')[-1] == self.lang_anterior:
			msg = \
_("""El texto no ha cambiado. No es necesario realizar una nueva traducción.""")
			gui.messageBox(msg, _("Información"), wx.ICON_INFORMATION)
			return

		result = DetectorDeIdioma().detectar_idioma(self.texto_origen.GetValue())
		if result["success"]:
			if result["data"] == self.choice_destino.GetStringSelection().split(' - ')[-1]:
				msg = \
_("""Se a detectado que el texto de origen es igual que el idioma destino al cual quiere traducirse.

Cambie el idioma destino de traducción si desea continuar.""")
				gui.messageBox(msg, _("Advertencia"), wx.ICON_WARNING)
				return
		else:
			msg = \
_("""No a sido posible detectar el idioma del texto origen.

Se va a intentar traducir, pero no se asegura el éxito de la operación.""")
			gui.messageBox(msg, _("Advertencia"), wx.ICON_WARNING)


		self.progress_dialog = ProgressDialog(self.frame, self.texto_origen.GetValue(), interfaz=True, secundary_frame=self)
		result = self.progress_dialog.ShowModal()
		if result == wx.ID_OK:
			if self.progress_dialog.completed:
				if not self.progress_dialog.traduccion_resultado or self.texto_origen.GetValue() == self.progress_dialog.traduccion_resultado:
					gui.messageBox(_("No se ha podido obtener la traducción de lo seleccionado."), _("Información"), wx.ICON_INFORMATION)
					return
				self.texto_destino.Clear()
				self.texto_destino.SetValue(self.progress_dialog.traduccion_resultado)
				self.texto_destino.SetFocus()
				self.texto_traducido_anterior = self.texto_origen.GetValue().strip()
				self.audio_obtenido = None  # Variable para almacenar el audio obtenido previamente
				self.texto_destino_anterior = ""  # Variable para almacenar el texto traducido previamente en destino
				self.lang_anterior = self.choice_destino.GetStringSelection().split(' - ')[-1]
			else:
				gui.messageBox(_("Hubo un error en la traducción:\n\n") + self.progress_dialog.error, _("Error"), wx.OK | wx.ICON_ERROR)
		elif result == wx.ID_CANCEL:
			gui.messageBox(_("La traducción fue cancelada por el usuario."), _("Cancelado"), wx.OK | wx.ICON_INFORMATION)

	def escuchar_traduccion(self, event):
		"""
		Maneja el evento de escuchar la traducción.

		:param event: Evento de botón.
		"""
		if not check_internet_connection():
			msg = \
_("""No se ha encontrado conexión a internet.

Si está conectado por Wifi, puede que NVDA iniciara antes que se conectara.

Si está conectado por cable, compruebe su conexión y asegúrese de que todo esté correcto.

Espere unos segundos.""")
			gui.messageBox(msg, _("Información"), wx.ICON_INFORMATION)
			return

		# Verificar si el cuadro de texto destino está vacío
		if not self.texto_destino.GetValue().strip():
			msg = \
_("""El cuadro de texto destino está vacío. Por favor, traduce algo.""")
			gui.messageBox(msg, _("Advertencia"), wx.ICON_WARNING)
			return

		# Si el texto destino no ha cambiado y ya se ha obtenido el audio previamente
		if self.texto_destino.GetValue().strip() == self.texto_destino_anterior and self.audio_obtenido is not None:
			# Reutilizar el audio obtenido previamente
			dialogo = ReproductorWav(self, self.frame, self.texto_destino.GetValue(), self.audio_obtenido)
			dialogo.ShowModal()
			dialogo.Destroy()
			return

		# Obtener el nuevo audio si el texto destino ha cambiado
		self.progress_dialog = ProgressDialog(self.frame, self.texto_destino.GetValue(), interfaz=True, secundary_frame=self, tts=True, lang_tts=self.choice_destino.GetStringSelection().split(' - ')[-1])
		result = self.progress_dialog.ShowModal()
		if result == wx.ID_OK:
			if self.progress_dialog.completed:
				if not self.progress_dialog.traduccion_resultado:
					msg = \
_("""No se ha podido obtener el audio.

Inténtelo más tarde.""")
					gui.messageBox(msg, _("Información"), wx.ICON_INFORMATION)
					return
				# Guardar el audio obtenido y el texto destino actual
				self.audio_obtenido = self.progress_dialog.traduccion_resultado
				self.texto_destino_anterior = self.texto_destino.GetValue().strip()
				dialogo = ReproductorWav(self, self.frame, self.texto_destino.GetValue(), self.audio_obtenido)
				dialogo.ShowModal()
				dialogo.Destroy()
			else:
				gui.messageBox(_("Hubo un error en la obtención del audio:\n\n") + self.progress_dialog.error, _("Error"), wx.ICON_ERROR)
		elif result == wx.ID_CANCEL:
			gui.messageBox(_("La obtención del audio fue cancelada por el usuario."), _("Cancelado"), wx.ICON_INFORMATION)

	def intercambiar_idiomas(self, event):
		"""
		Intercambia los idiomas seleccionados entre el Choice de origen y el Choice de destino.
		"""
		if self.choice_origen.GetStringSelection().split(' - ')[-1] == "auto":
			msg = \
_("""No se puede intercambiar idiomas cuando el idioma de origen es 'Auto Detectar'.""")
			gui.messageBox(msg, _("Información"), wx.ICON_INFORMATION)
			return

		idioma_origen = self.choice_origen.GetStringSelection()
		idioma_destino = self.choice_destino.GetStringSelection()

		# Temporalmente agregar los idiomas actuales al otro choice
		self.choice_origen.Append(idioma_destino)
		self.choice_destino.Append(idioma_origen)

		# Intercambiar las selecciones
		self.choice_origen.SetStringSelection(idioma_destino)
		self.choice_destino.SetStringSelection(idioma_origen)

		# Actualizar las listas de idiomas disponibles en ambos Choices
		self.actualizar_idiomas_destino(None)
		self.actualizar_idiomas_origen(None)

	def limpiar(self, event):
		"""
		Limpia los campos de texto de origen y destino.

		:param event: Evento de botón.
		"""
		self.texto_origen.SetValue('')
		self.texto_destino.SetValue('')
		self.texto_traducido_anterior = "" # Variable para almacenar el texto traducido anteriormente
		self.texto_destino_anterior = ""  # Variable para almacenar el texto traducido previamente en destino
		self.audio_obtenido = None  # Variable para almacenar el audio obtenido previamente
		self.lang_anterior = ""
		self.actualizar_contador_caracteres(None)
		self.texto_origen.SetFocus()

	def pegar(self, event):
		"""
		Pega el contenido del cuadro de texto de destino en la ventana activa.

		Si el cuadro de texto de destino no está vacío, este método copia su contenido al portapapeles
		y lo pega en la ventana activa. Si la ventana activa es una consola de Windows, utiliza un método
		alternativo para pegar el texto. También gestiona el respaldo del portapapeles y lo restaura después
		de pegar el contenido.

		:param event: El evento de botón o teclado que dispara esta acción.
		"""
		if not self.texto_destino.GetValue().strip():
			msg = \
_("""El cuadro de texto de destino está vacío. Por favor, traduce algo para pegar al foco.""")
			gui.messageBox(msg, _("Advertencia"), wx.ICON_WARNING)
			return

		self.Hide()
		event.Skip()
		paste = self.texto_destino.GetValue()
		# Source code taken from: frequentText add-on for NVDA. Written by Rui Fontes and Ângelo Abrantes
		try:
			clipboardBackup = api.getClipData()
		except:
			pass
		api.copyToClip(paste)
		time.sleep(0.1)
		api.processPendingEvents(False)
		focus = api.getFocusObject()
		if focus.windowClassName == "ConsoleWindowClass":
			# Windows console window - Control+V doesn't work here, so using an alternative method here
			WM_COMMAND = 0x0111
			watchdog.cancellableSendMessage(focus.windowHandle, WM_COMMAND, 0xfff1, 0)
		else:
			ui.message(_("Texto pegado al foco."))
			try:
				KeyboardInputGesture.fromName("Control+v").send()
			except:
				# Solución para teclados con caracteres cirilicos.
				KeyboardInputGesture.fromName("shift+insert").send()

		try:
			core.callLater(300, lambda: api.copyToClip(clipboardBackup))
		except:
			pass
		self.cerrar_dialogo(None)

	def onKeyPress(self, event):
		"""
		Maneja el evento de presión de teclas.

		:param event: El evento de presión de tecla.
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
		elif event.GetKeyCode() == wx.WXK_F3:
			self.pegar(event)
		elif event.GetKeyCode() == wx.WXK_ESCAPE:
			self.cerrar_dialogo(None)
		else:
			event.Skip()

	def cerrar_dialogo(self, event):
		"""
		Cierra el diálogo cuando se presiona el botón Cerrar.

		:param event: Evento de botón.
		"""
		self.frame.gestor_settings.IS_WinON = False
		if self.choice_origen.GetSelection() == 0:
			origen = "auto"
		else:
			origen = self.choice_origen.GetStringSelection().split(' - ')[-1]
		destino = self.choice_destino.GetStringSelection().split(' - ')[-1]
		self.frame.gestor_settings.guiLang_origen = origen
		self.frame.gestor_settings.guiLang_destino = destino
		self.frame.gestor_settings.guardaConfiguracion()
		self.Destroy()
		gui.mainFrame.postPopup()

