from abc import ABC, abstractmethod

class IUsuarioDAO(ABC):
  
    @abstractmethod
    def registrar_usuario(self, nombre, email, password):
        """Registra un nuevo usuario en la base de datos."""
        pass

    @abstractmethod
    def iniciar_sesion(self, email, password):
        """Inicia sesión y retorna el usuario."""
        pass

    @abstractmethod
    def modificar_rol_usuario(self, email, nuevo_rol):
        """Modifica el rol de un usuario."""
        pass
