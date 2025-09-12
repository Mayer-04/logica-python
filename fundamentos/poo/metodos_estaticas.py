# --------------------------
# * Métodos estáticos
# --------------------------


class Calculadora:
    # Método estático: No recibe 'self' ni 'cls'
    @staticmethod
    def sumar(a, b):
        """Suma dos números"""
        return a + b

    # Método de clase: recibe la clase como primer argumento
    @classmethod
    def descripcion(cls):
        """Descripción de la clase"""
        return f"Soy la clase {cls.__name__} y hago operaciones matemáticas."


print(Calculadora.sumar(5, 7))  # 12
print(
    Calculadora.descripcion()
)  # Soy la clase Calculadora y hago operaciones matemáticas.
