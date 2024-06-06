# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
import api
import textInfos

# Carga traducción
addonHandler.initTranslation()

def getSelectedText(obj):
	"""
	Obtiene el texto seleccionado en el objeto de la interfaz de usuario actual.

	:param obj: El objeto de la interfaz de usuario del cual se desea obtener el texto seleccionado.
	:return: Un diccionario con la clave 'success' que indica si la operación fue exitosa o no.
	         Si 'success' es True, incluye la clave 'data' con el texto seleccionado.
	         Si 'success' es False, incluye la clave 'data' con el valor None.
	"""
	try:
		info = obj.makeTextInfo(textInfos.POSITION_SELECTION)
		if info and not info.isCollapsed:
			return {'success': True, 'data': info.text}
	except (RuntimeError, NotImplementedError) as e:
		#logHandler.log.error(_("Error al obtener el texto seleccionado: {}").format(str(e)))
		return {'success': False, 'data': None}
	
	return {'success': False, 'data': None}
