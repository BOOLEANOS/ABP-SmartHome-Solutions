from dao.usuario_dao import registrar_usuario, iniciar_sesion, modificar_rol_usuario, datos_usuario
from dao.dispositivo_dao import obtener_dispositivos_usuario, crear_dispositivo, eliminar_dispositivo, cambiar_estado_dispositivo
from dao.automatizacion_dao import activar_modo_ahorro
from conn.db_conn import crear_conexion

# Variable global para controlar la autenticación
autenticado = None

def mostrar_menu_principal():
    print("\n=== SmartHome Solutions ===")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    return input("Seleccione una opción: ")

def mostrar_menu_usuario_admin(nombre, rol):
    print(f"\nBienvenido/a {nombre} ({rol})!")
    print("1. Gestionar dispositivos")
    print("2. Activar Modo Ahorro de Energía")
    print("3. Modificar rol de usuario")
    print("4. Cerrar sesión")
    return input("Seleccione una opción: ")

def mostrar_menu_usuario_estandar(nombre):
    print(f"\nBienvenido/a {nombre}")
    print("1. Consultar los datos personales")
    print("2. Menu modo ahorro de energía")
    print("3. Consultar dispositivos")
    print("4. Cerrar sesión")
    return input("Seleccione una opción: ")

def mostrar_menu_dispositivos():
    print("\n--- Gestión de Dispositivos ---")
    print("1. Listar dispositivos")
    print("2. Agregar dispositivo")
    print("3. Eliminar dispositivo")
    print("4. Buscar dispositivo")
    print("5. Activar/desactivar dispositivo")
    print("6. Volver al menú anterior")
    return input("Seleccione una opción: ")

def mostrar_menu_cambio_estado_dispositivo():
    print("\nDesea:")
    print("1. Activar dispositivos")
    print("2. Desactivar dispositivo")
    return input("Seleccione una opción: ")

def mostrar_menu_automatizaciones():
    print("\n--- Gestión de modo ahorro de energía ---")
    print("1. Activar automatización")
    print("2. Configurar automatización")
    print("3. Volver al menú anterior")
    return input("Seleccione una opción: ")

def buscar_dispositivo_por_nombre(usuario_id):
    """Función para buscar dispositivo por nombre"""
    nombre = input("Ingrese el nombre del dispositivo a buscar: ").strip()
    
    dispositivos = obtener_dispositivos_usuario(usuario_id)
    encontrados = []
    
    for d in dispositivos:
        if nombre.lower() in d["nombre"].lower():
            encontrados.append(d)
    
    if encontrados:
        print(f"\nDispositivos encontrados ({len(encontrados)}):")
        for d in encontrados:
            estado_str = "Encendido" if d["estado"] else "Apagado"
            print(f"ID: {d['id']}, Nombre: {d['nombre']}, Ubicación: {d['ubicacion']}, Estado: {estado_str}, Tipo: {d['tipo']}")
    else:
        print("No se encontraron dispositivos con ese nombre.")

def gestionar_automatizacion(usuario):
    opcion = ""
    while opcion != "3":
        opcion = mostrar_menu_automatizaciones()
        if opcion == "1":
            activar_modo_ahorro(usuario["id"])
        elif opcion == "2":
            print("Configurando modo ahorro de energía...")
            horaOn = input("Ingrese la hora para encender las luces: ")
            horaOff = input("Ingrese la hora para apagar las luces: ")
            print(f"Modo ahorro configurado: Encender a las {horaOn}, Apagar a las {horaOff}")
        elif opcion == "3":
            print("Volviendo al menú anterior...")
        else:
            print("Opción inválida. Intente nuevamente.")

