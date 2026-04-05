import os

def obtener_datos(ruta):
    try:
        with open(ruta, 'r') as ficha:
            return ficha.read().strip()
    except FileNotFoundError:
        return None

def reporte_bateria(): 
    raiz = "/sys/class/power_supply/BAT0/"

    # Extraemos la información
    estado = obtener_datos(raiz + "status")
    capacidad = obtener_datos(raiz + "capacity")
    salud = obtener_datos(raiz + "capacity_level")

    # Traduccion de datos
    traductor = {
        "Discharging": "🔋 Usando batería",
        "Charging": "⚡ Cargando",
        "Full": "✅ Batería llena",
        "Not charging": "🔌 Conectado (sin cargar)"
    }

    # Resultados en pantalla
    print("-" * 30)
    print("📋 REPORTE DE TU BATERÍA")
    print("-" * 30)
    print(f"Estado actual: {traductor.get(estado, 'Desconocido')}")
    print(f"Nivel de carga: {capacidad}%")
    print(f"Salud general: {salud}")
    print("-" * 30)

    # Arranque del programa
if __name__ == "__main__":
	reporte_bateria()
