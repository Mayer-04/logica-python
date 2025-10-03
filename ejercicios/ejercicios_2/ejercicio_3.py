"""
Escribe una función que determine si una palabra o frase es un palíndromo.
Un palíndromo se lee igual de izquierda a derecha y de derecha a izquierda, ignorando espacios,
signos de puntuación y mayúsculas/minúsculas.

Ejemplos:
----------
- "Anita lava la tina" → es un palíndromo.
- "Oso" → es un palíndromo.
- "Python es genial" → no es un palíndromo.

Pasos sugeridos:
-----------------
1. Convertir todo a minúsculas
2. Eliminar espacios y signos de puntuación
3. Comparar la cadena con su reverso
"""


def determinar_palindrome(palabra: str) -> bool:
    limpieza_palabra = palabra.lower().replace(" ", "").strip()
    palabra_invertida = "".join(reversed(limpieza_palabra))
    return limpieza_palabra == palabra_invertida


def es_palindromo(palabra: str) -> bool:
    limpieza_palabra = palabra.lower().replace(" ", "").strip()
    return limpieza_palabra == limpieza_palabra[::-1]


def is_palindrome(word: str) -> bool:
    palabra = ""
    for w in word:
        if w != " ":
            palabra += w

    limpiar_palabra = palabra.lower().strip()

    palabra_invertida = ""
    for i in range(len(limpiar_palabra) - 1, -1, -1):
        palabra_invertida += limpiar_palabra[i]

    return limpiar_palabra == palabra_invertida


print(is_palindrome("Anita lava la tina"))
print(is_palindrome("Oso"))
print(is_palindrome("Python es genial"))
