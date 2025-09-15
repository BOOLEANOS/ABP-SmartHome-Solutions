# archivo: poo-smarthome/automatizaciones.py

class Automatizacion:
    def __init__(self, id, nombre, condicion, acciones):
        
        self._id = id
        self._nombre = nombre
        self._condicion = condicion
        self._acciones = acciones

    def ejecutar(self, contexto=None):
       
        if self._evaluar_condicion(contexto):
            print(f"Ejecutando automatización: {self._nombre}")
            for accion in self._acciones:
                accion()