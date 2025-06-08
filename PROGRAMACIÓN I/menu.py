from usuarios import registrar_usuario, iniciar_sesion, modificar_rol_usuario
from dispositivos import *
from automatizaciones import activar_modo_ahorro


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
    print("3. Cerrar sesión")
    return input("Seleccione una opción: ")

def mostrar_menu_usuario_estandar(nombre, rol):
    print(f"\nBienvenido/a {nombre} ({rol})!")
    print("1. Consultar los datos personales")
    print("2. Menu Modo Ahorro de Energía")
    print("3. Consultar dispositivos")
    return input("Seleccione una opción: ")

def mostrar_menu_dispositivos():
    print("\n--- Gestión de Dispositivos ---")
    print("1. Listar dispositivos")
    print("2. Agregar dispositivo")
    print("3. Eliminar dispositivo")
    print("4. Volver al menú anterior")
    return input("Seleccione una opción: ")

def gestionar_dispositivos(dispositivos, usuario):
    opcion = ""
    while opcion != "4":
        opcion = mostrar_menu_dispositivos()
        match opcion:
            case "1":
                mostrar_dispositivos_usuario(dispositivos, usuario)
            case "2":
                crear_dispositivo(dispositivos, usuario)
            case "3":
                eliminar_dispositivo_por_nombre(dispositivos, usuario)
            case "4":
                print("Volviendo al menú anterior...")
            case _:
                print("Opción inválida. Intente nuevamente.")
    
def menu_usuario_admin(dispositivos, usuario):
    global autenticado
    autenticado = usuario
    sesion_activa = True
    print("entro sesion activa")
    while sesion_activa:
        opcion = mostrar_menu_usuario_admin(usuario["nombre"], usuario["rol"])
        if opcion == "1":
            gestionar_dispositivos(dispositivos, usuario)
        elif opcion == "2":
            activar_modo_ahorro(dispositivos, usuario)
        elif opcion == "3":
            autenticado = None
            print("Sesión cerrada.")
            sesion_activa = False
        else:
            print("Opción inválida.")
    
def menu_usuario_estandar(dispositivos, usuario):
    global autenticado
    autenticado = usuario
    sesion_activa = True
    print("entro sesion activa")
    while sesion_activa:
        opcion = mostrar_menu_usuario_estandar(usuario["nombre"], usuario["rol"])
        if opcion == "1":
            print("Consultado los datos personales")
        elif opcion == "2":
            print("Ir al menu modo ahorro de bateria")
        elif opcion == "3":
            print("Consultando dispositivos")
        else:
            print("Opción inválida.")

def menu_principal(dispositivos, usuarios):
    app_activa = True

    while app_activa:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            usuario = iniciar_sesion(usuarios)
            if usuario["rol"] == "admin":
                menu_usuario_admin(dispositivos, usuario)
            else:
                menu_usuario_estandar(dispositivos, usuario)
        elif opcion == "3":
            print("¡Hasta luego!")
            app_activa = False
        else:
            print("Opción inválida.")
            
def menu_admin(usuarios, dispositivos, automatizaciones, admin):
    while True:
        print("\n--- MENÚ ADMINISTRADOR ---")
        print("1. Consultar automatizaciones activas") #completa lore
        print("2. Gestionar dispositivos (no implementado aún)")
        print("3. Modificar rol de un usuario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            consultar_automatizaciones(automatizaciones) #completa lore
        elif opcion == "2":
            print("Función de gestión de dispositivos aún no disponible.")
        elif opcion == "3":
            modificar_rol_usuario(usuarios)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

