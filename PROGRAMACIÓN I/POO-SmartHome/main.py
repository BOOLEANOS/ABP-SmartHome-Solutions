from dao.usuario_dao import registrar_usuario, iniciar_sesion, modificar_rol_usuario
from dao.dispositivo_dao import obtener_dispositivos_usuario, crear_dispositivo, eliminar_dispositivo, cambiar_estado_dispositivo
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
    print("4. Consultar automatizaciones")
    print("5. Cerrar sesión")
    return input("Seleccione una opción: ")

def mostrar_menu_usuario_estandar(nombre):
    print(f"\nBienvenido/a {nombre}")
    print("1. Consultar los datos personales")
    print("2. Menu modo ahorro de energía")
    print("3. Consultar dispositivos")
    print("4. Consultar automatizaciones")
    print("5. Cerrar sesión")
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
            from dao.automatizacion_dao import activar_modo_ahorro
            activar_modo_ahorro(usuario["id"])
        elif opcion == "2":
            print("Configurando modo ahorro de energía...")
            horaOn = input("Ingrese la hora para encender las luces: ")
            horaOff = input("Ingrese la hora para apagar las luces: ")
            # Aquí podrías guardar esta configuración en la base de datos
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
            print("Opción inválida. Intente nuevamente.")
    
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

def consultar_automatizaciones(usuario_id):
    print("\n--- Automatizaciones Configuradas ---")
    # Esta función podría implementarse en automatizacion_dao.py
    print("Funcionalidad en desarrollo...")

def datos_usuario(usuario):
    print(f"Nombre: {usuario['nombre']}\n"
          f"Email: {usuario['correo']}\n"
          f"Contraseña: {usuario['contrasena']}\n"
          f"Rol: {usuario['rol']}\n")

def menu_usuario_admin(usuario):
    global autenticado
    autenticado = usuario
    sesion_activa = True
    
    while sesion_activa:
        opcion = mostrar_menu_usuario_admin(usuario["nombre"], usuario["rol"])
        if opcion == "1":
            gestionar_dispositivos(usuario)
        elif opcion == "2":
            from dao.automatizacion_dao import activar_modo_ahorro
            activar_modo_ahorro(usuario["id"])
        elif opcion == "3":
            email = input("Email del usuario a modificar: ")
            print("\nRoles disponibles:")
            print("1. admin")
            print("2. estandar")
            nuevo_rol_id = input("Seleccione el ID del nuevo rol (1 o 2): ")
            modificar_rol_usuario(email, nuevo_rol_id)
        elif opcion == "4":
            consultar_automatizaciones(usuario["id"])
        elif opcion == "5":
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
            dispositivos = obtener_dispositivos_usuario(usuario["id"])
            if dispositivos:
                for d in dispositivos:
                    estado_str = "Encendido" if d["estado"] else "Apagado"
                    print(f"Nombre: {d['nombre']}, Ubicación: {d['ubicacion']}, Estado: {estado_str}, Tipo: {d['tipo']}")
            else:
                print("No hay dispositivos registrados.")
        elif opcion == "4":
            consultar_automatizaciones(usuario["id"])
        elif opcion == "5":
            autenticado = None
            sesion_activa = False
            print("Sesión cerrada.")
        else:
            print("Opción inválida.")

def main():
    # Verificar conexión a la base de datos
    conexion = crear_conexion()
    if conexion:
        print("✓ Conectado a la base de datos MySQL")
        conexion.close()
    else:
        print("⚠ No se pudo conectar a la base de datos")
    
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
    main()
import mysql.connector
from conn.db_conn import crear_conexion, cerrar_conexion

def obtener_dispositivos_usuario(usuario_id):
    conexion = None
    cursor = None
    try:
        conexion = crear_conexion()
        dispositivos = []
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            query = """
            SELECT d.id_dispositivo, d.nombre_dispositivo, d.ubicacion, 
                   d.estado_dispositivo, t.tipo_dispositivo, t.id_tipo
            FROM Dispositivo d
            JOIN Tipo_dispositivo t ON d.id_tipo = t.id_tipo
            WHERE d.id_usuario = %s
            """
            cursor.execute(query, (usuario_id,))
            
            resultados = cursor.fetchall()
            
            for row in resultados:
                estado_bool = True if row['estado_dispositivo'] == 'encendido' else False
                dispositivo = {
                    "id": row['id_dispositivo'],
                    "nombre": row['nombre_dispositivo'],
                    "ubicacion": row['ubicacion'],
                    "estado": estado_bool,
                    "tipo": row['tipo_dispositivo'],
                    "tipo_id": row['id_tipo']
                }
                dispositivos.append(dispositivo)
                
        return dispositivos
        
    except mysql.connector.Error as e:
        print(f"Error al obtener dispositivos: {e}")
        return []
    finally:
        cerrar_conexion(conexion, cursor)

def crear_dispositivo(usuario_id):
    conexion = None
    cursor = None
    try:
        nombre = input("Nombre del dispositivo: ").strip()
        ubicacion = input("Ubicación (cocina, living, comedor, etc.): ").strip()
        
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            
            # Mostrar tipos disponibles
            cursor.execute("SELECT * FROM Tipo_dispositivo")
            tipos = cursor.fetchall()
            print("\nTipos de dispositivos disponibles:")
            for tipo in tipos:
                print(f"{tipo[0]}. {tipo[1]}")
            
            tipo_id = input("Seleccione el ID del tipo: ")
            
            # Insertar dispositivo
            cursor.execute(
                "INSERT INTO Dispositivo (nombre_dispositivo, ubicacion, estado_dispositivo, id_usuario, id_tipo) VALUES (%s, %s, 'apagado', %s, %s)",
                (nombre, ubicacion, usuario_id, tipo_id)
            )
            conexion.commit()
            print(f"Dispositivo '{nombre}' agregado correctamente.")
            
    except mysql.connector.Error as e:
        print(f"Error al crear dispositivo: {e}")
    finally:
        cerrar_conexion(conexion, cursor)

def eliminar_dispositivo(usuario_id):
    conexion = None
    cursor = None
    try:
        nombre = input("Ingrese el nombre del dispositivo a eliminar: ").strip()

        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "DELETE FROM Dispositivo WHERE nombre_dispositivo = %s AND id_usuario = %s",
                (nombre, usuario_id)
            )
            
            if cursor.rowcount > 0:
                conexion.commit()
                print(f"Dispositivo '{nombre}' eliminado.")
            else:
                print("Dispositivo no encontrado.")
                
    except mysql.connector.Error as e:
        print(f"Error al eliminar dispositivo: {e}")
    finally:
        cerrar_conexion(conexion, cursor)

def cambiar_estado_dispositivo(usuario_id, estado):
    conexion = None
    cursor = None
    try:
        nombre = input("Ingrese el nombre del dispositivo: ").strip()

        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            estado_db = 'encendido' if estado else 'apagado'
            cursor.execute(
                "UPDATE Dispositivo SET estado_dispositivo = %s WHERE nombre_dispositivo = %s AND id_usuario = %s",
                (estado_db, nombre, usuario_id)
            )
            
            if cursor.rowcount > 0:
                conexion.commit()
                if estado:
                    print("Dispositivo activado correctamente.")
                else:
                    print("Dispositivo desactivado correctamente.")
            else:
                print("Dispositivo no encontrado.")
                
    except mysql.connector.Error as e:
        print(f"Error al cambiar estado: {e}")
    finally:
        cerrar_conexion(conexion, cursor)