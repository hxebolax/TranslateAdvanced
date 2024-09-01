# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
#
# Carga NVDA
import addonHandler
import ui
import gui
# Carga Python
import sys
import os
import wx
import threading
import tempfile
import time
# Carga personal
from ..data.lib._311.wx import media as wx_media

# Carga traducción
addonHandler.initTranslation()

class WAVPlayer:
	"""
	Clase para manejar la reproducción de archivos WAV utilizando wxPython.
	"""
	def __init__(self, parent):
		"""
		Inicializa una instancia del reproductor de WAV.
		:param parent: El padre wx.Panel o wx.Frame que contiene el reproductor.
		"""
		# Crear un MediaCtrl con el padre dado y sin agregarlo a ningún sizer para que no sea visible
		self.media_ctrl = wx_media.MediaCtrl(parent, style=wx_media.MC_NO_AUTORESIZE)
		self.media_ctrl.Hide()  # Ocultar el widget para que no sea visible
		self.is_playing = False
		self.is_paused = False
		self.filepath = None
		self.ui_update_callback = None  # Callback para actualizar la UI cuando el audio termina
		self.media_ctrl.Bind(wx_media.EVT_MEDIA_STOP, self.on_media_finished)

	def load(self, filepath):
		"""
		Carga un archivo WAV para su reproducción.
		:param filepath: Ruta del archivo WAV.
		"""
		try:
			if not self.media_ctrl.Load(filepath):
				raise Exception(_("No se pudo cargar el archivo WAV."))
			self.filepath = filepath
			self.media_ctrl.SetVolume(0.5)  # Volumen inicial al 50%
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)

	def load_from_bytes(self, audio_bytes):
		"""
		Carga un archivo WAV desde una cadena de bytes para su reproducción.
		:param audio_bytes: Cadena de bytes que contiene el audio WAV.
		"""
		try:
			# Crear un archivo temporal para cargar los bytes de audio
			with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
				temp_file.write(audio_bytes)
				temp_filepath = temp_file.name

			if not self.media_ctrl.Load(temp_filepath):
				os.remove(temp_filepath)  # Eliminar archivo temporal si la carga falla
				raise Exception(_("No se pudo cargar el archivo WAV desde bytes."))
			self.filepath = temp_filepath
			self.media_ctrl.SetVolume(0.5)  # Volumen inicial al 50%
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)

	def play(self):
		"""
		Reproduce el archivo WAV cargado.
		"""
		try:
			if self.filepath is None:
				raise Exception(_("No se ha cargado ningún archivo WAV."))
			if self.is_paused:
				self.media_ctrl.Play()
				self.is_paused = False
			else:
				self.media_ctrl.Play()
			self.is_playing = True
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)

	def pause(self):
		"""
		Pausa la reproducción del archivo WAV.
		"""
		try:
			if not self.is_playing:
				return
			self.media_ctrl.Pause()
			self.is_paused = True
			self.is_playing = False
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)

	def stop(self):
		"""
		Detiene la reproducción del archivo WAV.
		"""
		try:
			self.media_ctrl.Stop()
			self.is_playing = False
			self.is_paused = False
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)

	def set_volume(self, volume):
		"""
		Establece el volumen del reproductor.
		:param volume: Volumen a establecer (0-100).
		"""
		try:
			volume = max(0, min(100, volume)) / 100.0  # Asegurarse de que el volumen esté en el rango 0-1
			self.media_ctrl.SetVolume(volume)
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)

	def set_speed(self, speed):
		"""
		Establece la velocidad de reproducción del reproductor.
		:param speed: Velocidad a establecer en rango de 0.75 a 2.0.
		"""
		try:
			playback_rate = speed / 50.0  # Convertir el rango a un rango de 0.0-2.0 (donde 1.0 es la velocidad normal)
			self.media_ctrl.SetPlaybackRate(playback_rate)
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)

	def get_current_time(self):
		"""
		Obtiene el tiempo transcurrido de la reproducción.
		:return: Tiempo transcurrido en milisegundos.
		"""
		try:
			return self.media_ctrl.Tell()
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)
			return 0

	def get_total_time(self):
		"""
		Obtiene el tiempo total del archivo WAV.
		:return: Tiempo total en milisegundos.
		"""
		try:
			return self.media_ctrl.Length()
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)
			return 0

	def format_time(self, milliseconds):
		"""
		Convierte el tiempo en milisegundos a un formato legible (hh:mm:ss).
		:param milliseconds: Tiempo en milisegundos.
		:return: Tiempo en formato hh:mm:ss.
		"""
		try:
			seconds = milliseconds // 1000
			minutes = seconds // 60
			seconds = seconds % 60
			hours = minutes // 60
			minutes = minutes % 60
			return f"{hours:02}:{minutes:02}:{seconds:02}"
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)
			return "00:00:00"

	def on_media_finished(self, event):
		"""
		Maneja el evento cuando el audio finaliza la reproducción.
		"""
		try:
			self.is_playing = False
			self.is_paused = False
			if self.ui_update_callback:
				wx.CallAfter(self.ui_update_callback)  # Llama al callback para actualizar la interfaz
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)

	def close(self):
		"""
		Cierra el reproductor y libera los recursos.
		"""
		try:
			if self.filepath and os.path.exists(self.filepath) and 'temp_audio' in self.filepath:
				try:
					os.remove(self.filepath)  # Eliminar archivo temporal si existe
				except:
					pass
			self.media_ctrl.Destroy()
		except Exception as e:
			gui.messageBox(str(e), _("Error"), wx.ICON_ERROR)

