class Automatizacion:
    def __init__(self, id, nombre, condicion, acciones):
        self._id = id
        self._nombre = nombre
        self._condicion = condicion   # Texto o función que determina cuándo se activa
        self._acciones = acciones     # Lista de funciones o dispositivos a modificar

    def ejecutar(self):
        print(f"Ejecutando automatización: {self._nombre}")
        for accion in self._acciones:
            accion()  # Se asume que cada acción es una función ejecutable