from dominio.dispositivos import Dispositivo
from conn.db_conn import crear_conexion, cerrar_conexion
from mysql.connector import Error

class DispositivoDAO:
    
    def crear_dispositivo(dispositivo: Dispositivo):
        conexion = crear_conexion()
        if conexion is None:
            print("No se pudo conectar a la base de datos.")
            return
        
        try:
            cursor = conexion.cursor()
            query = """INSERT INTO dispositivos (nombre, ubicacion, estado, tipo)
                       VALUES (%s, %s, %s, %s)"""
            valores = (
                dispositivo.get_nombre(),
                dispositivo.get_ubicacion(),
                dispositivo.get_estado(),
                dispositivo.get_tipo(),
            )
            cursor.execute(query, valores)
            conexion.commit()
            print("Dispositivo agregado correctamente.")
        except Error as e:
            print(f"Error al insertar dispositivo: {e}")
        finally:
            cerrar_conexion(conexion)

    def obtener_todos():
        conexion = crear_conexion()
        if conexion is None:
            print("No se pudo conectar a la base de datos.")
            return []

        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, ubicacion, estado, tipo FROM dispositivos")
            filas = cursor.fetchall()
            dispositivos = [Dispositivo(*fila) for fila in filas]
            return dispositivos
        except Error as e:
            print(f"Error al obtener dispositivos: {e}")
            return []
        finally:
            cerrar_conexion(conexion)

    def obtener_por_id(id_dispositivo):
        conexion = crear_conexion()
        if conexion is None:
            return None

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id, nombre, ubicacion, estado, tipo FROM dispositivos WHERE id = %s",
                (id_dispositivo,)
            )
            fila = cursor.fetchone()
            if fila:
                return Dispositivo(*fila)
            else:
                return None
        except Error as e:
            print(f"Error al obtener dispositivo por ID: {e}")
            return None
        finally:
            cerrar_conexion(conexion)

    def actualizar_dispositivo(dispositivo: Dispositivo):
        conexion = crear_conexion()
        if conexion is None:
            print("No se pudo conectar a la base de datos.")
            return
        
        try:
            cursor = conexion.cursor()
            query = """UPDATE dispositivos
                       SET nombre = %s, ubicacion = %s, estado = %s, tipo = %s
                       WHERE id = %s"""
            valores = (
                dispositivo.get_nombre(),
                dispositivo.get_ubicacion(),
                dispositivo.get_estado(),
                dispositivo.get_tipo(),
                dispositivo.get_id()
            )
            cursor.execute(query, valores)
            conexion.commit()
            if cursor.rowcount > 0:
                print("Dispositivo actualizado correctamente.")
            else:
                print("No se encontró el dispositivo con ese ID.")
        except Error as e:
            print(f"Error al actualizar dispositivo: {e}")
        finally:
            cerrar_conexion(conexion)
          
    def eliminar_dispositivo(id_dispositivo):
        conexion = crear_conexion()
        if conexion is None:
            print("No se pudo conectar a la base de datos.")
            return

        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM dispositivos WHERE id = %s", (id_dispositivo,))
            conexion.commit()
            if cursor.rowcount > 0:
                print("Dispositivo eliminado correctamente.")
            else:
                print("No se encontró el dispositivo.")
        except Error as e:
            print(f"Error al eliminar dispositivo: {e}")
        finally:
            cerrar_conexion(conexion)
