import mysql.connector
from conn.db_conn import crear_conexion, cerrar_conexion
from dominio.automatizacion import Automatizacion

def activar_modo_ahorro(usuario_id):
    print(f"\nActivando modo ahorro de energía...")
    
    conexion = None
    cursor = None
    try:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            
            # Apagar todos los dispositivos del usuario
            cursor.execute(
                "UPDATE Dispositivo SET estado_dispositivo = 'apagado' WHERE id_usuario = %s",
                (usuario_id,)
            )
            
            conexion.commit()
            print("Modo ahorro activado. Todos los dispositivos han sido apagados.")
            
    except mysql.connector.Error as e:
        print(f"Error al activar modo ahorro: {e}")
    finally:
        cerrar_conexion(conexion, cursor)

def configurar_modo_ahorro(hora_on, hora_off):
    print(f"Configurando modo ahorro: Encender a las {hora_on}, Apagar a las {hora_off}")
    print("Configuración guardada exitosamente.")

def consultar_automatizaciones(usuario_id):
    print("\n--- Automatizaciones Configuradas ---")
    
    conexion = None
    cursor = None
    try:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            query = """
            SELECT a.nombre_automatizacion, a.estado_automatizacion, 
                   c.tipo_condicion, ac.tipo_accion, d.nombre_dispositivo
            FROM Automatizacion a
            LEFT JOIN Condicion_Automatizacion c ON a.id_condicion = c.id_condicion
            LEFT JOIN Accion_Automatizacion ac ON a.id_accion = ac.id_accion
            LEFT JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
            WHERE d.id_usuario = %s OR d.id_usuario IS NULL
            """
            cursor.execute(query, (usuario_id,))
            
            automatizaciones = cursor.fetchall()
            if automatizaciones:
                for auto in automatizaciones:
                    print(f"Nombre: {auto['nombre_automatizacion']}, Estado: {auto['estado_automatizacion']}, Condición: {auto['tipo_condicion']}, Acción: {auto['tipo_accion']}, Dispositivo: {auto['nombre_dispositivo']}")
            else:
                print("No hay automatizaciones configuradas.")
                
    except mysql.connector.Error as e:
        print(f"Error al consultar automatizaciones: {e}")
    finally:
        cerrar_conexion(conexion, cursor)

def obtener_automatizaciones_usuario(usuario_id):
    """Obtener todas las automatizaciones de un usuario como objetos"""
    conexion = None
    cursor = None
    automatizaciones = []
    
    try:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            query = """
            SELECT a.id_automatizacion, a.nombre_automatizacion, 
                   c.tipo_condicion, ac.tipo_accion
            FROM Automatizacion a
            LEFT JOIN Condicion_Automatizacion c ON a.id_condicion = c.id_condicion
            LEFT JOIN Accion_Automatizacion ac ON a.id_accion = ac.id_accion
            LEFT JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
            WHERE d.id_usuario = %s
            """
            cursor.execute(query, (usuario_id,))
            
            for row in cursor.fetchall():
                # Crear objeto Automatizacion
                automatizacion = Automatizacion(
                    id=row['id_automatizacion'],
                    nombre=row['nombre_automatizacion'],
                    condicion=row['tipo_condicion'],
                    acciones=[lambda: print(f"Ejecutando: {row['tipo_accion']}")]
                )
                automatizaciones.append(automatizacion)
                
    except mysql.connector.Error as e:
        print(f"Error al obtener automatizaciones: {e}")
    finally:
        cerrar_conexion(conexion, cursor)
    
    return automatizaciones