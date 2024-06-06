# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Código de Gerardo Kessler
# Carga NVDA
import ui
import speech
# Carga Python
import threading
from time import sleep

def mute(time, msg=False):
	"""
	Función para romper la cadena de verbalización y callar al sintetizador durante el tiempo especificado.

	Args:
		time (float): Tiempo en segundos durante el cual el sintetizador estará silenciado.
		msg (str, optional): Mensaje opcional que se mostrará antes de silenciar el sintetizador. Por defecto es False.
	"""
	if msg:
		ui.message(msg)
		sleep(0.1)
	threading.Thread(target=killSpeak, args=(time,), daemon=True).start()

def killSpeak(time):
	"""
	Silencia el sintetizador por un tiempo específico.

	Args:
		time (float): Tiempo en segundos durante el cual el sintetizador estará silenciado.

	Nota:
		Si el modo de voz no es "talk", se cancela el proceso para evitar modificaciones en otros modos de voz.
	"""
	# Si el modo de voz no es talk, se cancela el proceso para evitar modificaciones en otros modos de voz
	if speech.getState().speechMode != speech.SpeechMode.talk:
		return
	speech.setSpeechMode(speech.SpeechMode.off)
	sleep(time)
	speech.setSpeechMode(speech.SpeechMode.talk)
