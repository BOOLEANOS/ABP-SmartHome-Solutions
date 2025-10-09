class Dispositivo:
    def __init__(self, id, nombre, ubicacion, estado, tipo):
        self.__id = id
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__estado = estado
        self.__tipo = tipo
    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_ubicacion(self):
        return self.__ubicacion

    def get_estado(self):
        return self.__estado

    def get_tipo(self):
        return self.__tipo

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def set_tipo(self, tipo):
        self.__tipo = tipo
        
    def encender(self):
        self.__estado = True

    def apagar(self):
        self.__estado = False

    def __str__(self):
        descripcion_estado = "Encendido" if self.__estado else "Apagado"
        return f"Dispositivo(ID: {self.__id}, Nombre: {self.__nombre}, Ubicación: {self.__ubicacion}, Estado: {descripcion_estado}, Tipo: {self.__tipo})"
   
   
   
    
# print (Dispositivo(1, "Lámpara", "Sala", True, "luz").__str__()) 
    
 