class ReproductorWav(wx.Dialog):
	"""
	Clase que crea un diálogo personalizado con controles específicos para reproducir audio WAV.

	:param parent: Ventana padre del diálogo.
	:param parent_primary: Ventana principal de la aplicación.
	:param text: Texto asociado a la reproducción de audio.
	:param audio: Bytes del archivo de audio WAV para ser reproducido.
	"""

	def __init__(self, parent, parent_primary, text, audio):
		"""
		Inicializa el diálogo con sus componentes y disposición.
		:param parent: Ventana padre del diálogo.
		:param parent_primary: Ventana principal de la aplicación.
		:param text: Texto asociado a la reproducción de audio.
		:param audio: Bytes del archivo de audio WAV para ser reproducido.
		"""
		try:
			super().__init__(parent, title=_("Reproductor de audio"), size=(600, 400))

			self.frame = parent_primary
			self.text = text
			self.audio = audio
			# Pasar el panel principal como padre para el WAVPlayer
			panel = wx.Panel(self)
			self.player = WAVPlayer(panel)
			self.player.ui_update_callback = self.on_audio_finished  # Establece el callback
			self.player.load_from_bytes(self.audio)  # Cambia la ruta al archivo deseado
			self.InitUI(panel)
			self.CrearTablaAceleradora()
			self.AgregarAyudas()
		except Exception as e:
			gui.messageBox(str(e), _("Error al inicializar el diálogo"), wx.ICON_ERROR)

	def InitUI(self, panel):
		"""
		Inicializa la interfaz de usuario con todos los componentes necesarios.
		:param panel: Panel wx.Panel donde se colocarán los componentes.
		"""
		try:
			# Sizer vertical principal
			vertical_sizer = wx.BoxSizer(wx.VERTICAL)

			# Crear etiqueta y cuadro de texto de solo lectura
			etiqueta = wx.StaticText(panel, label=_("&Texto traducido:"))
			self.cuadro_texto = wx.TextCtrl(panel, style=wx.TE_READONLY | wx.TE_MULTILINE)
			self.cuadro_texto.SetMinSize((-1, 100))  # Altura mínima para el cuadro de texto

			# Añadir etiqueta y cuadro de texto al sizer vertical
			vertical_sizer.Add(etiqueta, 0, wx.ALL, 5)
			vertical_sizer.Add(self.cuadro_texto, 1, wx.EXPAND | wx.ALL, 5)

			# Sizer horizontal para los botones de control
			horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

			# Botones de control
			self.btn_atrasar = wx.Button(panel, label=_("Atrasar (F1)"))
			self.btn_reproducir = wx.Button(panel, label=_("Reproducir (F2)"))
			self.btn_adelantar = wx.Button(panel, label=_("Adelantar (F3)"))
			self.btn_detener = wx.Button(panel, label=_("Detener (F4)"))

			# Añadir botones al sizer horizontal
			horizontal_sizer.Add(self.btn_atrasar, 0, wx.ALL, 5)
			horizontal_sizer.Add(self.btn_reproducir, 0, wx.ALL, 5)
			horizontal_sizer.Add(self.btn_adelantar, 0, wx.ALL, 5)
			horizontal_sizer.Add(self.btn_detener, 0, wx.ALL, 5)

			# Nuevo sizer horizontal para los controles de volumen y velocidad
			volumen_velocidad_sizer = wx.BoxSizer(wx.HORIZONTAL)

			# Etiqueta y slider de volumen
			etiqueta_volumen = wx.StaticText(panel, label=_("Volumen (F5 / F6)"))
			self.slider_volumen = wx.Slider(panel, minValue=0, maxValue=100, value=50)  # Iniciar en 50 (50% volumen)

			# Añadir etiqueta y slider al sizer horizontal
			volumen_velocidad_sizer.Add(etiqueta_volumen, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
			volumen_velocidad_sizer.Add(self.slider_volumen, 1, wx.EXPAND | wx.ALL, 5)

			# Etiqueta y choice de velocidad
			etiqueta_velocidad = wx.StaticText(panel, label=_("Velocidad (F7 / F8)"))
			self.choice_velocidad = wx.Choice(panel, choices=["0.50", "0.75", "1.0", "1.25", "1.5", "1.75", "2.0"])
			self.choice_velocidad.SetSelection(2)  # Selecciona 1.0 como valor por defecto

			# Añadir etiqueta y choice de velocidad al sizer horizontal
			volumen_velocidad_sizer.Add(etiqueta_velocidad, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
			volumen_velocidad_sizer.Add(self.choice_velocidad, 1, wx.EXPAND | wx.ALL, 5)

			# Añadir el sizer horizontal al sizer vertical
			vertical_sizer.Add(horizontal_sizer, 0, wx.EXPAND | wx.ALL, 5)
			vertical_sizer.Add(volumen_velocidad_sizer, 0, wx.EXPAND | wx.ALL, 5)

			# Sizer horizontal para los botones "Guardar" y "Cerrar"
			botones_sizer = wx.BoxSizer(wx.HORIZONTAL)
			self.btn_guardar = wx.Button(panel, label=_("&Guardar"))
			self.btn_cerrar = wx.Button(panel, label=_("&Cerrar"))

			# Añadir botones al sizer de botones
			botones_sizer.Add(self.btn_guardar, 0, wx.ALL, 5)
			botones_sizer.Add(self.btn_cerrar, 0, wx.ALL, 5)

			# Añadir el sizer de botones al sizer vertical
			vertical_sizer.Add(botones_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

			# Establecer el sizer del panel
			panel.SetSizer(vertical_sizer)

			# Ajustar el tamaño del diálogo
			self.Layout()
			self.CenterOnScreen()

			# Enlazar eventos a métodos
			self.btn_reproducir.Bind(wx.EVT_BUTTON, self.on_play_pause)
			self.btn_detener.Bind(wx.EVT_BUTTON, self.on_stop)
			self.btn_atrasar.Bind(wx.EVT_BUTTON, self.on_rewind)
			self.btn_adelantar.Bind(wx.EVT_BUTTON, self.on_forward)
			self.btn_guardar.Bind(wx.EVT_BUTTON, self.on_save)
			self.btn_cerrar.Bind(wx.EVT_BUTTON, self.on_close)

			self.slider_volumen.Bind(wx.EVT_SLIDER, self.on_change_volume)
			self.choice_velocidad.Bind(wx.EVT_CHOICE, self.on_change_speed)  # Nuevo evento para el wx.Choice

			self.cuadro_texto.SetValue(self.text)
			self.btn_reproducir.SetFocus()
		except Exception as e:
			gui.messageBox(str(e), _("Error al inicializar la interfaz de usuario"), wx.ICON_ERROR)

	def CrearTablaAceleradora(self):
		"""
		Crea una tabla aceleradora para asignar atajos de teclado a las funciones principales del reproductor.
		"""
		# Crear IDs para los aceleradores
		self.accel_id_atrasar = wx.NewIdRef()
		self.accel_id_reproducir = wx.NewIdRef()
		self.accel_id_adelantar = wx.NewIdRef()
		self.accel_id_detener = wx.NewIdRef()
		self.accel_id_bajar_volumen = wx.NewIdRef()
		self.accel_id_subir_volumen = wx.NewIdRef()
		self.accel_id_bajar_velocidad = wx.NewIdRef()
		self.accel_id_subir_velocidad = wx.NewIdRef()
		self.accel_id_informacion = wx.NewIdRef()

		# Configuración de la tabla aceleradora
		accel_tbl = wx.AcceleratorTable([
			(wx.ACCEL_NORMAL, wx.WXK_F1, self.accel_id_atrasar),
			(wx.ACCEL_NORMAL, wx.WXK_F2, self.accel_id_reproducir),
			(wx.ACCEL_NORMAL, wx.WXK_F3, self.accel_id_adelantar),
			(wx.ACCEL_NORMAL, wx.WXK_F4, self.accel_id_detener),
			(wx.ACCEL_NORMAL, wx.WXK_F5, self.accel_id_bajar_volumen),
			(wx.ACCEL_NORMAL, wx.WXK_F6, self.accel_id_subir_volumen),
			(wx.ACCEL_NORMAL, wx.WXK_F7, self.accel_id_bajar_velocidad),
			(wx.ACCEL_NORMAL, wx.WXK_F8, self.accel_id_subir_velocidad),
			(wx.ACCEL_NORMAL, wx.WXK_F9, self.accel_id_informacion)
		])
		self.SetAcceleratorTable(accel_tbl)

		# Asignar los IDs al método correspondiente
		self.Bind(wx.EVT_MENU, self.on_rewind, id=self.accel_id_atrasar)
		self.Bind(wx.EVT_MENU, self.on_play_pause, id=self.accel_id_reproducir)
		self.Bind(wx.EVT_MENU, self.on_forward, id=self.accel_id_adelantar)
		self.Bind(wx.EVT_MENU, self.on_stop, id=self.accel_id_detener)
		self.Bind(wx.EVT_MENU, self.decrease_volume, id=self.accel_id_bajar_volumen)
		self.Bind(wx.EVT_MENU, self.increase_volume, id=self.accel_id_subir_volumen)
		self.Bind(wx.EVT_MENU, self.decrease_speed, id=self.accel_id_bajar_velocidad)
		self.Bind(wx.EVT_MENU, self.increase_speed, id=self.accel_id_subir_velocidad)
		self.Bind(wx.EVT_MENU, self.mostrar_informacion, id=self.accel_id_informacion)

	def AgregarAyudas(self):
		"""
		Establece los textos de ayuda para todos los widgets de la interfaz.
		"""
		self.SetHelp(self.cuadro_texto, _("Este cuadro muestra el texto traducido. Es de solo lectura."))
		self.SetHelp(self.btn_atrasar, _("Presiona este botón para retroceder la reproducción 10 segundos."))
		self.SetHelp(self.btn_reproducir, _("Presiona este botón para reproducir o pausar la reproducción."))
		self.SetHelp(self.btn_adelantar, _("Presiona este botón para adelantar la reproducción 10 segundos."))
		self.SetHelp(self.btn_detener, _("Presiona este botón para detener la reproducción."))
		self.SetHelp(self.slider_volumen, _("Ajusta el volumen de reproducción con este control."))
		self.SetHelp(self.choice_velocidad, _("Selecciona la velocidad de reproducción con esta lista."))
		self.SetHelp(self.btn_guardar, _("Presiona este botón para guardar el archivo de audio."))
		self.SetHelp(self.btn_cerrar, _("Presiona este botón para cerrar el diálogo."))

	def SetHelp(self, widget, text):
		"""
		Establece un mensaje de ayuda para un widget específico.

		:param widget: El widget al cual se le asignará el mensaje de ayuda.
		:param text: El texto del mensaje de ayuda que se mostrará cuando el widget reciba el enfoque y se presione Ctrl+H.
		"""
		self.frame.gestor_ayuda.agregar_ayuda(widget, text)

	def informar_accion(self, mensaje):
		"""
		Utiliza ui.message para informar al usuario de una acción específica realizada.

		:param mensaje: El mensaje a mostrar al usuario.
		"""
		if self.player.is_playing or self.player.is_paused:
			ui.message(mensaje)

	def mostrar_informacion(self, event):
		"""
		Muestra información sobre el reproductor.
		"""
		try:
			current_time = self.player.get_current_time()
			total_time = self.player.get_total_time()
			percentage = (current_time / total_time) * 100 if total_time > 0 else 0
			status_text = _(
				f"Tiempo transcurrido: {self.player.format_time(current_time)}  "
				f"Tiempo total: {self.player.format_time(total_time)}  "
				f"Porcentaje de reproducción: {percentage:.2f}%"
			)
			self.informar_accion(status_text)
		except Exception as e:
			gui.messageBox(str(e), _("Error al actualizar el estado"), wx.ICON_ERROR)

	def decrease_volume(self, event):
		"""
		Disminuye el volumen del reproductor al mover el slider de volumen un paso hacia abajo.
		"""
		current_volume = self.slider_volumen.GetValue()
		if current_volume > 0:
			self.slider_volumen.SetValue(current_volume - 1)
			self.player.set_volume(current_volume - 1)
			ui.message(_("Volumen {}%".format(current_volume - 1)))

	def increase_volume(self, event):
		"""
		Aumenta el volumen del reproductor al mover el slider de volumen un paso hacia arriba.
		"""
		current_volume = self.slider_volumen.GetValue()
		if current_volume < 100:
			self.slider_volumen.SetValue(current_volume + 1)
			self.player.set_volume(current_volume + 1)
			ui.message(_("Volumen {}%".format(current_volume + 1)))

	def decrease_speed(self, event):
		"""
		Disminuye la velocidad de reproducción al mover el choice de velocidad un paso hacia abajo.
		"""
		current_selection = self.choice_velocidad.GetSelection()
		if current_selection > 0:
			self.choice_velocidad.SetSelection(current_selection - 1)
			self.on_change_speed(None)
			ui.message(_("Velocidad {}%".format(self.choice_velocidad.GetString(current_selection - 1))))

	def increase_speed(self, event):
		"""
		Aumenta la velocidad de reproducción al mover el choice de velocidad un paso hacia arriba.
		"""
		current_selection = self.choice_velocidad.GetSelection()
		if current_selection < self.choice_velocidad.GetCount() - 1:
			self.choice_velocidad.SetSelection(current_selection + 1)
			self.on_change_speed(None)
			ui.message(_("Velocidad {}%".format(self.choice_velocidad.GetString(current_selection + 1))))

	def on_load(self, event):
		"""
		Maneja el evento de cargar un archivo WAV desde el sistema de archivos.
		"""
		try:
			with wx.FileDialog(self, _("Cargar archivo WAV"), wildcard=_("Archivo WAV (*.wav)|*.wav"),
								style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
				if fileDialog.ShowModal() == wx.ID_CANCEL:
					return  # El usuario canceló la operación

				pathname = fileDialog.GetPath()
				try:
					self.player.load(pathname)
				except Exception as e:
					gui.messageBox(_("No se pudo cargar el archivo: {}").format(e), _("Error"), wx.ICON_ERROR)
		except Exception as e:
			gui.messageBox(str(e), _("Error al cargar archivo"), wx.ICON_ERROR)

	def on_save(self, event):
		"""
		Maneja el evento para guardar los bytes de audio en un archivo WAV.
		"""
		try:
			with wx.FileDialog(self, _("Guardar archivo WAV"), wildcard=_("Archivo WAV (*.wav)|*.wav"),
								style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
				if fileDialog.ShowModal() == wx.ID_CANCEL:
					return  # El usuario canceló la operación

				pathname = fileDialog.GetPath()
				try:
					with open(pathname, 'wb') as f:
						f.write(self.audio)
					gui.messageBox(_("Archivo guardado correctamente."), _("Información"), wx.ICON_INFORMATION)
				except Exception as e:
					gui.messageBox(_("No se pudo guardar el archivo: {}").format(e), _("Error"), wx.ICON_ERROR)
		except Exception as e:
			gui.messageBox(str(e), _("Error al guardar archivo"), wx.ICON_ERROR)

	def on_play_pause(self, event):
		"""
		Maneja el evento de reproducir o pausar el archivo WAV.
		"""
		try:
			if self.player.is_playing:
				self.player.pause()
				self.btn_reproducir.SetLabel(_("Reproducir (F2)"))
				self.informar_accion(_("Pausar"))
			else:
				self.player.play()
				self.btn_reproducir.SetLabel(_("Pausar (F2)"))
				self.informar_accion(_("Reproducir"))
		except Exception as e:
			gui.messageBox(_("No se pudo reproducir o pausar el archivo: {}").format(e), _("Error"), wx.ICON_ERROR)

	def on_stop(self, event):
		"""
		Maneja el evento de detener la reproducción.
		"""
		try:
			self.informar_accion(_("Detener"))
			self.player.stop()
			self.btn_reproducir.SetLabel(_("Reproducir (F2)"))
		except Exception as e:
			gui.messageBox(_("No se pudo detener el archivo: {}").format(e), _("Error"), wx.ICON_ERROR)

	def on_rewind(self, event):
		"""
		Maneja el evento de atrasar la reproducción.
		"""
		try:
			self.informar_accion(_("Atrasar 10 segundos"))
			self.player.media_ctrl.Seek(self.player.get_current_time() - 10000)  # Atrasar 10 segundos
		except Exception as e:
			gui.messageBox(_("No se pudo atrasar el archivo: {}").format(e), _("Error"), wx.ICON_ERROR)

	def on_forward(self, event):
		"""
		Maneja el evento de adelantar la reproducción.
		"""
		try:
			self.informar_accion(_("Adelantar 10 segundos"))
			self.player.media_ctrl.Seek(self.player.get_current_time() + 10000)  # Adelantar 10 segundos
			if self.player.get_current_time() >= self.player.get_total_time():
				self.on_audio_finished()
		except Exception as e:
			gui.messageBox(_("No se pudo adelantar el archivo: {}").format(e), _("Error"), wx.ICON_ERROR)

	def on_change_volume(self, event):
		"""
		Maneja el evento de cambiar el volumen a través del slider.
		"""
		try:
			volume = self.slider_volumen.GetValue()
			self.player.set_volume(volume)
		except Exception as e:
			gui.messageBox(str(e), _("Error al cambiar el volumen"), wx.ICON_ERROR)

	def on_change_speed(self, event):
		"""
		Maneja el evento de cambiar la velocidad a través del wx.Choice.
		"""
		try:
			speed_str = self.choice_velocidad.GetStringSelection()
			speed = float(speed_str)
			self.player.set_speed(speed * 50)  # Ajusta el rango de velocidad al rango de 0-100
		except Exception as e:
			gui.messageBox(str(e), _("Error al cambiar la velocidad"), wx.ICON_ERROR)

	def on_audio_finished(self):
		"""
		Maneja el evento cuando el audio finaliza la reproducción.
		"""
		try:
			self.btn_reproducir.SetLabel(_("Reproducir (F2)"))
		except Exception as e:
			gui.messageBox(str(e), _("Error al finalizar el audio"), wx.ICON_ERROR)

	def on_close(self, event):
		"""
		Cierra el reproductor y libera los recursos.
		"""
		try:
			self.player.close()
			self.Close()
		except Exception as e:
			gui.messageBox(str(e), _("Error al cerrar el diálogo"), wx.ICON_ERROR)
