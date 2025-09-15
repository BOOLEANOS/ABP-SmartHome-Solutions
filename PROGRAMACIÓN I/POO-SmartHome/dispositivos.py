class Dispositivo:
    def __init__(self, id_dispositivo, nombre_dispositivo, ubicacion, estado_dispositivo, id_tipo, id_usuario):
        self.id_dispositivo = id_dispositivo
        self.nombre_dispositivo = nombre_dispositivo
        self.ubicacion = ubicacion
        self.estado_dispositivo = estado_dispositivo
        self.id_tipo = id_tipo
        self.id_usuario = id_usuario  
    
    def encender(self):
        self.estado_dispositivo = True

    def apagar(self):
        self.estado_dispositivo = False

    def __str__(self):
        estado = "Encendido" if self.estado_dispositivo else "Apagado"
        return f"Dispositivo(ID: {self.id_dispositivo}, Nombre: {self.nombre_dispositivo}, Ubicación: {self.ubicacion}, Estado: {estado})"
