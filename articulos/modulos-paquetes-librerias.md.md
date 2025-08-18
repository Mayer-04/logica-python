# Conceptos importantes en Python

## 📦 Módulo

Un **módulo** es simplemente un archivo con extensión `.py` que contiene código de Python: **funciones**, **clases** o **variables** que puedes usar en otros archivos.

### ¿Para qué sirve?

Te ayuda a organizar tu código en partes reutilizables y fáciles de entender.

**Ejemplo:**

Supongamos que tienes un archivo llamado `saludos.py`:

```python
# saludos.py

def hola(nombre):
    print(f"¡Hola, {nombre}!")
```

Ahora, en otro archivo puedes usarlo así:

```python
# main.py
import saludos

saludos.hola("Ana")
```

**Consejo:** Usa **módulos** para evitar repetir código y mantener tus proyectos ordenados.

## 📁 Paquete

Un **paquete** es una carpeta/directorio que **agrupa varios módulos** relacionados. Para que Python la reconozca como paquete, debe tener un archivo llamado `__init__.py` (puede estar vacío).

**Estructura de ejemplo:**

```markdown
mi_paquete/
│
├── `__init__.py`
├── saludo.py
└── despedida.py
```

**¿Cómo se usa?**

```python
# saludo.py
def hola(nombre):
    print(f"¡Hola, {nombre}!")

# main.py
from mi_paquete import saludo

saludo.hola("Luis")
```

> [!NOTE]
> Los paquetes son útiles cuando tu proyecto crece y quieres dividirlo en partes más fáciles de manejar.

## 📚 Librería o Biblioteca

Una **librería** (también llamada biblioteca) es un **conjunto de módulos o paquetes** que ofrecen funcionalidades listas para usar, como trabajar con datos, hacer gráficos, crear sitios web, etc.

### Tipos de librerías

### Externas

No vienen con Python. Se instalan con herramientas como `pip`, `poetry`, `uv`, etc.

```bash
pip install pandas
```

**Ejemplos populares:**

- `Pandas`: manejo de datos en tablas (tipo Excel).
- `Requests`: hacer solicitudes a internet (APIs).
- `NumPy`: operaciones matemáticas y arreglos.
- `FastAPI`: construir APIs web.

### Nativas (o estándar)

Ya vienen con Python, no necesitas instalarlas.

> [!NOTE]
> Usa librerías para aprovechar el trabajo que ya hicieron otros programadores.

## ¿Qué es una librería nativa en Python?

Una **librería nativa** es parte de la _"biblioteca estándar"_ de Python. Son herramientas incluidas desde el primer momento que instalas Python.

**Características:**

- Listas para usar (sin instalar nada).
- Son oficiales y mantenidas por Python.
- Funcionan bien para muchas tareas comunes.

**Ejemplos de librerías nativas:**

| Librería      | ¿Para qué sirve?                                |
| ------------- | ----------------------------------------------- |
| `math`        | Funciones matemáticas                           |
| `os`          | Interacción con archivos y el sistema operativo |
| `json`        | Leer y escribir archivos JSON                   |
| `random`      | Números aleatorios                              |
| `datetime`    | Fechas y horas                                  |
| `collections` | Estructuras de datos avanzadas                  |

**Ejemplo utilizando una librería nativa:**

```python
import random

numero = random.randint(1, 10)
print(f"Número aleatorio: {numero}")
```
