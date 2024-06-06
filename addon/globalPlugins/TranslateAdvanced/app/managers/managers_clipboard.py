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
import threading

# Carga traducción
addonHandler.initTranslation()

# Definición de tipos y constantes
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

WM_CLIPBOARDUPDATE = 0x031D
CF_UNICODETEXT = 13

class ClipboardMonitor:
	"""
	Clase para monitorear cambios en el portapapeles en tiempo real.
	"""

	class WNDCLASS(ctypes.Structure):
		_fields_ = [("style", ctypes.c_uint),
					("lpfnWndProc", ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.wintypes.HWND, ctypes.c_uint, ctypes.wintypes.WPARAM, ctypes.wintypes.LPARAM)),
					("cbClsExtra", ctypes.c_int),
					("cbWndExtra", ctypes.c_int),
					("hInstance", ctypes.wintypes.HINSTANCE),
					("hIcon", ctypes.wintypes.HICON),
					("hCursor", ctypes.wintypes.HANDLE),
					("hbrBackground", ctypes.wintypes.HBRUSH),
					("lpszMenuName", ctypes.wintypes.LPCWSTR),
					("lpszClassName", ctypes.wintypes.LPCWSTR)]

	def __init__(self, callback=None):
		"""
		Inicializa el monitor del portapapeles.
		
		:param callback: Función a llamar cuando el portapapeles cambie.
		"""
		self.callback = callback
		self.running = False
		self.hwnd = None
		self._ignore_next_change = False

	def start(self):
		"""
		Inicia el monitor del portapapeles.
		"""
		if not self.running:
			self.running = True
			self._monitor_thread = threading.Thread(target=self._run, daemon=True)
			self._monitor_thread.start()

	def stop(self):
		"""
		Detiene el monitor del portapapeles.
		"""
		if self.running:
			self.running = False
			user32.RemoveClipboardFormatListener(self.hwnd)
			user32.DestroyWindow(self.hwnd)
			self._monitor_thread.join()

	def _run(self):
		"""
		Función que se ejecuta en un hilo separado para monitorear el portapapeles.
		"""
		wndclass = self.WNDCLASS()
		hinst = kernel32.GetModuleHandleW(None)
		wndclass.lpfnWndProc = self._get_wnd_proc()
		wndclass.hInstance = hinst
		wndclass.lpszClassName = "ClipboardMonitor"

		if not user32.RegisterClassW(ctypes.byref(wndclass)):
			raise RuntimeError(_("Error registrando clase de ventana"))

		self.hwnd = user32.CreateWindowExW(
			0, wndclass.lpszClassName, "ClipboardMonitor", 0, 0, 0, 0, 0, 0, 0, hinst, None
		)
		if not self.hwnd:
			raise RuntimeError(_("Error creando ventana"))

		if not user32.AddClipboardFormatListener(self.hwnd):
			raise RuntimeError(_("Error agregando listener de portapapeles"))

		msg = ctypes.wintypes.MSG()
		while self.running:
			while user32.PeekMessageW(ctypes.byref(msg), 0, 0, 0, 1):
				user32.TranslateMessage(ctypes.byref(msg))
				user32.DispatchMessageW(ctypes.byref(msg))

	def _get_wnd_proc(self):
		"""
		Obtiene la función de procesamiento de ventana.
		
		:return: Función WndProc.
		"""
		def wnd_proc(hwnd, msg, wparam, lparam):
			if msg == WM_CLIPBOARDUPDATE:
				self._on_clipboard_change()
			return user32.DefWindowProcW(hwnd, msg, wparam, lparam)
		return ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.wintypes.HWND, ctypes.c_uint, ctypes.wintypes.WPARAM, ctypes.wintypes.LPARAM)(wnd_proc)

	def _on_clipboard_change(self):
		"""
		Callback para manejar cambios en el portapapeles.
		"""
		if self._ignore_next_change:
			self._ignore_next_change = False
			return

		text = self._get_clipboard_text()
		if text is not None:
			self.callback(text)

	def _get_clipboard_text(self):
		"""
		Obtiene el texto actual del portapapeles.
		
		:return: El texto del portapapeles o None si no hay texto disponible.
		"""
		user32.OpenClipboard(0)
		handle = user32.GetClipboardData(CF_UNICODETEXT)
		if handle:
			data = ctypes.c_wchar_p(kernel32.GlobalLock(handle)).value
			kernel32.GlobalUnlock(handle)
		else:
			data = None
		user32.CloseClipboard()
		return data

	def get_clipboard_text(self):
		"""
		Obtiene el texto actual del portapapeles.
		
		:return: El texto del portapapeles o None si no hay texto disponible.
		"""
		return self._get_clipboard_text()

	def set_clipboard_text(self, text):
		"""
		Establece el texto en el portapapeles sin activar el callback.
		
		:param text: El texto a establecer en el portapapeles.
		"""
		self._ignore_next_change = True
		user32.OpenClipboard(0)
		user32.EmptyClipboard()
		hglobal = kernel32.GlobalAlloc(0x2000, (len(text) + 1) * ctypes.sizeof(ctypes.c_wchar))
		lock = kernel32.GlobalLock(hglobal)
		ctypes.cdll.msvcrt.wcscpy(ctypes.c_wchar_p(lock), text)
		kernel32.GlobalUnlock(hglobal)
		user32.SetClipboardData(CF_UNICODETEXT, hglobal)
		user32.CloseClipboard()

	def clear_clipboard(self):
		"""
		Limpia el contenido del portapapeles.
		"""
		self._ignore_next_change = True
		user32.OpenClipboard(0)
		user32.EmptyClipboard()
		user32.CloseClipboard()
