# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import globalPluginHandler
import addonHandler
import languageHandler
import logHandler
import globalVars
import core
import ui
import gui
import api
import speech
from speech import *
from scriptHandler import script, getLastScriptRepeatCount
# Carga Python
import os
import wx
import queue
from threading import Thread
# Carga personal
from .app.managers.managers_settings import GestorSettings
from .app.managers.managers_lang import TraductorIdiomas
from .app.managers.managers_translate import GestorTranslate
from .app.managers.managers_cache import LocalCacheHandler
from .app.managers.managers_clipboard import ClipboardMonitor
from .app.managers.managers_apis import APIManager
from .app.guis.guis_options import ConfigDialog
from .app.guis.guis_lang import DialogoLang
from .app.guis.guis_progress import ProgressDialog
from .app.guis.guis_result import DialogResults
from .app.guis.guis_hostory import DialogHistory
from .app.utils.utils_security import disableInSecureMode
from .app.utils.utils_network import is_connected, realizar_solicitud_https
from .app.utils.utils_various import getSelectedText

# Carga traducción
addonHandler.initTranslation()

@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	"""
	Clase principal del complemento Traductor Avanzado.
	"""
	def __init__(self, *args, **kwargs):
		"""
		Inicializa el complemento, verifica la conexión a internet y carga los certificados.
		"""
		super(GlobalPlugin, self).__init__(*args, **kwargs)

		if not is_connected():
			msg = \
_("""No se a encontrado conexión a internet.

Si esta conectado por Wifi puede que NVDA iniciara antes que se conectara.

Espere unos segundos y vuelva a reiniciar NVDA.

Si esta conectado por cable compruebe su conexión y asegúrese que todo esta correcto.

Se cancelara la carga del complemento Traductor Avanzado.""")
			logHandler.log.error(msg)
			return

		# Comprobación de almacén de certificados raíz de Windows.
		# Si no están correctos se actualizan.
		try:
			url = "https://www.google.com"
			contenido = realizar_solicitud_https(url)
			self.IS_OK = True
		except Exception as e:
			msg = \
_("""Se a encontrado errores en la carga del complemento.

Error:

{}""").format(str(e))
			logHandler.log.error(msg)
			return

		if hasattr(globalVars, _("Traductor Avanzado")):
			self.postStartupHandler()
		core.postNvdaStartup.register(self.postStartupHandler)
		globalVars.TranslateAdvanced = None

		# Gestores globales
		self.gestor_settings = None
		self.gestor_lang = None
		self.gestor_translate = None
		self.gestor_portapapeles = None
		self.gestor_apis = None
		# Utilidades
		self._cache = None
		self.menu = None

	def postStartupHandler(self):
		"""
		Controlador para la inicialización posterior al inicio de NVDA.
		"""
		Thread(target=self.__inicio, daemon=True).start()

	def __inicio(self):
		"""
		Inicializa los gestores y configura el menú de NVDA.
		"""
		# Carga el gestor de ajustes y todo lo necesario
		self.gestor_settings = GestorSettings(self)
		# Gestor de APIS
		self.gestor_apis = APIManager(self.gestor_settings.file_api)
		# Carga el cache
		self._cache = LocalCacheHandler(self.gestor_settings, logHandler)
		if self.gestor_settings.chkCache:
			self._cache.loadLocalCache()
		# Carga gestor de lenguajes
		self.gestor_lang = TraductorIdiomas(self)
		# Carga el gestor de traducción y todo lo necesario
		self.gestor_translate = GestorTranslate(self)
		self.gestor_settings._nvdaSpeak = speech._manager.speak
		self.gestor_settings._nvdaGetPropertiesSpeech = speech.getPropertiesSpeech
		speech._manager.speak = self.gestor_translate.speak
		speech.getPropertiesSpeech = self.gestor_settings._nvdaGetPropertiesSpeech
		self.gestor_settings._enableTranslation = False
		# Gestor del portapapeles
		self.gestor_portapapeles = ClipboardMonitor()
		# Menú de NVDA
		self.menu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.WXMenu = wx.Menu()
		self.mainItem = self.menu.AppendSubMenu(self.WXMenu, _("&Traductor Avanzado"), "")
		self.settingsItem = self.WXMenu.Append(1, _("&Configuración de Traductor Avanzado"), "")
		self.docuSettingsItem = self.WXMenu.Append(2, _("&Documentación del complemento"), "")
		self.donaSettingsItem = self.WXMenu.Append(3, _("&invítame a un café si te gusta mi trabajo"), "")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSettings, self.settingsItem)
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSettings, self.docuSettingsItem)
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSettings, self.donaSettingsItem)

		if self.IS_OK:
			msg = \
