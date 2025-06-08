# dispositivos.py

def mostrar_dispositivos_usuario(dispositivos, usuario):
    print("\nDispositivos registrados:")

    if not dispositivos:
        print("No hay dispositivos registrados.")
        return

    for idx, d in enumerate(dispositivos, 1):
        estado = "Encendido" if d["estado"] else "Apagado"
        print(f"{idx}. {d['nombre']} ({d['tipo']}) - Estado: {estado}")

def crear_dispositivo(dispositivos, usuario):
    nombre = input("Nombre del dispositivo: ").strip()
    tipo = input("Tipo (luz, cámara, termostato, etc.): ").strip()

    if not nombre or not tipo:
        print("Nombre y tipo son obligatorios.")
        return

    nuevo_dispositivo = {
        "id": len(dispositivos) + 1,
        "nombre": nombre,
        "tipo": tipo,
        "estado": True,
        "usuario_id": usuario["id"]
    }
    dispositivos.append(nuevo_dispositivo)
    print(f" Dispositivo '{nombre}' agregado correctamente.")

def eliminar_dispositivo_por_nombre(dispositivos, usuario):
    nombre = input("Ingrese el nombre del dispositivo a eliminar: ").strip()

    for d in dispositivos:
        if d["nombre"].lower() == nombre.lower():
            dispositivos.remove(d)
            print(f"Dispositivo '{nombre}' eliminado.")
            return

    print("Dispositivo no encontrado o no pertenece a su cuenta.")