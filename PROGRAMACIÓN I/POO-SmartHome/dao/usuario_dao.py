import mysql.connector
from conn.db_conn import crear_conexion, cerrar_conexion

def datos_usuario(usuario):
    """Mostrar los datos del usuario"""
    print(f"Nombre: {usuario['nombre']}\n"
          f"Email: {usuario['correo']}\n"
          f"Contraseña: {usuario['contrasena']}\n"
          f"Rol: {usuario['rol']}\n")
def iniciar_sesion(email, password):
    conexion = None
    cursor = None
    try:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(
                """SELECT u.id_usuario, u.nombre_usuario, u.email, u.password, r.nombre_rol 
                   FROM Usuario u 
                   JOIN Rol r ON u.id_rol = r.id_rol 
                   WHERE u.email = %s AND u.password = %s""",
                (email, password)
            )
            usuario = cursor.fetchone()  # Solo obtiene un resultado
            
            if usuario:
                print("Inicio de sesión exitoso.")
                # Asegurarse de leer todos los resultados si los hay
                cursor.fetchall()  # Esto limpia cualquier resultado restante
                
                usuario_normalizado = {
                    "id": usuario["id_usuario"],
                    "nombre": usuario["nombre_usuario"],
                    "correo": usuario["email"],
                    "contrasena": usuario["password"],
                    "rol": usuario["nombre_rol"]
                }
                return usuario_normalizado
            else:
                print("Credenciales incorrectas.")
                return None
        else:
            print("No se pudo conectar a la base de datos.")
            return None
            
    except mysql.connector.Error as e:
        print(f"Error al iniciar sesión: {e}")
        return None
    finally:
        # Siempre cerrar cursor y conexión en el finally
        cerrar_conexion(conexion, cursor)

def registrar_usuario(nombre, email, password):
    conexion = None
    cursor = None
    try:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            
            # Verificar si es el primer usuario
            cursor.execute("SELECT COUNT(*) FROM Usuario")
            count = cursor.fetchone()[0]
            cursor.fetchall()  # Limpiar resultados
            
            id_rol = 1 if count == 0 else 2  # 1=admin, 2=estandar
            
            # Insertar usuario
            cursor.execute(
                "INSERT INTO Usuario (nombre_usuario, email, password, id_rol) VALUES (%s, %s, %s, %s)",
                (nombre, email, password, id_rol)
            )
            conexion.commit()
            
            rol_nombre = "admin" if id_rol == 1 else "estandar"
            print(f"Usuario {nombre} registrado con éxito como {rol_nombre}.")
            return True
            
        else:
            print("No se pudo conectar a la base de datos.")
            return False
            
    except mysql.connector.Error as e:
        print(f"Error al registrar usuario: {e}")
        return False
    finally:
        cerrar_conexion(conexion, cursor)

def modificar_rol_usuario(email, nuevo_rol_id):
    conexion = None
    cursor = None
    try:
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE Usuario SET id_rol = %s WHERE email = %s",
                (nuevo_rol_id, email)
            )
            
            if cursor.rowcount > 0:
                conexion.commit()
                print(f"Rol actualizado correctamente.")
                return True
            else:
                print("Usuario no encontrado.")
                return False
                
    except mysql.connector.Error as e:
        print(f"Error al modificar rol: {e}")
        return False
    finally:
        cerrar_conexion(conexion, cursor)