_("""Traductor Avanzado iniciado correctamente.""")
			logHandler.log.info(msg)

	def terminate(self):
		"""
		Finaliza el complemento y guarda la configuración.
		"""
		speech._manager.speak = self.gestor_settings._nvdaSpeak
		speech.getPropertiesSpeech = self.gestor_settings._nvdaGetPropertiesSpeech
		if self.gestor_settings.chkCache:
			self._cache.saveLocalCache()
		self.gestor_settings.guardaConfiguracion()
		self.menu.Remove(self.mainItem)
		core.postNvdaStartup.unregister(self.postStartupHandler)
		super().terminate()

	def chk_banderas(self, menu=False, toogle=False):
		"""
		Verifica condiciones antes de realizar acciones específicas.

		:param menu: Indica si el menú está abierto.
		:param toogle: Indica si se debe alternar una bandera.
		:return: True si todas las condiciones se cumplen, de lo contrario False.
		"""
		if self.gestor_settings.IS_WinON: 
			msg = \
_("""Ya hay una instancia de Traductor Avanzado abierta.

Ciérrela para realizar esta acción.""")
			gui.messageBox(msg, _("Información"), wx.ICON_INFORMATION) if menu else ui.message(msg)
			return False
		if self.gestor_settings.is_active_translate: 
			msg = \
_("""Tiene una traducción en curso. Espere a que termine.""")
			gui.messageBox(msg, _("Información"), wx.ICON_INFORMATION) if menu else ui.message(msg)
			return False
		if toogle:
			if self.gestor_settings._enableTranslation: 
				msg = \
