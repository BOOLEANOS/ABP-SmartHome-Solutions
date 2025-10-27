from abc import ABC, abstractmethod

class IDispositivoDAO(ABC):
  
    @abstractmethod
    def crear_dispositivo(self, dispositivo, id_usuario):
        """Crea un nuevo dispositivo en la base de datos."""
        pass

    @abstractmethod
    def obtener_todos_por_usuario(self, id_usuario):
        """Obtiene todos los dispositivos de un usuario."""
        pass

    @abstractmethod
    def obtener_por_id(self, id_dispositivo):
        """Obtiene un dispositivo por su ID."""
        pass

    @abstractmethod
    def actualizar_dispositivo(self, dispositivo):
        """Actualiza los datos de un dispositivo existente."""
        pass
      
    @abstractmethod
    def eliminar_dispositivo(self, id_dispositivo):
        """Elimina un dispositivo según su ID."""
        pass

    @abstractmethod
    def obtener_tipos_dispositivos(self):
        """Obtiene los tipos de dispositivos disponibles."""
        pass
