from usuarios import registrar_usuario, iniciar_sesion, modificar_rol_usuario
from dispositivos import *
from automatizaciones import activar_modo_ahorro


def mostrar_menu_principal():
    print("\n=== SmartHome Solutions ===")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    return input("Seleccione una opción: ")

def mostrar_menu_usuario(nombre, rol):
    print(f"\nBienvenido/a {nombre} ({rol})!")
    print("1. Gestionar dispositivos")
    print("2. Activar Modo Ahorro de Energía")
    print("3. Cerrar sesión")
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
    
def menu_usuario(dispositivos, usuario):
    global autenticado
    autenticado = usuario
    sesion_activa = True
    print("entro sesion activa")
    while sesion_activa:
        opcion = mostrar_menu_usuario(usuario["nombre"], usuario["rol"])
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

def menu_principal(dispositivos, usuarios):
    app_activa = True

    while app_activa:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            usuario = iniciar_sesion(usuarios)
            if usuario:
                menu_usuario(dispositivos, usuario)
        elif opcion == "3":
            print("¡Hasta luego!")
            app_activa = False
        else:
            print("Opción inválida.")
            
def menu_admin(usuarios, dispositivos, automatizaciones, admin):
    while True:
        print("\n--- MENÚ ADMINISTRADOR ---")
        print("1. Encender un dispositivo")
        print("2. Apagar un dispositivo")
        print("3. Ver estado de los dispositivos")
        print("4. Salir")
        # bucle principal
        while True: 
            mostrar = menu_admin()
            opcion= input("Elige una opcion:")

    if opcion == "1":
            print ("/n dispositivos disponibles para encender:")
            for nombre  in dispositivos:
                if not dispositivos[nombre]:
                    print(f"-{nombre}")
                nombre = input ("escribe el nombre exacto del dispositivo a encender:")
            if nombre in dispositivos  and not dispositivo [nombre]:
                        dispositivos [nombre] = True 
                        print (f"{nombre}encendido.")
            else: 
                print("nombre invalido o ya esta encendido.")
    elif opcion == "2":
            print("/n dispositivos disponibles para apagar:")
            for nombre in dispositivos:
             if dispositivos [nombre]:
                print(f"-{nombre}")
                nombre = input ("escribe elnombre exacto del dispositivo a apagar:")
                if nombre in dispositivos and dispositivos[nombre]:
                     dispositivos[nombre]= False
                     print (f"{nombre} apagado.")
                else:
                     print("nombre invalido oya esta apagado.")
                     
    elif opcion == "3":
            mostrar_estado()

    elif opcion == "4":
      print("saliendo del sistema...")
      
      
    else:
      print("Opción no valida.intenta nuevamente.")

