# dispositivos.py
def menu_dispositivos(dispositivos, usuario):
    while True:
        print("\n--- Gestión de Dispositivos ---")
        print("1. Listar dispositivos")
        print("2. Agregar dispositivo")
        print("3. Eliminar dispositivo")
        print("4. Volver al menú anterior")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_dispositivos(dispositivos, usuario)
        elif opcion == "2":
            agregar_dispositivo(dispositivos, usuario)
        elif opcion == "3":
            eliminar_dispositivo(dispositivos, usuario)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def listar_dispositivos(dispositivos, usuario):
    print("\nDispositivos registrados:")
    encontrados = False
    for d in dispositivos:
        if d["usuario_id"] == usuario["id"]:
            print(f"- {d['nombre']} ({d['tipo']}), Estado: {'Encendido' if d['estado'] else 'Apagado'}")
            encontrados = True
    if not encontrados:
        print("No hay dispositivos registrados.")

def agregar_dispositivo(dispositivos, usuario):
    nombre = input("Nombre del dispositivo: ")
    tipo = input("Tipo (luz, cámara, termostato, etc.): ")
    nuevo = {
        "id": len(dispositivos) + 1,
        "nombre": nombre,
        "tipo": tipo,
        "estado": True,
        "usuario_id": usuario["id"]
    }
    dispositivos.append(nuevo)
    print("Dispositivo agregado con éxito.")

def eliminar_dispositivo(dispositivos, usuario):
    nombre = input("Nombre del dispositivo a eliminar: ")
    for d in dispositivos:
        if d["usuario_id"] == usuario["id"] and d["nombre"] == nombre:
            dispositivos.remove(d)
            print("Dispositivo eliminado.")
            return
    print("Dispositivo no encontrado.")
