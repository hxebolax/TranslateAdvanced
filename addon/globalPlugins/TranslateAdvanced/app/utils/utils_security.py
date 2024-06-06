# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import globalPluginHandler
import globalVars
import addonHandler

# Carga traducción
addonHandler.initTranslation()

def disableInSecureMode(decoratedCls):
	"""
	Deshabilita la ejecución de un objeto o clase en modo seguro.
	
	:param decoratedCls: El objeto o clase que se desea deshabilitar en modo seguro.
	:return: Retorna globalPluginHandler.GlobalPlugin si la aplicación está en modo seguro, 
	         de lo contrario retorna el objeto o clase original (decoratedCls).
	"""
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else decoratedCls
