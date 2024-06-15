# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import wx
import threading
from time import sleep

# Carga traducción
addonHandler.initTranslation()

class ClipboardMonitor:
	"""
	Clase para monitorizar el portapapeles y detectar cambios de contenido de texto en tiempo real.
	"""
	def __init__(self, frame, check_interval=0.5):
		"""
		Inicializa una nueva instancia de la clase ClipboardMonitor.

		:param check_interval: Intervalo de tiempo en segundos para verificar el portapapeles.
		"""
		self.frame = frame
		self.check_interval = check_interval
		self.last_content = ""
		self._running = False
		self._initial_check = True

	def get_clipboard_text(self):
		"""
		Obtiene el texto actual del portapapeles, si está disponible.

		:return: El texto del portapapeles o None si no hay texto disponible.
		"""
		clipboard = wx.Clipboard.Get()
		try:
			clipboard.Open()
		except Exception as e:
			logHandler.log.error(_("Error al abrir el portapapeles: {0}").format(e))
			sleep(0.10)
			try:
				clipboard.Open()
			except Exception as e:
				logHandler.log.error(_("Error persistente al abrir el portapapeles: {0}").format(e))
				return None
		try:
			if clipboard.IsSupported(wx.DataFormat(wx.DF_TEXT)):
				text_data = wx.TextDataObject()
				clipboard.GetData(text_data)
				return text_data.GetText()
			return None
		finally:
			clipboard.Close()

	def set_clipboard_text(self, text):
		"""
		Copia el texto proporcionado al portapapeles.

		:param text: El texto que se va a copiar al portapapeles.
		"""
		clipboard = wx.Clipboard.Get()
		try:
			clipboard.Open()
			text_data = wx.TextDataObject()
			text_data.SetText(text)
			clipboard.SetData(text_data)
			clipboard.Flush()
		except Exception as e:
			logHandler.log.error(_("Error al copiar texto al portapapeles: {0}").format(e))
		finally:
			clipboard.Close()

	def clear_clipboard(self):
		"""
		Limpia el contenido del portapapeles.
		"""
		clipboard = wx.Clipboard.Get()
		try:
			clipboard.Open()
			clipboard.Clear()
		except Exception as e:
			logHandler.log.error(_("Error al limpiar el portapapeles: {0}").format(e))
		finally:
			clipboard.Close()

	def has_clipboard_changed(self):
		"""
		Verifica si el contenido del portapapeles ha cambiado.

		:return: True si el contenido del portapapeles ha cambiado, False en caso contrario.
		"""
		current_content = self.get_clipboard_text()
		if current_content is not None and current_content != self.last_content:
			self.last_content = current_content
			return True
		return False

	def start_monitoring(self):
		"""
		Inicia la monitorización del portapapeles en un hilo separado.
		"""
		self._running = True
		thread = threading.Thread(target=self._monitor_clipboard)
		thread.daemon = True
		thread.start()

	def stop_monitoring(self):
		"""
		Detiene la monitorización del portapapeles.
		"""
		self._running = False

	def _monitor_clipboard(self):
		"""
		Método interno que monitoriza el portapapeles periódicamente.
		"""
		while self._running:
			if self.has_clipboard_changed():
				if not self._initial_check:
					logHandler.log.info(_("El contenido del portapapeles ha cambiado: {0}").format(self.last_content))
				else:
					self._initial_check = False
			sleep(self.check_interval)

	def get_last_clipboard_text(self):
		"""
		Obtiene el último contenido de texto conocido del portapapeles.

		:return: El último contenido de texto del portapapeles.
		"""
		return self.last_content
