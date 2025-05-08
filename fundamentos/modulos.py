"""
* Módulos en Python
-------------------
Un módulo es un `archivo` Python que contiene código y definiciones de funciones, clases, variables, etc.
- Ayuda a reutilizar código de otros archivos.
- Este código puede ser importado en otro archivo Python para utilizar sus definiciones.

- import: Se usa para importar un módulo completo en tu programa.
- from: Se usa junto con import para importar algo específico de un módulo.
- as: Se usa para darle un nombre alternativo o alias a un módulo.
- Para importar algo específico de un módulo, se usa: `from módulo import nombre_función` o `from módulo import *`.
"""

# Importar el módulo `random`
import random

print(random.randint(1, 10))

# Importar el módulo `math` y dandole un alias `m`
import math as m

print(m.pi)

# Importar algo específico de un módulo, en lugar de importar el módulo completamente.
# Su traducción sería: "del módulo funciones importa saludar_con_titulo"
from funciones.funciones import saludar_con_titulo

saludar_con_titulo("Mayer")
