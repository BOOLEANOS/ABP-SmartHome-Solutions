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
    #simular de datos en memoria
    usuarios =[]
    dispositivos = []
    automatizaciones =["encender luces a las 18" "apagar  luces a las 23"]
    def consultar_automatizaciones(automatizacion):
        print("/n---automatizaciones activas---")
        if not automatizaciones:
            print("no hay automatizaciones activas.")
            return #salimos de la funcion si no hay automatizaciones
        for auto in automatizaciones:
            print (f"-{auto}")
        
       

