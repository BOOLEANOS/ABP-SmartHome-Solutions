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
        else:
            print(f"No se cumple la condición de: {self._nombre}")

    def _evaluar_condicion(self, contexto):
        if callable(self._condicion):
            return self._condicion(contexto)
        return bool(self._condicion)