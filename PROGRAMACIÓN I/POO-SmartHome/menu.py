from usuarios import registrar_usuario, iniciar_sesion, modificar_rol_usuario, datos_usuario
from dispositivos import GestionDispositivos
from automatizaciones import activar_modo_ahorro, configurar_modo_ahorro
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

def buscar_dispositivo_por_nombre(gestion_dispositivos):
    """Función para buscar dispositivo por nombre"""
    nombre = input("Ingrese el nombre del dispositivo a buscar: ").strip()
    
    dispositivos = gestion_dispositivos._GestionDispositivos__dispositivos  # Acceder a la lista interna
    encontrados = []
    
    for d in dispositivos:
        if nombre.lower() in d.get_nombre().lower():
            encontrados.append(d)
    
    if encontrados:
        print(f"\nDispositivos encontrados ({len(encontrados)}):")
        for d in encontrados:
            print(d.__str__())
    else:
        print("No se encontraron dispositivos con ese nombre.")

def gestionar_automatizacion(gestion_dispositivos, usuario):
    opcion = ""
    while opcion != "3":
        opcion = mostrar_menu_automatizaciones()
        match opcion:
            case "1":
                dispositivos = gestion_dispositivos._GestionDispositivos__dispositivos
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

def gestionar_dispositivos(gestion_dispositivos, usuario):
    opcion = ""
    while opcion != "6":
        opcion = mostrar_menu_dispositivos()
        match opcion:
            case "1":
                gestion_dispositivos.mostrar_dispositivos()
            case "2":
                gestion_dispositivos.crear_dispositivo()
            case "3":
                gestion_dispositivos.eliminar_dispositivo_por_nombre()
            case "4":
                buscar_dispositivo_por_nombre(gestion_dispositivos)
            case "5":
                activar_desactivar_dispositivo(gestion_dispositivos)
            case "6":
                print("Volviendo al menú anterior...")
            case _:
                print("Opción inválida. Intente nuevamente.")
    
def activar_desactivar_dispositivo(gestion_dispositivos):
    opcion = ""
    while opcion != "1" and opcion != "2":
        opcion = mostrar_menu_cambio_estado_dispositivo()
        match opcion:
            case "1":
                gestion_dispositivos.cambiar_estado_dispositivo(True)
            case "2":
                gestion_dispositivos.cambiar_estado_dispositivo(False)
            case _:
                print("Opción inválida. Intente nuevamente.")

def mostrar_dispositivos_usuario(gestion_dispositivos, usuario):
    """Función para mostrar dispositivos del usuario"""
    gestion_dispositivos.mostrar_dispositivos()

def menu_usuario_admin(gestion_dispositivos, usuario, usuarios):
    global autenticado
    autenticado = usuario
    sesion_activa = True
    
    while sesion_activa:
        opcion = mostrar_menu_usuario_admin(usuario["nombre"], usuario["rol"])
        if opcion == "1":
            gestionar_dispositivos(gestion_dispositivos, usuario)
        elif opcion == "2":
            dispositivos = gestion_dispositivos._GestionDispositivos__dispositivos
            activar_modo_ahorro(dispositivos, usuario)
        elif opcion == "3":
            modificar_rol_usuario(usuarios)
        elif opcion == "4":
            autenticado = None
            print("Sesión cerrada.")
            sesion_activa = False
        else:
            print("Opción inválida.")
    
def menu_usuario_estandar(gestion_dispositivos, usuario):
    global autenticado
    autenticado = usuario
    sesion_activa = True
    
    while sesion_activa:
        opcion = mostrar_menu_usuario_estandar(usuario["nombre"])
        if opcion == "1":
            print("Consultando los datos personales...\n")
            datos_usuario(usuario)
        elif opcion == "2":
            gestionar_automatizacion(gestion_dispositivos, usuario)
        elif opcion == "3":
            print("Consultando dispositivos...\n")
            mostrar_dispositivos_usuario(gestion_dispositivos, usuario)
        elif opcion == "4":
            autenticado = None
            sesion_activa = False
            print("Sesión cerrada.")
        else:
            print("Opción inválida.")

def menu_principal():
    # Inicializar estructuras de datos
    usuarios = []
    lista_dispositivos = []  # Lista vacía de dispositivos
    gestion_dispositivos = GestionDispositivos(lista_dispositivos)
    
    app_activa = True

    while app_activa:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            usuario = iniciar_sesion(usuarios)
            if usuario:  # Solo si el login fue exitoso
                if usuario["rol"] == "admin":
                    menu_usuario_admin(gestion_dispositivos, usuario, usuarios)
                else:
                    menu_usuario_estandar(gestion_dispositivos, usuario)
        elif opcion == "3":
            print("¡Hasta luego!")
            app_activa = False
        else:
            print("Opción inválida.")

# Ejecutar la aplicación
if __name__ == "__main__":
    menu_principal()
