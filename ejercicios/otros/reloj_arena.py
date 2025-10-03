"""
Reloj de arena de índices en una lista de strings
---------------------------------------------------
Enunciado: Dada una lista de palabras, recórrela formando un “reloj de arena”: avanza desde el primer
elemento al último, luego retrocede desde el penúltimo al segundo.
Concatenar las palabras en el orden visitado y devolver el string final.
Si la lista tiene 0 o 1 elementos, devolverla tal cual.

Explicación: Este patrón evita repetir los extremos al retroceder, por lo que debes manejar cuidadosamente
los rangos y condiciones de parada.
Es un buen ejercicio para pensar en recorridos no lineales y concatenación eficiente de strings.
Considera listas muy pequeñas y muy grandes, y evalúa si usar join frente a concatenaciones sucesivas.

Restricciones: No uses slicing inverso directo para todo el recorrido;
construye el patrón con bucles explícitos.

Casos de prueba:
-----------------
reloj_de_arena(["sol", "luna", "mar", "cielo"]) -> "sollunamarcielomarluna"

reloj_de_arena(["a"]) -> "a"

reloj_de_arena([]) -> ""

reloj_de_arena(["uno", "dos", "tres"]) -> "unodostresdos"

reloj_de_arena(["x", "y", "z", "w", "v"]) -> "xyzwvwzy"
"""


def formar_reloj_arena(palabras: list[str]) -> str:
    if len(palabras) == 0:
        return ""

    if len(palabras) == 1:
        return palabras[0]

    reloj_arena = ""
    # reloj_arena = "".join(palabras)
    for i in range(len(palabras)):
        reloj_arena += palabras[i]

    for i in range(len(palabras) - 2, 0, -1):
        reloj_arena += palabras[i]

    return reloj_arena


print(formar_reloj_arena(["sol", "luna", "mar", "cielo"]))
print(formar_reloj_arena(["a"]))
print(formar_reloj_arena([]))
print(formar_reloj_arena(["uno", "dos", "tres"]))
print(formar_reloj_arena(["x", "y", "z", "w", "v"]))
