import os
import subprocess
import sys

def ejecutar(comando, mensaje):
    print(f">> {mensaje}...")
    try:
        subprocess.run(comando, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(" [OK]")
    except subprocess.CalledProcessError:
        print(f" [ERROR] No se pudo completar: {mensaje}")

def verificar_versiones():
    print("\n=== REPORTE DE VERSIONES INSTALADAS ===")
    
    # Lista de comandos para pedir la versión a cada herramienta
    herramientas = {
        "Git": "git --version",
        "VS Code": "code --version | head -n 1",
        "Docker": "docker --version",
        "Terraform": "terraform --version | head -n 1",
        "Ansible": "ansible --version | head -n 1",
        "Node": "node -v",
        "NPM": "npm -v",
        "Python": "python3 --version"
    }

    for nombre, comando in herramientas.items():
        try:
            # Ejecutamos el comando y capturamos el texto que devuelve
            resultado = subprocess.check_output(comando, shell=True, text=True).strip()
            print(f"{nombre}: {resultado}")
        except:
            print(f"{nombre}: No instalada o con error")

def instalar_todo():
    print("=== Iniciando Instalación de Laboratorio DevOps ===")

    # 1. Actualizar repositorios
    ejecutar("sudo apt-get update", "Actualizando lista de paquetes")

    # 2. Git
    ejecutar("sudo apt-get install -y git", "Instalando Git")

    # 3. VS Code
    ejecutar("sudo snap install --classic code", "Instalando VS Code")

    # 4. Docker
    ejecutar("sudo apt-get install -y docker.io && sudo systemctl enable --now docker", "Instalando Docker")
    ejecutar(f"sudo usermod -aG docker {os.getlogin()}", "Configurando permisos de Docker")

    # 5. Terraform
    cmd_tf = (
        "wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg && "
        "echo \"deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main\" | sudo tee /etc/apt/sources.list.d/hashicorp.list && "
        "sudo apt-get update && sudo apt-get install -y terraform"
    )
    ejecutar(cmd_tf, "Instalando Terraform")

    # 6. Ansible
    ejecutar("sudo apt-get install -y ansible", "Instalando Ansible")

    # 7. Postman
    ejecutar("sudo snap install postman", "Instalando Postman")

    # 8. Node.js y NPM
    ejecutar("sudo apt-get install -y nodejs npm", "Instalando Node.js y NPM")

    # --- NUEVO: Verificación final ---
    verificar_versiones()

    print("\n===============================================")
    print("Instalación completada. Reiniciá la sesión para aplicar cambios.")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Error: Corré el script con sudo (sudo python3 setup_devops.py)")
        sys.exit(1)
    instalar_todo()
