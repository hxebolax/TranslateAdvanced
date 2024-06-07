import os
import json
import zipfile

class GestorIdiomas:
	"""
	Clase para gestionar idiomas y comprimir carpetas en el directorio translates.
	"""
	def __init__(self, translates_dir='.'):
		self.translates_dir = translates_dir
		self.languages_file = os.path.join(self.translates_dir, 'languages.json')
		if not os.path.exists(self.languages_file):
			with open(self.languages_file, 'w') as file:
				json.dump({}, file, indent='\t')

	def limpiar_pantalla(self):
		"""
		Limpia la pantalla de la terminal.
		"""
		if os.name == 'nt':  # Windows
			os.system('cls')
		else:  # Linux y macOS
			os.system('clear')

	def pausar_y_limpiar(self):
		"""
		Pausa para que el usuario vea el resultado y luego limpia la pantalla.
		"""
		input("\nPresione Enter para continuar...")
		self.limpiar_pantalla()

	def crear_zip_de_carpeta(self, carpeta):
		"""
		Crea un archivo .zip para la carpeta dada.
		
		:param carpeta: Nombre de la carpeta dentro de translates
		"""
		try:
			ruta_carpeta = os.path.join(self.translates_dir, carpeta)
			archivo_zip = os.path.join(self.translates_dir, f"{carpeta}.zip")
			
			with zipfile.ZipFile(archivo_zip, 'w') as zipf:
				for root, dirs, files in os.walk(ruta_carpeta):
					for file in files:
						ruta_completa = os.path.join(root, file)
						# Calcula la ruta relativa sin incluir la carpeta raíz
						ruta_relativa = os.path.relpath(ruta_completa, ruta_carpeta)
						zipf.write(ruta_completa, ruta_relativa)
			print(f"Creado: {archivo_zip}")
		except Exception as e:
			print(f"Error al crear el zip para la carpeta {carpeta}: {e}")

	def cargar_idiomas(self):
		"""
		Carga el archivo de idiomas JSON.
		
		:return: Diccionario de idiomas
		"""
		try:
			with open(self.languages_file, 'r') as file:
				return json.load(file)
		except Exception as e:
			print(f"Error al cargar el archivo de idiomas: {e}")
			return {}

	def guardar_idiomas(self, idiomas):
		"""
		Guarda el diccionario de idiomas en el archivo JSON.
		
		:param idiomas: Diccionario de idiomas a guardar
		"""
		try:
			with open(self.languages_file, 'w') as file:
				json.dump(idiomas, file, indent='\t')
		except Exception as e:
			print(f"Error al guardar el archivo de idiomas: {e}")

	def agregar_idioma(self):
		"""
		Agrega un nuevo idioma al archivo JSON.
		"""
		try:
			idioma = input("Ingrese el código del idioma (e.g., pt-br, en, fr): ")
			idiomas = self.cargar_idiomas()
			
			if idioma in idiomas:
				print(f"El idioma {idioma} ya existe.")
			else:
				idiomas[idioma] = 1
				self.guardar_idiomas(idiomas)
				print(f"Idioma {idioma} agregado con versión 1.")
		except Exception as e:
			print(f"Error al agregar el idioma: {e}")
		self.pausar_y_limpiar()

	def actualizar_idioma(self):
		"""
		Actualiza la versión de un idioma en el archivo JSON.
		"""
		try:
			idioma = input("Ingrese el código del idioma a actualizar: ")
			idiomas = self.cargar_idiomas()
			
			if idioma in idiomas:
				print(f"Versión actual del idioma {idioma}: {idiomas[idioma]}")
				nueva_version = int(input("Ingrese la nueva versión: "))
				idiomas[idioma] = nueva_version
				self.guardar_idiomas(idiomas)
				print(f"Idioma {idioma} actualizado a versión {nueva_version}.")
			else:
				print(f"El idioma {idioma} no existe.")
		except Exception as e:
			print(f"Error al actualizar el idioma: {e}")
		self.pausar_y_limpiar()

	def eliminar_idioma(self):
		"""
		Elimina un idioma del archivo JSON.
		"""
		try:
			idioma = input("Ingrese el código del idioma a eliminar: ")
			idiomas = self.cargar_idiomas()
			
			if idioma in idiomas:
				del idiomas[idioma]
				self.guardar_idiomas(idiomas)
				print(f"Idioma {idioma} eliminado.")
			else:
				print(f"El idioma {idioma} no existe.")
		except Exception as e:
			print(f"Error al eliminar el idioma: {e}")
		self.pausar_y_limpiar()

	def comprimir_carpetas(self):
		"""
		Comprime todas las carpetas dentro de translates.
		"""
		try:
			for carpeta in os.listdir(self.translates_dir):
				ruta_carpeta = os.path.join(self.translates_dir, carpeta)
				if os.path.isdir(ruta_carpeta) and carpeta != os.path.basename(self.languages_file):
					self.crear_zip_de_carpeta(carpeta)
		except Exception as e:
			print(f"Error al comprimir las carpetas: {e}")
		self.pausar_y_limpiar()

	def mostrar_menu(self):
		"""
		Muestra el menú principal y maneja las opciones del usuario.
		"""
		while True:
			print("\nMenú de opciones:")
			print("1. Agregar idioma")
			print("2. Actualizar idioma")
			print("3. Eliminar idioma")
			print("4. Comprimir carpetas")
			print("0. Salir")
			
			opcion = input("Seleccione una opción: ")
			
			if opcion == '1':
				self.agregar_idioma()
			elif opcion == '2':
				self.actualizar_idioma()
			elif opcion == '3':
				self.eliminar_idioma()
			elif opcion == '4':
				self.comprimir_carpetas()
			elif opcion == '0':
				print("Saliendo...")
				break
			else:
				print("Opción no válida. Intente de nuevo.")
				self.pausar_y_limpiar()

if __name__ == "__main__":
	gestor = GestorIdiomas()
	gestor.mostrar_menu()
