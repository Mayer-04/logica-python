"""
* Módulos y paquetes en Python
-------------------------------
Un módulo es un "archivo" .py que contiene código Python como funciones, clases, variables, etc.

- Ayuda a organizar y reutilizar código en diferentes programas.
- Este código puede ser importado en otro archivo Python para utilizar sus definiciones.

Paquetes
---------
Un paquete es una directorio que contiene varios módulos y un archivo especial llamado '__init__.py'.

- `import:` Se usa para importar un módulo completo en tu programa.
- `from:` Se usa junto con 'import' para importar algo específico de un módulo.
- `as:` Se usa para darle un nombre alternativo o alias a un módulo.
- Para importar algo específico de un módulo, se usa:
  `from modulo import funcion` o `from modulo import *`.
  
  
Buenas prácticas
-----------------
- Prefiere `from módulo import función` si solo necesitas una parte.
- Usa as para acortar nombres largos: import pandas as pd
  
Malas prácticas
---------------- 
- Importar todo de un módulo: `from modulo import *`.
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

# Importar varios módulos.
import math, sys
