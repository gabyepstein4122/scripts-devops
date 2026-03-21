import os
from datetime import datetime

log_file = "/home/gaboa/Scripts/maintenance.log"

def new_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def maintenance():
    print("\n 1. 🚀 Starting full update...")
    command = "sudo apt update && sudo apt upgrade -y"
    os.system(command)

def limpiar_cache():
    print("\n 2. ⏳ Checking package cache space...")
    os.system("sudo du -sh /var/cache/apt/archives") 
    
    print("🧹 Cleaning temporary package files...")
    os.system("sudo apt autoremove -y && sudo apt clean")
    
    print("✅ Cache cleared and system optimized.")

if __name__ == "__main__":
    maintenance()
    limpiar_cache()
    print("\n✅ Process completed!")