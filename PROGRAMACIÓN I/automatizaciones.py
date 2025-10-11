# automatizaciones.py
luces_on = "18"
luces_off = "23"

def activar_modo_ahorro(dispositivos, usuario):
    print("\nActivando Modo Ahorro de Energía...")
    apagados = 0
    for d in dispositivos:
        if d["tipo"] not in ["cámara", "alarma"]:
            d["estado"] = False
            apagados += 1
    print(f"Se apagaron {apagados} dispositivo(s) no esenciales.")
    print #lorenapereyra
    #simular de datos en memoria
    usuarios =[]
    dispositivos = []
    automatizaciones =[f"Encender luces a las {luces_on}", f"Apagar luces a las {luces_off}"]
    consultar_automatizaciones(automatizaciones)
    
def consultar_automatizaciones(automatizaciones):
    print("\n---automatizaciones activas---")
    if not automatizaciones:
        print("no hay automatizaciones activas.")
        return #salimos de la funcion si no hay automatizaciones
    for auto in automatizaciones:
        print (f"- {auto}")

def configurar_modo_ahorro(hora_on, hora_off):
    global luces_on
    global luces_off
    luces_on = hora_on
    luces_off = hora_off
        
       

