import sys
import os

# Configurar path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

print("🔌 Probando conexión básica...")

try:
    # Probar solo la conexión primero
    from conn.db_conn import crear_conexion
    
    conexion = crear_conexion()
    if conexion:
        print("✅ Conexión a MySQL exitosa!")
        
        # Probar consultas básicas
        cursor = conexion.cursor()
        
        # Contar usuarios
        cursor.execute("SELECT COUNT(*) FROM Usuario")
        usuarios_count = cursor.fetchone()[0]
        print(f"✅ Usuarios en BD: {usuarios_count}")
        
        # Contar dispositivos
        cursor.execute("SELECT COUNT(*) FROM Dispositivo")
        dispositivos_count = cursor.fetchone()[0]
        print(f"✅ Dispositivos en BD: {dispositivos_count}")
        
        # Mostrar algunos usuarios
        cursor.execute("SELECT nombre_usuario, email, nombre_rol FROM Usuario u JOIN Rol r ON u.id_rol = r.id_rol LIMIT 3")
        usuarios = cursor.fetchall()
        print("\n📋 Algunos usuarios:")
        for usuario in usuarios:
            print(f"  - {usuario[0]} ({usuario[1]}) - {usuario[2]}")
        
        conexion.close()
        print("\n🎉 ¡Base de datos funcionando correctamente!")
    else:
        print("❌ Error en la conexión a MySQL")

except ImportError as e:
    print(f"❌ Error de importación: {e}")
    print("\n💡 Posibles soluciones:")
    print("1. Verifica que el archivo conn/db_conn.py exista")
    print("2. Revisa que tengas mysql-connector-python instalado")
    print("3. Ejecuta: pip install mysql-connector-python")
    
except Exception as e:
    print(f"❌ Error: {e}")

