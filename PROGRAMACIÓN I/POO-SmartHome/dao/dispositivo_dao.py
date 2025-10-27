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