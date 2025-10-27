
from dao.dispositivo_dao import DispositivoDAO
from dominio.dispositivos import Dispositivo
class GestionIDispositivos:
    def __init__(self, id_usuario):
        self.__id_usuario = id_usuario
        self.__dispositivo_dao = DispositivoDAO()
        self.__dispositivos = self.__dispositivo_dao.obtener_todos_por_usuario(id_usuario)

# gestion_dispositivos.py
import re
from dominio.dispositivos import Dispositivo


    def get_dispositivos(self):
        self.__dispositivos = self.__dispositivo_dao.obtener_todos_por_usuario(self.__id_usuario)
        return self.__dispositivos

    def mostrar_dispositivos(self):
        print("\n=== TUS DISPOSITIVOS ===")
        dispositivos = self.get_dispositivos()
        
        if not dispositivos:
            print("No hay dispositivos registrados.")
            return

        for d in dispositivos:
            print(d)

    def crear_dispositivo(self):
        print("\n=== AGREGAR NUEVO DISPOSITIVO ===")
        nombre = input("Nombre del dispositivo: ").strip()
        ubicacion = input("Ubicación (cocina, living, comedor, etc.): ").strip()
        
        tipos = self.__dispositivo_dao.obtener_tipos_dispositivos()
        print("\nTipos de dispositivos disponibles:")
        for tipo in tipos:
            print(f"{tipo[0]}. {tipo[1]}")
        
        try:
            id_tipo = int(input("Seleccione el tipo (número): ").strip())
        except ValueError:
            print("Tipo inválido.")
            return

        if not nombre or not ubicacion:
            print("Nombre y ubicación son obligatorios.")
            return

        nuevo_dispositivo = Dispositivo(0, nombre, ubicacion, 'apagado', id_tipo)
        self.__dispositivo_dao.crear_dispositivo(nuevo_dispositivo, self.__id_usuario)
        self.get_dispositivos()

    def eliminar_dispositivo_por_nombre(self):
        nombre = input("Ingrese el nombre del dispositivo a eliminar: ").strip()

        for d in self.__dispositivos:
            if d.get_nombre().lower() == nombre.lower():
                self.__dispositivo_dao.eliminar_dispositivo(d.get_id())
                print(f"Dispositivo '{nombre}' eliminado.")
                self.get_dispositivos()
                return

        print("Dispositivo no encontrado.")

    def cambiar_estado_dispositivo(self, estado):
        nombre = input("Ingrese el nombre del dispositivo: ").strip()

        for d in self.__dispositivos:
            if d.get_nombre().lower() == nombre.lower():
                if estado:
                    d.encender()
                else:
                    d.apagar()
                self.__dispositivo_dao.actualizar_dispositivo(d)
                if estado:
                    print("Dispositivo activado correctamente.")
                else:
                    print("Dispositivo desactivado correctamente.")
                return

        print("Dispositivo no encontrado.")