def gestionar_dispositivos(usuario):
    opcion = ""
    while opcion != "6":
        opcion = mostrar_menu_dispositivos()
        if opcion == "1":
            dispositivos = obtener_dispositivos_usuario(usuario["id"])
            if dispositivos:
                print("\nDispositivos registrados:")
                for d in dispositivos:
                    estado_str = "Encendido" if d["estado"] else "Apagado"
                    print(f"ID: {d['id']}, Nombre: {d['nombre']}, Ubicación: {d['ubicacion']}, Estado: {estado_str}, Tipo: {d['tipo']}")
            else:
                print("No hay dispositivos registrados.")
        elif opcion == "2":
            crear_dispositivo(usuario["id"])
        elif opcion == "3":
            eliminar_dispositivo(usuario["id"])
        elif opcion == "4":
            buscar_dispositivo_por_nombre(usuario["id"])
        elif opcion == "5":
            activar_desactivar_dispositivo(usuario["id"])
        elif opcion == "6":
            print("Volviendo al menú anterior...")
        else:
            print("Opción inválida.")
    
def activar_desactivar_dispositivo(usuario_id):
    opcion = ""
    while opcion != "1" and opcion != "2":
        opcion = mostrar_menu_cambio_estado_dispositivo()
        if opcion == "1":
            cambiar_estado_dispositivo(usuario_id, True)
        elif opcion == "2":
            cambiar_estado_dispositivo(usuario_id, False)
        else:
            print("Opción inválida. Intente nuevamente.")

def mostrar_dispositivos_usuario(usuario_id):
    """Función para mostrar dispositivos del usuario"""
    dispositivos = obtener_dispositivos_usuario(usuario_id)
    if dispositivos:
        print("\nDispositivos registrados:")
        for d in dispositivos:
            estado_str = "Encendido" if d["estado"] else "Apagado"
            print(f"ID: {d['id']}, Nombre: {d['nombre']}, Ubicación: {d['ubicacion']}, Estado: {estado_str}, Tipo: {d['tipo']}")
    else:
        print("No hay dispositivos registrados.")

def menu_usuario_admin(usuario):
    global autenticado
    autenticado = usuario
    sesion_activa = True
    
    while sesion_activa:
        opcion = mostrar_menu_usuario_admin(usuario["nombre"], usuario["rol"])
        if opcion == "1":
            gestionar_dispositivos(usuario)
        elif opcion == "2":
            activar_modo_ahorro(usuario["id"])
        elif opcion == "3":
            email = input("Email del usuario a modificar: ")
            print("\nRoles disponibles:")
            print("1. admin")
            print("2. estandar")
            nuevo_rol_id = input("Seleccione el ID del nuevo rol (1 o 2): ")
            modificar_rol_usuario(email, nuevo_rol_id)
        elif opcion == "4":
            autenticado = None
            print("Sesión cerrada.")
            sesion_activa = False
        else:
            print("Opción inválida.")
    
def menu_usuario_estandar(usuario):
    global autenticado
    autenticado = usuario
    sesion_activa = True
    
    while sesion_activa:
        opcion = mostrar_menu_usuario_estandar(usuario["nombre"])
        if opcion == "1":
            print("Consultando los datos personales...\n")
            datos_usuario(usuario)
        elif opcion == "2":
            gestionar_automatizacion(usuario)
        elif opcion == "3":
            print("Consultando dispositivos...\n")
            mostrar_dispositivos_usuario(usuario["id"])
        elif opcion == "4":
            autenticado = None
            sesion_activa = False
            print("Sesión cerrada.")
        else:
            print("Opción inválida.")

def menu_principal():
    app_activa = True

    while app_activa:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            email = input("Ingrese su email: ")
            password = input("Cree una contraseña: ")
            registrar_usuario(nombre, email, password)
        elif opcion == "2":
            email = input("Email: ")
            password = input("Contraseña: ")
            usuario = iniciar_sesion(email, password)
            if usuario:  # Solo si el login fue exitoso
                if usuario["rol"] == "admin":
                    menu_usuario_admin(usuario)
                else:
                    menu_usuario_estandar(usuario)
        elif opcion == "3":
            print("¡Hasta luego!")
            app_activa = False
        else:
            print("Opción inválida.")

# Ejecutar la aplicación
if __name__ == "__main__":
    # Verificar conexión a la base de datos
    conexion = crear_conexion()
    if conexion:
        print("✓ Conectado a la base de datos MySQL")
        conexion.close()
    else:
        print("⚠ No se pudo conectar a la base de datos")
    
    menu_principal()