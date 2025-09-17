from abc import ABC, abstractmethod

# -------------------------
# * Interfaces en Python
# -------------------------
# En Python no existen "interfaces" como en otros lenguajes de programación,
# pero podemos simularlas usando clases abstractas (ABC).
#
# - No puedes crear (instanciar) directamente la clase abstracta.
# - Cualquier clase hija está obligada a implementar TODOS los métodos abstractos.
# - Es útil en patrones de diseño como Repository, DAO, Service, Adapter, Strategy, etc.


class Repository(ABC):
    """Interfaz que define operaciones básicas para trabajar con datos."""

    @abstractmethod
    def save(self, data: dict) -> None:
        """
        Guarda un registro.

        Args:
            data (dict): Información que se quiere almacenar.

        Ejemplo:
            {"id": 1, "nombre": "Juan"}
        """
        pass

    @abstractmethod
    def search(self, query: dict) -> dict:
        """
        Busca un registro a partir de una consulta.

        Args:
            query (dict): Condiciones de búsqueda.

        Returns:
            dict: Registro encontrado o un diccionario vacío si no existe.

        Ejemplo:
            query = {"id": 1}
            return {"id": 1, "nombre": "Juan"}
        """
        pass
