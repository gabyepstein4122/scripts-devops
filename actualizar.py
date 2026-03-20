import os

def mantenimiento():
    print("\n 1. 🚀 Iniciando actualización completa...")
    comando = "sudo apt update && sudo apt upgrade -y"
    os.system(comando)

def limpiar_cache():
    print("\n 2. ⏳ Verificando espacio en caché de paquetes...")
    os.system("sudo du -sh /var/cache/apt/archives") 
    
    print("🧹 Limpiando archivos temporales de paquetes...")
    os.system("sudo apt autoremove -y && sudo apt clean")
    
    print("✅ Caché purgada y sistema optimizado.")

if __name__ == "__main__":
    mantenimiento()
    limpiar_cache()
    print("\n✅ ¡Proceso terminado!")