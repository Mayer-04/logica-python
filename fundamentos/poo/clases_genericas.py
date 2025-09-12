# -------------------------------------
# * Genéricos en clases (Python 3.12+)
# -------------------------------------
# Los genéricos permiten definir clases que funcionan con diferentes tipos,
# manteniendo la verificación de tipos en tiempo de desarrollo y mejorando la
# legibilidad del código.
# sin necesidad de importar: `from typing import TypeVar, Generic`

class Caja[T]:
    """
    Representa una caja que almacena un valor de tipo genérico T.

    Parámetros del constructor:
        valor (T): El contenido que se guardará en la caja.

    Métodos:
        obtener() -> T:
            Retorna el valor almacenado en la caja.
        __repr__() -> str:
            Devuelve una representación legible de la caja.
    """
    def __init__(self, valor: T):
        self.valor = valor

    def obtener(self) -> T:
        """Retorna el valor almacenado en la caja."""
        return self.valor

    def __repr__(self) -> str:
        return f"Caja({self.valor!r})"


# Ejemplos de uso
caja_numeros = Caja[int](5)
print(caja_numeros.obtener())   # Salida: 5

caja_colores = Caja[str]("Negro")
print(caja_colores.obtener())   # Salida: 'Negro'

caja_lista = Caja[list[int]]([1, 2, 3])
print(caja_lista.obtener())     # Salida: [1, 2, 3]