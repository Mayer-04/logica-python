import platform

"""
CPython es la implementación de Python más utilizada, la más rápida y la más madura.

- Tanto el intérprete como los módulos están escritos en el lenguaje de programación C.
- El código que escribes en Python no se traduce directamente a C. Se compila a un formato `bytecode`.
- El código Python al interpretarse, lo interpreta algo hecho con C pero no traduce a C.
- CPython está instalado por defecto en la mayor parte de las distribuciones Linux y en las últimas versiones 
de MacOS como de Windows.
"""

# Verificar la implementación de Python que estamos usando.
print(platform.python_implementation())  # Salida: CPython
