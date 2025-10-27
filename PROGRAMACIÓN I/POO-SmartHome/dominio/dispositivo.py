class Dispositivo:
    def __init__(self, id_dispositivo, nombre_dispositivo, ubicacion, estado_dispositivo, id_tipo, id_usuario=None):
        self.__id_dispositivo = id_dispositivo
        self.__nombre_dispositivo = nombre_dispositivo
        self.__ubicacion = ubicacion
        self.__estado_dispositivo = estado_dispositivo
        self.__id_tipo = id_tipo
        self.__id_usuario = id_usuario

    def get_id(self):
        return self.__id_dispositivo

    def get_nombre(self):
        return self.__nombre_dispositivo

    def get_ubicacion(self):
        return self.__ubicacion

    def get_estado(self):
        return self.__estado_dispositivo

    def get_tipo(self):
        return self.__id_tipo

    def get_id_usuario(self):
        return self.__id_usuario

    def set_estado(self, estado):
        self.__estado_dispositivo = estado

    def encender(self):
        self.__estado_dispositivo = 'encendido'

    def apagar(self):
        self.__estado_dispositivo = 'apagado'

    def __str__(self):
        estado_str = "Encendido" if self.__estado_dispositivo == 'encendido' else "Apagado"
        tipo_str = self._get_tipo_nombre()
        return f"ID: {self.__id_dispositivo}, Nombre: {self.__nombre_dispositivo}, Ubicación: {self.__ubicacion}, Estado: {estado_str}, Tipo: {tipo_str}"

    def _get_tipo_nombre(self):
        tipos = {
            1: "Luz",
            2: "Sensor", 
            3: "Cámara",
            4: "Electrodoméstico"
        }
        return tipos.get(self.__id_tipo, "Desconocido")