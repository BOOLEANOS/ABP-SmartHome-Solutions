# gestion_dispositivos.py
import re
from dominio.dispositivos import Dispositivo

class GestionDispositivos:
    def __init__(self, dispositivos):
        self.__dispositivos = dispositivos

    def mostrar_dispositivos(self):
        print("\nDispositivos registrados:")

        if not self.__dispositivos:
            print("No hay dispositivos registrados.")
            return

        for d in self.__dispositivos:
            print(d.__str__())

    def crear_dispositivo(self):
        nombre = input("Nombre del dispositivo: ").strip()
        ubicacion = input("Ubicación (cocina, living, comedor, etc.): ").strip()
        tipo = input("Tipo (luz, cámara, termostato, etc.): ").strip()

        if not nombre or not ubicacion or not tipo:
            print("Nombre y tipo son obligatorios.")
            return

        nuevo_id = len(self.__dispositivos) + 1
        estado = True
        nuevo_dispositivo = Dispositivo(nuevo_id, nombre, ubicacion, estado, tipo)
        self.__dispositivos.append(nuevo_dispositivo)
        print(f" Dispositivo '{nombre}' agregado correctamente.")

    def eliminar_dispositivo_por_nombre(self):
        nombre = input("Ingrese el nombre del dispositivo a eliminar: ").strip()

        for d in self.__dispositivos:
            if d.get_nombre().lower() == nombre.lower():
                self.__dispositivos.remove(d)
                print(f"Dispositivo '{nombre}' eliminado.")
                return

        print("Dispositivo no encontrado o no pertenece a su cuenta.")

    def cambiar_estado_dispositivo(self, estado):
        nombre = input("Ingrese el nombre del dispositivo: ").strip()

        for d in self.__dispositivos:
            if d.get_nombre().lower() == nombre.lower():
                if (estado):
                    d.encender()
                    print("Dispositivo activado correctamente.")
                else:
                    d.apagar()
                    print("Dispositivo desactivado correctamente.")
                return

        print("Dispositivo no encontrado o no pertenece a su cuenta.")