_("""Tiene la traducción simultanea activada.

Desactívela para realizar esta acción.""")
				gui.messageBox(msg, _("Información"), wx.ICON_INFORMATION) if menu else ui.message(msg)
				return False
		return True

	def onSettings(self, event):
		"""
		Maneja los eventos del menú de configuración.

		:param event: Evento de menú.
		"""
		if event.GetId() == 1: # Configuración
			self.script_onSettings(event.GetId(), True)
		elif event.GetId() == 2: # Documentación
			wx.LaunchDefaultBrowser(addonHandler.Addon(os.path.join(os.path.dirname(__file__), "..", "..")).getDocFilePath())
		elif event.GetId() == 3: # Donaciones
			wx.LaunchDefaultBrowser("https://paypal.me/hjbcdonaciones?country.x=ES&locale.x=es_ES")

	@script(gesture=None, description=_("Abre la configuración del complemento"), category=_("Traductor Avanzado"))
	def script_onSettings(self, event, menu=False):
		"""
		Abre la configuración del complemento.

		:param event: Evento que desencadena la función.
		:param menu: Indica si el menú está abierto.
		"""
		if self.chk_banderas(menu, True):
			LaunchThread(self, 1).start()

	@script(gesture=None, description=_("Cambiar idioma de origen"), category=_("Traductor Avanzado"))
	def script_choice_lang_origen(self, event):
		"""
		Cambia el idioma de origen del traductor.

		:param event: Evento que desencadena la función.
		"""
		if self.chk_banderas(False, True):
			if self.gestor_settings.choiceOnline == 7: # Solo para Microsoft
				LaunchThread(self, 2).start()
			else:
				ui.message(_("El idioma origen solo puede ser cambiado si tiene seleccionado el traductor de Microsoft."))

	@script(gesture=None, description=_("Cambiar idioma de destino"), category=_("Traductor Avanzado"))
	def script_choice_lang_destino(self, event):
		"""
		Cambia el idioma de destino del traductor.

		:param event: Evento que desencadena la función.
		"""
		if self.chk_banderas(False, True):
			LaunchThread(self, 3).start()

	@script(gesture=None, description=_("Cambiar el modulo de traducción"), category=_("Traductor Avanzado"))
	def script_choice_translate_change(self, event):
		"""
		Cambia el módulo de traducción.

		:param event: Evento que desencadena la función.
		"""
		if self.chk_banderas(False, True):
			LaunchThread(self, 4).start()

	@script(gesture=None, description=_("Eliminar todas las traducciones en caché para todas las aplicaciones"), category=_("Traductor Avanzado"))
	def script_flushAllCache(self, event):
		"""
		Elimina todas las traducciones en caché para todas las aplicaciones.

		:param event: Evento que desencadena la función.
		"""
		if getLastScriptRepeatCount() == 0:
			ui.message(_("Pulse dos veces para eliminar todas las traducciones en caché de todas las aplicaciones."))
			return
		self.gestor_settings._translationCache = {}
		path = self.gestor_settings.dir_cache
		error = False
		if os.path.isdir(path):
			if not os.listdir(path):
				ui.message(_("No hay cache para borrar."))
				return
			for entry in os.listdir(path):
				try:
					os.unlink(os.path.join(path, entry))
				except Exception:
					logHandler.log.error(_(f"Fallo al eliminar {entry}"))
					error = True
		else:
			ui.message(_("El directorio de la cache no existe."))
			return
		ui.message(_("Se ha eliminado toda la cache.")) if not error else ui.message(_("No se a podido eliminar toda la cache."))

	@script(gesture=None, description=_("Eliminar la caché de traducción para la aplicación enfocada actualmente"), category=_("Traductor Avanzado"))
	def script_flushCurrentAppCache(self, event):
		"""
		Elimina la caché de traducción para la aplicación enfocada actualmente.

		:param event: Evento que desencadena la función.
		"""
		try:
			appName = globalVars.focusObject.appModule.appName
		except:
			ui.message(_("No hay aplicación enfocada."))
			return
		if getLastScriptRepeatCount() == 0:
			data = languageHandler.getLanguageDescription(self.gestor_translate.get_choice_lang_destino())
			ui.message(_("Pulse dos veces para eliminar todas las traducciones de {} en lenguaje {}").format(appName, self.gestor_translate.get_choice_lang_destino() if data is None else data))
			return
		self.gestor_settings._translationCache[appName] = {}
		fullPath = os.path.join(self.gestor_settings.dir_cache, "{}_{}.json".format(appName, self.gestor_translate.get_choice_lang_destino()))
		if os.path.exists(fullPath):
			try:
				os.unlink(fullPath)
				ui.message(_("Se ha borrado la cache de la aplicación {} correctamente.").format(appName))
			except Exception as e:
				logHandler.log.error(_("Fallo al borrar la cache de la aplicación {} : {}").format(appName, str(e)))
				ui.message(_("Error al borrar la caché de traducción de la aplicación."))
		else:
			ui.message(_("No hay traducciones guardadas para {}").format(appName))

	@script(gesture=None, description=_("Activa o desactiva la cache de traducción"), category=_("Traductor Avanzado"))
	def script_toggleCache(self, event):
		"""
		Activa o desactiva la caché de traducción según el estado actual.
		
		:param event: El evento que desencadena la función.
		"""
		# Verifica si hay alguna ventana abierta
		if self.gestor_settings.IS_WinON:
			ui.message(_("La activación o desactivación de la cache no puede hacerse mientras haya una ventana de Traductor Avanzado abierta"))
			return
		
		# Guarda el estado actual de la traducción
		temp = self.gestor_settings._enableTranslation
		
		# Si la traducción está habilitada, la deshabilita y guarda la caché local si corresponde
		if self.gestor_settings._enableTranslation:
			self.gestor_settings._enableTranslation = False
			temp = True
			if self.gestor_settings.chkCache:
				self._cache.saveLocalCache()
		else:
			temp = False
		
		# Cambia el estado de la caché
		self.gestor_settings.chkCache = not self.gestor_settings.chkCache
		
		# Muestra el mensaje correspondiente a la acción realizada
		if self.gestor_settings.chkCache:
			ui.message(_("Cache de traducción activada."))
		else:
			ui.message(_("Cache de traducción desactivada."))
		
		# Actualiza la configuración de la caché
		self.gestor_settings.setConfig("chkCache", self.gestor_settings.chkCache)
		
		# Si la traducción estaba habilitada, la re-habilita y carga la caché local si corresponde
		if temp:
			self.gestor_settings._enableTranslation = True
			if self.gestor_settings.chkCache:
				self._cache.loadLocalCache()

	@script(gesture=None, description=_("Copiar el ultimo texto traducido al portapapeles"), category=_("Traductor Avanzado"))
	def script_copyLastTranslation(self, event):
		"""
		Copia el último texto traducido al portapapeles si no hay una traducción en curso.
		
		:param event: El evento que desencadena la función.
		"""
		
		# Verifica si hay una traducción en curso
		if self.gestor_settings.is_active_translate:
			ui.message(_("Tiene una traducción en curso. Espere a que termine."))
			return
		
		# Verifica si existe texto traducido y si su longitud es mayor a cero
		if self.gestor_settings._lastTranslatedText and len(self.gestor_settings._lastTranslatedText) > 0:
			# Copia el texto traducido al portapapeles
			self.gestor_portapapeles.set_clipboard_text(self.gestor_settings._lastTranslatedText)
			# Muestra un mensaje indicando el texto copiado
			ui.message(_("Se ha copiado lo siguiente al portapapeles: {}").format(self.gestor_settings._lastTranslatedText))
		else:
			# Muestra un mensaje indicando que no hay texto para copiar
			ui.message(_("No se ha podido copiar nada al portapapeles"))

	@script(gesture=None, description=_("Activa o desactiva la traducción simultánea Online"), category=_("Traductor Avanzado"))
	def script_toggleTranslateOnline(self, event):
		"""
		Activa o desactiva la traducción simultánea Online.

		Verifica las condiciones necesarias antes de activar o desactivar la traducción Online,
		y muestra mensajes adecuados según el estado actual del sistema.
		"""
		if self.chk_banderas():
			self.gestor_settings._enableTranslation = not self.gestor_settings._enableTranslation
			ui.message(_("Traducción activada.")) if self.gestor_settings._enableTranslation else ui.message(_("Traducción desactivada."))
			if self.gestor_settings.chkCache:
				self._cache.loadLocalCache() if self.gestor_settings._enableTranslation else self._cache.saveLocalCache()

	@script(gesture=None, description=_("Traduce el texto seleccionado"), category=_("Traductor Avanzado"))
	def script_translate_select(self, event):
		"""
		Traduce el texto seleccionado.

		:param event: Evento que desencadena la función.
		"""
		if self.chk_banderas(False, True):
			# Obtiene el texto seleccionado
			temp = getSelectedText(api.getCaretObject())
			if not temp['success'] or temp['data'] == '':
				ui.message(_("Sin selección para traducir"))
				return
			# Deshabilita la traducción y activa el estado de traducción
			self.gestor_settings._enableTranslation = False
			self.gestor_settings.is_active_translate = True
			LaunchThread(self, 5, temp['data']).start()

	@script(gesture=None, description=_("Muestra el historial de traducción"), category=_("Traductor Avanzado"))
	def script_translate_history(self, event):
		"""
		Muestra el historial de traducción.

		:param event: Evento que desencadena la función.
		"""
		if self.chk_banderas(False, True):
			if not self.gestor_settings.historialOrigen:
				ui.message(_("No hay nada en el historial todavía."))
				return
			LaunchThread(self, 6).start()

