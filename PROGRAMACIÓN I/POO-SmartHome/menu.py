from gestion_usuarios import GestionDeUsuarios
from gestion_dispositivos import GestionDispositivos


def mostrar_menu_principal():
    print("\n=== SmartHome Solutions ===")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    return input("Seleccione una opción: ")

def mostrar_menu_usuario_admin(nombre, rol):
    print(f"\nBienvenido/a {nombre} ({rol})!")
    print("1. Gestionar dispositivos")
    print("2. Cambiar de rol de un usuario")
    print("3. Cerrar sesión")
    return input("Seleccione una opción: ")

def mostrar_menu_usuario_estandar(nombre):
    print(f"\nBienvenido/a {nombre}")
    print("1. Consultar los datos personales")
    print("2. Consultar dispositivos")
    print("3. Cerrar sesión")
    return input("Seleccione una opción: ")

def mostrar_menu_dispositivos():
    print("\n--- Gestión de Dispositivos ---")
    print("1. Listar dispositivos")
    print("2. Agregar dispositivo")
    print("3. Eliminar dispositivo")
    print("4. Activar/desactivar dispositivo")
    print("5. Volver al menú anterior")
    return input("Seleccione una opción: ")

def mostrar_menu_cambio_estado_dispositivo():
    print("\nDesea:")
    print("1. Activar dispositivos")
    print("2. Desactivar dispositivo")
    return input("Seleccione una opción: ")

gestor_usuario = GestionDeUsuarios([])
gestor_dispositivos = GestionDispositivos([])

def gestionar_dispositivos():
    opcion = ""
    while opcion != "5":
        opcion = mostrar_menu_dispositivos()
        match opcion:
            case "1":
                gestor_dispositivos.mostrar_dispositivos()
            case "2":
                gestor_dispositivos.crear_dispositivo()
            case "3":
                gestor_dispositivos.eliminar_dispositivo_por_nombre()
            case "4":
                activar_desactivar_dispositivo()
            case "5":
                print("Volviendo al menú anterior...")
            case _:
                print("Opción inválida. Intente nuevamente.")
    
def activar_desactivar_dispositivo():
    opcion = ""
    while opcion != "1" and opcion != "2":
        opcion = mostrar_menu_cambio_estado_dispositivo()
        match opcion:
            case "1":
                gestor_dispositivos.cambiar_estado_dispositivo(True)
            case "2":
                gestor_dispositivos.cambiar_estado_dispositivo(False)
            case _:
                print("Opción inválida. Intente nuevamente.")

    
def menu_usuario_admin(usuario):
    global autenticado
    autenticado = usuario
    sesion_activa = True
    print("entro sesion activa")
    while sesion_activa:
        opcion = mostrar_menu_usuario_admin(usuario.get_nombre(), usuario.get_rol())
        if opcion == "1":
            gestionar_dispositivos()
        elif opcion == "2":
            gestor_usuario.modificar_rol_usuario()
        elif opcion == "3":
            autenticado = None
            print("Sesión cerrada.")
            sesion_activa = False
        else:
            print("Opción inválida.")
    
def menu_usuario_estandar(usuario):
    global autenticado
    autenticado = usuario
    sesion_activa = True
    print("entro sesion activa")
    while sesion_activa:
        opcion = mostrar_menu_usuario_estandar(usuario.get_nombre())
        if opcion == "1":
            print("Consultando los datos personales...\n")
            usuario.mostrar_datos()
        elif opcion == "2":
            print("Consultando dispositivos...\n")
            gestor_dispositivos.mostrar_dispositivos()
        elif opcion == "3":
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
            gestor_usuario.registrar_usuario()
        elif opcion == "2":
            usuario = gestor_usuario.iniciar_sesion()
            if usuario != None:
                if usuario.get_rol() == "admin":
                    menu_usuario_admin(usuario)
                else:
                    menu_usuario_estandar(usuario)
        elif opcion == "3":
            print("¡Hasta luego!")
            app_activa = False
        else:
            print("Opción inválida.")

