from dominio.usuario import Usuario
from conn.db_conn import crear_conexion, cerrar_conexion
from mysql.connector import Error

class UsuarioDAO:
   
    def crear_usuario(usuario: Usuario):
        conexion = crear_conexion()
        if conexion is None:
            print("No se pudo conectar a la base de datos.")
            return
        
        try:
            cursor = conexion.cursor()
            query = """INSERT INTO usuarios (nombre, correo, contrasena, rol)
                       VALUES (%s, %s, %s, %s)"""
            valores = (
                usuario.get_nombre(),
                usuario.get_correo(),
                usuario.get_contrasena(),
                usuario.get_rol(),
            )
            cursor.execute(query, valores)
            conexion.commit()
            print("Usuario agregado correctamente.")
        except Error as e:
            print(f"Error al insertar usuario: {e}")
        finally:
            cerrar_conexion(conexion)

    def obtener_todos():
        conexion = crear_conexion()
        if conexion is None:
            print("No se pudo conectar a la base de datos.")
            return []

        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, correo, contrasena, rol FROM usuarios")
            filas = cursor.fetchall()
            usuarios = [Usuario(*fila) for fila in filas]
            return usuarios
        except Error as e:
            print(f"Error al obtener usuarios: {e}")
            return []
        finally:
            cerrar_conexion(conexion)

    def obtener_por_correo(correo):
        conexion = crear_conexion()
        if conexion is None:
            return None

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id, nombre, correo, contrasena, rol FROM usuarios WHERE correo = %s",
                (correo,)
            )
            fila = cursor.fetchone()
            if fila:
                return Usuario(*fila)
            else:
                return None
        except Error as e:
            print(f"Error al obtener usuario por correo: {e}")
            return None
        finally:
            cerrar_conexion(conexion)

    def actualizar_rol(correo, nuevo_rol):
        conexion = crear_conexion()
        if conexion is None:
            print("No se pudo conectar a la base de datos.")
            return
        
        try:
            cursor = conexion.cursor()
            cursor.execute("UPDATE usuarios SET rol = %s WHERE correo = %s", (nuevo_rol, correo))
            conexion.commit()
            if cursor.rowcount > 0:
                print("🔁 Rol actualizado correctamente.")
            else:
                print("No se encontró el usuario con ese correo.")
        except Error as e:
            print(f"Error al actualizar rol: {e}")
        finally:
            cerrar_conexion(conexion)
          
    def eliminar_usuario(correo):
        conexion = crear_conexion()
        if conexion is None:
            print("No se pudo conectar a la base de datos.")
            return

        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM usuarios WHERE correo = %s", (correo,))
            conexion.commit()
            if cursor.rowcount > 0:
                print("🗑️ Usuario eliminado correctamente.")
            else:
                print("No se encontró el usuario.")
        except Error as e:
            print(f"Error al eliminar usuario: {e}")
        finally:
            cerrar_conexion(conexion)
