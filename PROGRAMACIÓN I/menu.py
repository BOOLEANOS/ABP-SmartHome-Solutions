from usuarios import registrar_usuario, iniciar_sesion, modificar_rol_usuario, datos_usuario
from dispositivos import *
from automatizaciones import activar_modo_ahorro, configurar_modo_ahorro, consultar_automatizaciones


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
    print("4. Activar/desactivar dispositivo")
    print("5. Volver al menú anterior")
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

def gestionar_automatizacion(dispositivos, usuario):
    opcion = ""
    while opcion != "3":
        opcion = mostrar_menu_automatizaciones()
        match opcion:
            case "1":
                activar_modo_ahorro(dispositivos, usuario)
            case "2":
                print("Configurando modo ahorro de energía...")
                horaOn = input("Ingrese la hora para encender las luces: ")
                horaOff = input("Ingrese la hora para apagar las luces: ")
                configurar_modo_ahorro(horaOn, horaOff)
            case "3":
                print("Volviendo al menú anterior...")
            case _:
                print("Opción inválida. Intente nuevamente.")

def gestionar_dispositivos(dispositivos, usuario):
    opcion = ""
    while opcion != "5":
        opcion = mostrar_menu_dispositivos()
        match opcion:
            case "1":
                mostrar_dispositivos_usuario(dispositivos, usuario)
            case "2":
                crear_dispositivo(dispositivos, usuario)
            case "3":
                eliminar_dispositivo_por_nombre(dispositivos, usuario)
            case "4":
                activar_desactivar_dispositivo(dispositivos)
            case "5":
                print("Volviendo al menú anterior...")
            case _:
                print("Opción inválida. Intente nuevamente.")
    
def activar_desactivar_dispositivo(dispositivos):
    opcion = ""
    while opcion != "1" and opcion != "2":
        opcion = mostrar_menu_cambio_estado_dispositivo()
        match opcion:
            case "1":
                cambiar_estado_dispositivo(dispositivos, True)
            case "2":
                cambiar_estado_dispositivo(dispositivos, False)
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
        opcion = mostrar_menu_usuario_estandar(usuario["nombre"])
        if opcion == "1":
            print("Consultando los datos personales...\n")
            datos_usuario(usuario)
        elif opcion == "2":
            gestionar_automatizacion(dispositivos, usuario)
        elif opcion == "3":
            print("Consultando dispositivos...\n")
            mostrar_dispositivos_usuario(dispositivos, usuario)
        elif opcion == "4":
            autenticado = None
            sesion_activa = False
            print("Sesión cerrada.")
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

