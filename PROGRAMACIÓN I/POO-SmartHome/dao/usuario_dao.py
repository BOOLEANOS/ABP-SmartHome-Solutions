from dominio.usuario import Usuario
from conn.db_conn import crear_conexion, cerrar_conexion
from mysql.connector import Error

class UsuarioDAO:
    def agregar_usuario(usuario):
        conexion = crear_conexion()
        if not conexion:
            print("Error al conectar a la base de datos.")
            return
        try:
            cursor = conexion.cursor()
            sql = """INSERT INTO Usuario (nombre_usuario, email, fecha_nacimiento, password, id_rol)
                     VALUES (%s, %s, %s, %s, %s)"""
            valores = (usuario.nombre_usuario, usuario.email, usuario.fecha_nacimiento, usuario.password, usuario.id_rol)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Usuario agregado correctamente.")
        except Error as e:
            print(f"Error al agregar usuario: {e}")
        finally:
            cerrar_conexion(conexion)

    def obtener_usuarios():
        conexion = crear_conexion()
        if not conexion:
            print("Error al conectar a la base de datos.")
            return []
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Usuario")
            return cursor.fetchall()
        except Error as e:
            print(f"Error al obtener usuarios: {e}")
            return []
        finally:
            cerrar_conexion(conexion)
          
    def buscar_usuario_por_email(email):
        conexion = crear_conexion()
        if not conexion:
            print("Error al conectar a la base de datos.")
            return None
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Usuario WHERE email = %s", (email,))
            resultado = cursor.fetchone()
            if resultado:
                return Usuario(
                    resultado["nombre_usuario"],
                    resultado["email"],
                    resultado["fecha_nacimiento"],
                    resultado["password"],
                    resultado["id_rol"]
                )
            return None
        except Error as e:
            print(f"Error al buscar usuario: {e}")
            return None
        finally:
            cerrar_conexion(conexion)
