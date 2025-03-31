import subprocess

def ejecutar(comando):
	try:
		resultado = subprocess.check_output(comando, shell=True, text=True).strip()
		return resultado
	except subprocess.CalledProcessError:
		return ""

def esta_en_git():
	return ejecutar("git rev-parse --is-inside-work-tree") == "true"

def main():
	if not esta_en_git():
		print("❌ No estás dentro de un repositorio Git.")
		return

	rama = ejecutar("git symbolic-ref --short HEAD")
	print("🔄 Verificando estado remoto...")
	subprocess.call("git fetch", shell=True)

	adelantado = ejecutar(f"git rev-list --count {rama}..origin/{rama}")
	retrasado = ejecutar(f"git rev-list --count origin/{rama}..{rama}")

	if adelantado == "0" and retrasado == "0":
		print(f"✅ El repositorio está completamente actualizado con origin/{rama}.")
		return

	if adelantado != "0":
		print(f"📌 Tu rama local está adelantada por {adelantado} commit(s).")
		resp = input("¿Querés hacer PUSH? (s/n): ")
		if resp.lower() == "s":
			subprocess.call(f"git push origin {rama}", shell=True)

	if retrasado != "0":
		print(f"📥 El repositorio remoto tiene {retrasado} commit(s) que no tenés en local.")
		resp = input("¿Querés hacer PULL? (s/n): ")
		if resp.lower() == "s":
			subprocess.call(f"git pull origin {rama}", shell=True)

if __name__ == "__main__":
	main()
