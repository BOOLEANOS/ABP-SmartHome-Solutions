class Automatizacion:
    def __init__(self, id, nombre, condicion, acciones):
        """
        id: int -> identificador único
        nombre: str -> nombre de la automatización
        condicion: str (o función) -> condición que debe cumplirse
        acciones: list[callable] -> lista de funciones a ejecutar
        """
        self._id = id
        self._nombre = nombre
        self._condicion = condicion
        self._acciones = acciones

    def ejecutar(self, contexto=None):
        """
        Evalúa la condición y ejecuta las acciones si se cumple.
        'contexto' puede ser un diccionario con información útil
        para evaluar la condición (hora, usuarios activos, etc.)
        """
        if self._evaluar_condicion(contexto):
            print(f"Ejecutando automatización: {self._nombre}")
            for accion in self._acciones:
                accion()
        else:
            print(f"No se cumple la condición de: {self._nombre}")

    def _evaluar_condicion(self, contexto):
        # Por ahora simple: si condicion es callable, la ejecuta
        if callable(self._condicion):
            return self._condicion(contexto)
        # Si es texto, lo tratamos como True/False
        return bool(self._condicion)