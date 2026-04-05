import subprocess
import os

# Configuración basada en tus resultados
INTERFACE = "wlp3s0"
ROUTER_IP = "192.168.100.1"
INTERNET_CHECK = "8.8.8.8"

def check_ping(ip):
    try:
        # Tira 2 pings rápidos
        subprocess.check_output(f"ping -c 2 -W 1 {ip}", shell=True)
        return True
    except:
        return False

def reporte_red():
    print("=== 🛰️  DIAGNÓSTICO DE RED CLARO - CÓRDOBA ===")
    
    # 1. ¿Está la placa de red activa?
    status = subprocess.getoutput(f"cat /sys/class/net/{INTERFACE}/operstate")
    if status == "up":
        print(f"[OK] Placa {INTERFACE} encendida.")
    else:
        print(f"[ERROR] La placa {INTERFACE} está apagada o desconectada.")
        return

    # 2. ¿Llego al módem de Claro?
    if check_ping(ROUTER_IP):
        print(f"[OK] Conexión al router ({ROUTER_IP}) exitosa.")
    else:
        print(f"[ALERTA] No llego al router. Revisá el Wi-Fi o el cable.")

    # 3. ¿Tengo salida a Internet?
    if check_ping(INTERNET_CHECK):
        print(f"[OK] Salida a Internet confirmada (Google DNS).")
    else:
        print(f"[ALERTA] Sin internet. El problema parece ser el proveedor (Claro).")

if __name__ == "__main__":
    reporte_red()
