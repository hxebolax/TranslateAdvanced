# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Este archivo está cubierto por la Licencia Pública General de GNU.
#
# Carga NVDA
import addonHandler
import logHandler
# Carga Python
import ctypes
import ctypes.wintypes
import ssl
import urllib.request
import urllib.error

# Carga traducción
addonHandler.initTranslation()

### Inicio certificados
class CERT_USAGE_MATCH(ctypes.Structure):
	_fields_ = (
		("dwType", ctypes.wintypes.DWORD),
		("cUsageIdentifier", ctypes.wintypes.DWORD),
		("rgpszUsageIdentifier", ctypes.c_void_p),  # LPSTR *
	)

class CERT_CHAIN_PARA(ctypes.Structure):
	_fields_ = (
		("cbSize", ctypes.wintypes.DWORD),
		("RequestedUsage", CERT_USAGE_MATCH),
		("RequestedIssuancePolicy", CERT_USAGE_MATCH),
		("dwUrlRetrievalTimeout", ctypes.wintypes.DWORD),
		("fCheckRevocationFreshnessTime", ctypes.wintypes.BOOL),
		("dwRevocationFreshnessTime", ctypes.wintypes.DWORD),
		("pftCacheResync", ctypes.c_void_p),  # LPFILETIME
		("pStrongSignPara", ctypes.c_void_p),  # PCCERT_STRONG_SIGN_PARA
		("dwStrongSignFlags", ctypes.wintypes.DWORD),
	)

def actualizar_certificados_raiz():
	"""
	Actualiza el almacén de certificados raíz de Windows utilizando una URL de Google.
	"""
	crypt = ctypes.windll.crypt32
	# URL a usar para obtener el certificado del servidor (Google)
	check_url = "https://www.google.com"

	# Crear un contexto SSL no verificado
	ssl_context = ssl._create_unverified_context()

	# Obtener el certificado del servidor
	with urllib.request.urlopen(check_url, context=ssl_context) as u:
		cert = u.fp.raw._sock.getpeercert(True)

	# Convertir a un formato usable por Windows
	cert_context = crypt.CertCreateCertificateContext(
		0x00000001,  # X509_ASN_ENCODING
		cert,
		len(cert)
	)

	# Configuración de parámetros de cadena
	chain_para = CERT_CHAIN_PARA(
		cbSize=ctypes.sizeof(CERT_CHAIN_PARA),
		RequestedUsage=CERT_USAGE_MATCH()
	)

	# Solicitar a Windows que construya una cadena de certificados, lo que activará una actualización de certificados raíz
	chain_context = ctypes.c_void_p()
	crypt.CertGetCertificateChain(
		None,
		cert_context,
		None,
		None,
		ctypes.byref(chain_para),
		0,
		None,
		ctypes.byref(chain_context)
	)

	# Liberar contextos de certificados
	crypt.CertFreeCertificateChain(chain_context)
	crypt.CertFreeCertificateContext(cert_context)

def realizar_solicitud_https(url):
	"""
	Intenta realizar una solicitud HTTPS a la URL proporcionada.
	Si falla por un error de verificación de certificado, intenta actualizar los certificados y reintentar.

	:param url: URL a la que se realizará la solicitud HTTPS.
	:return: Respuesta de la solicitud HTTPS.
	"""
	try:
		with urllib.request.urlopen(url) as response:
			return response.read()
	except urllib.error.URLError as e:
		if isinstance(e.reason, ssl.SSLCertVerificationError) and e.reason.reason == "CERTIFICATE_VERIFY_FAILED":
			actualizar_certificados_raiz()
			# Intentar nuevamente la solicitud
			with urllib.request.urlopen(url) as response:
				return response.read()
		else:
			raise
### Fin certificados

def is_connected():
	"""
	Comprueba si hay conexión a internet utilizando ctypes.

	:return: True si hay conexión, False en caso contrario.
	"""
	INTERNET_CONNECTION_OFFLINE = 0x20
	INTERNET_CONNECTION_CONFIGURED = 0x40
	INTERNET_CONNECTION_LAN = 0x02
	INTERNET_CONNECTION_MODEM = 0x01
	INTERNET_CONNECTION_PROXY = 0x04
	INTERNET_RAS_INSTALLED = 0x10
	INTERNET_CONNECTION_MODEM_BUSY = 0x08
	INTERNET_CONNECTION_ONLINE = 0x01

	# Cargar la biblioteca wininet.dll
	wininet = ctypes.WinDLL("wininet.dll")

	# Comprobar el estado de conexión
	flags = ctypes.c_int(0)
	connection = wininet.InternetGetConnectedState(ctypes.byref(flags), 0)

	# Analizar los indicadores de conexión
	if connection:
		return not bool(flags.value & INTERNET_CONNECTION_OFFLINE)
	else:
		return False
