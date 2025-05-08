"""
* Operadores de comparación
---------------------------
- Se utilizan para comparar dos valores.
- Puedes encadenar múltiples comparaciones en una sola expresión
- Cuando `encadenas comparaciones`, Python evalúa cada comparación en orden y verifica si todas son verdaderas.
- Si todas las comparaciones son verdaderas, Python devuelve `True` por el contrario, `False`.
"""

# Igualdad
print(1 == 1)  # True
print(1 == 2)  # False

# Desigualdad o diferente
print(1 != 1)  # False

# Mayor que
print(1 > 1)  # False

# Menor que
print(1 < 1)  # False

# Mayor o igual que
print(1 >= 1)  # True

# Menor o igual que
print(1 <= 1)  # True

# Encandenar comparaciones
# 1 < 2 and 2 < 3
print("Encadenar comparaciones:", 1 < 2 < 3)  # True
