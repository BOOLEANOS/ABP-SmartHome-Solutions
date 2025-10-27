import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",      
            user="root",           
            password="1234",           
            database="smarthome",
            buffered=True  # Esto ayuda a evitar el error de resultados no leídos
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrar_conexion(conexion, cursor=None):
    try:
        # Cerrar cursor primero si existe
        if cursor:
            cursor.close()
        
        # Luego cerrar conexión
        if conexion and conexion.is_connected():
            conexion.close()
    except Error as e:
        print(f"Error al cerrar conexión: {e}")