class LaunchThread(Thread):
	"""
	Clase para gestionar la ejecución de diferentes diálogos en hilos separados.
	"""
	def __init__(self, frame, option, text=None):
		"""
		Inicializa el hilo con las opciones proporcionadas.

		:param frame: El marco principal.
		:param option: La opción a ejecutar.
		:param text: El texto a traducir, si aplica.
		"""
		super(LaunchThread, self).__init__()

		self.frame = frame
		self.option = option
		self.text = text
		self.daemon = True

	def run(self):
		"""
		Ejecuta la opción seleccionada en un hilo separado.
		"""
		def appLauncherAjustes():
			"""
			Lanza el diálogo de configuración.
			"""
			self._main = ConfigDialog(gui.mainFrame, self.frame)
			gui.mainFrame.prePopup()
			self._main.Show()

		def change_origen():
			"""
			Cambia el idioma de origen.
			"""
			gui.mainFrame.prePopup()
			dlg = DialogoLang(None, self.frame, 0)
			dlg.ShowModal()
			dlg.Destroy()
			gui.mainFrame.postPopup()

		def change_destino():
			"""
			Cambia el idioma de destino.
			"""
			gui.mainFrame.prePopup()
			dlg = DialogoLang(None, self.frame, 1)
			dlg.ShowModal()
			dlg.Destroy()
			gui.mainFrame.postPopup()

		def change_traductor():
			"""
			Cambia el módulo de traducción.
			"""
			gui.mainFrame.prePopup()
			dlg = DialogoLang(None, self.frame, 2)
			dlg.ShowModal()
			dlg.Destroy()
			gui.mainFrame.postPopup()

		def translate_select():
			"""
			Traduce el texto seleccionado.
			"""
			self.progress_dialog = ProgressDialog(self.frame, self.text)
			result = self.progress_dialog.ShowModal()
			if result == wx.ID_OK:
				self.frame.gestor_settings.is_active_translate = False
				if self.progress_dialog.completed:
					if not self.progress_dialog.traduccion_resultado or self.text == self.progress_dialog.traduccion_resultado:
						gui.messageBox(_("No se ha podido obtener la traducción de lo seleccionado."), _("Información"), wx.ICON_INFORMATION)
						return
					show_translation_result(self.progress_dialog.traduccion_resultado)
				else:
					self.frame.gestor_settings.is_active_translate = False
					gui.messageBox(_("Hubo un error en la traducción:\n\n") + self.progress_dialog.error, _("Error"), wx.OK | wx.ICON_ERROR)
			elif result == wx.ID_CANCEL:
				self.frame.gestor_settings.is_active_translate = False
				gui.messageBox(_("La traducción fue cancelada por el usuario."), _("Cancelado"), wx.OK | wx.ICON_INFORMATION)

		def show_translation_result(data):
			"""
			Muestra el diálogo con el resultado de la traducción.
			"""
			gui.mainFrame.prePopup()
			dlg = DialogResults(None, _("Resultado de la traducción"), data)
			dlg.ShowModal()
			dlg.Destroy()
			gui.mainFrame.postPopup()

		def translate_history():
			"""
			Muestra el historial de traducción.
			"""
			gui.mainFrame.prePopup()
			dlg = DialogHistory(None, self.frame)
			dlg.ShowModal()
			dlg.Destroy()
			gui.mainFrame.postPopup()

		if self.option == 1: # Configuración
			wx.CallAfter(appLauncherAjustes)
		elif self.option == 2: # Cambiar idioma origen
			wx.CallAfter(change_origen)
		elif self.option == 3: # Cambiar idioma destino
			wx.CallAfter(change_destino)
		elif self.option == 4: # Cambiar modulo traducción destino
			wx.CallAfter(change_traductor)
		elif self.option == 5: # Traducir seleccionado
			wx.CallAfter(translate_select)
		elif self.option == 6: # Historial de traducción
			wx.CallAfter(translate_history)
