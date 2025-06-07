# automatizaciones.py
def activar_modo_ahorro(dispositivos, usuario):
    print("\nActivando Modo Ahorro de Energía...")
    apagados = 0
    for d in dispositivos:
        if d["usuario_id"] == usuario["id"] and d["tipo"] not in ["cámara", "alarma"]:
            d["estado"] = False
            apagados += 1
    print(f"Se apagaron {apagados} dispositivo(s) no esenciales.")
    print #lorenapereyra