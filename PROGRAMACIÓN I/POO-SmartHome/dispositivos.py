class Dispositivo:
    def __init__(self, id, nombre, ubicacion, estado, tipo, usuario):
        self.__id = id
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__estado = estado
        self.__tipo = tipo
    
    def encender(self):
        self.__estado = True

    def apagar(self):
        self.__estado = False

    def __str__(self):
        descripcion_estado = "Encendido" if self.__estado else "Apagado"
        return f"Dispositivo(ID: {self.__id}, Nombre: {self.__nombre}, Ubicación: {self.__ubicacion}, Estado: {descripcion_estado}, Tipo: {self.__tipo})"
    
# print (Dispositivo(1, "Lámpara", "Sala", True, "luz").__str__()) 
    
 