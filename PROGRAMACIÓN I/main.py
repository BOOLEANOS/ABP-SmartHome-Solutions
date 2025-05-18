from usuarios import registrar_usuario, iniciar_sesion
from dispositivos import menu_dispositivos
from automatizaciones import activar_modo_ahorro

usuarios = []
dispositivos = []
autenticado = None

while True:
    print("\n=== SmartHome Solutions ===")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario(usuarios)
    elif opcion == "2":
        autenticado = iniciar_sesion(usuarios)
        if autenticado:
            while True:
                print(f"\nBienvenido/a {autenticado['nombre']}!")
                print("1. Gestionar dispositivos")
                print("2. Activar Modo Ahorro de Energía")
                print("3. Cerrar sesión")
                sub_opcion = input("Seleccione una opción: ")
                if sub_opcion == "1":
                    menu_dispositivos(dispositivos, autenticado)
                elif sub_opcion == "2":
                    activar_modo_ahorro(dispositivos, autenticado)
                elif sub_opcion == "3":
                    autenticado = None
                    break
                else:
                    print("Opción inválida.")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
