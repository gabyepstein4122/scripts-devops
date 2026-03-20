import os

def mantenimiento():
    print("🚀 Iniciando actualización completa...")
    comando = "sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt clean"
    os.system(comando)

def limpiar_cache():
    print("🧹 Realizando limpieza profunda de caché...")
    os.system("sudo du -sh /var/cache/apt/archives") 
    os.system("sudo apt clean")
    print("✨ Caché de paquetes purgada.")

if __name__ == "__main__":
    mantenimiento()
    limpiar_cache()
    print("\n✅ ¡Proceso terminado!")