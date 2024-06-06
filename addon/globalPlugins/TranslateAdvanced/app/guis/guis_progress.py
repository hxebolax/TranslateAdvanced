# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
# Carga Python
import wx
import threading
# Carga personal
from ..src_translations.src_google_api_free import TranslatorGoogleApiFree

# Carga traducción
addonHandler.initTranslation()

class ProgressDialog(wx.Dialog):
	"""
	Diálogo de progreso para la traducción de textos.
	"""
	def __init__(self, frame, texto_a_traducir):
		"""
		Inicializa el diálogo de progreso.

		:param frame: El marco principal de la aplicación.
		:param texto_a_traducir: El texto que se va a traducir.
		"""
		super(ProgressDialog, self).__init__(None, title=_("Progreso de la Traducción"), size=(600, 200))

		self.frame = frame
		self.texto_a_traducir = texto_a_traducir
		self.canceled = False
		self.completed = False
		self.error = None
		self.traduccion_resultado = ""
		self.translator = TranslatorGoogleApiFree()

		# Crear widgets
		self.progress_bar = wx.Gauge(self, range=100)
		self.cancel_button = wx.Button(self, label=_("Cancelar"))

		# Layout
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.progress_bar, 0, wx.EXPAND | wx.ALL, 10)
		sizer.Add(self.cancel_button, 0, wx.ALL | wx.ALIGN_CENTER, 10)
		self.SetSizer(sizer)

		# Bindings
		self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)

		self.CenterOnScreen()

		# Iniciar hilo de traducción
		self.translate_thread = threading.Thread(target=self.translate_text, daemon=True)
		self.translate_thread.start()

	def on_cancel(self, event):
		"""
		Maneja el evento de cancelación de la traducción.

		:param event: Evento de botón.
		"""
		self.canceled = True
		self.translator.stop()
		wx.CallAfter(self.progress_bar.SetValue, 0)
		wx.CallAfter(self.onFinish)

	def translate_text(self):
		"""
		Hilo que maneja la traducción del texto.
		"""
		self.traduccion_resultado = self.translator.translate_google_api_free(
			lang_from="auto",
			lang_to=self.frame.gestor_settings.choiceLangDestino_google,
			text=self.texto_a_traducir,
			mostrar_progreso=True,
			widget=self.update_progress,
			IS_DIALOGO=True,
		)

		error = self.translator.get_error()
		if not self.canceled and not error["success"]:
			self.completed = True
			wx.CallAfter(self.onFinish)
		else:
			self.error = error["data"]
			wx.CallAfter(self.onFinish)

	def update_progress(self, progreso):
		"""
		Actualiza la barra de progreso.

		:param progreso: Porcentaje de progreso.
		"""
		wx.CallAfter(self.progress_bar.SetValue, int(progreso))

	def onFinish(self):
		"""
		Maneja el final del proceso de traducción.
		"""
		if self.IsModal():
			self.EndModal(wx.ID_OK if not self.canceled else wx.ID_CANCEL)
		else:
			self.Close()
