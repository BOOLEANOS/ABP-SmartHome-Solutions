def iniciar_sesion():
    email = input("Email: ")
    password = input("Contraseña: ")
    
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(
                """SELECT u.id_usuario, u.nombre_usuario, u.email, u.password, r.nombre_rol 
                   FROM Usuario u 
                   JOIN Rol r ON u.id_rol = r.id_rol 
                   WHERE u.email = %s AND u.password = %s""",
                (email, password)
            )
            usuario = cursor.fetchone()
            
            if usuario:
                print("Inicio de sesión exitoso.")
                # Normalizar los nombres de campos para el sistema
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
                
        except mysql.connector.Error as e:
            print(f"Error al iniciar sesión: {e}")
            return None
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo conectar a la base de datos.")
        return None
