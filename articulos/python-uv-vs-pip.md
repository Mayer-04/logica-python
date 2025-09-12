# Entornos virtuales y gestores de dependencias en Python: `pip` + `venv` vs. `uv`

Cuando trabajamos en Python, es fundamental **aislar las dependencias de cada proyecto** para evitar conflictos entre librerías. Tradicionalmente, esto se hace con **`venv`** y **`pip`**, pero han surgido alternativas modernas como **`uv`**, que prometen mayor velocidad, simplicidad y un flujo de trabajo más moderno.

A continuación, veremos cómo usar ambos enfoques, sus ventajas y principales comandos.

---

## ¿Qué es un entorno virtual?

Un **entorno virtual** es como una **caja aislada** donde instalamos las librerías de un proyecto sin que interfieran con otros.

**Ventajas:**

- Evita conflictos entre versiones de librerías.
- Permite reproducir proyectos en otros equipos fácilmente.
- Facilita la colaboración en equipo.

---

## Configuración con `pip` y `venv` (método tradicional)

### Crear un entorno virtual

```bash
python -m venv venv
```

- El flag `-m` le dice a Python que ejecute un módulo como si fuera un script.
- `-m venv`: busca el módulo llamado `venv` en la biblioteca estándar y lo ejecuta.

Esto genera una carpeta `venv` que contendrá todas las dependencias de tu proyecto.

### Activar el entorno virtual

- **En Visual Studio Code**:

  - Abre el buscador de comandos: `>Python: Select Interpreter`.
  - Selecciona el intérprete que muestre `('venv')`.
  - VS Code activará el entorno automáticamente.

- **En la terminal**:
  - Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

- Linux/macOS:

```bash
source venv/bin/activate
```

- Para salir, basta con:

```bash
deactivate
```

### Instalar dependencias con `pip`

```bash
pip install pandas numpy
```

Si quieres guardar y compartir dependencias:

```bash
pip freeze > requirements.txt
```

Y para instalarlas en otro entorno:

```bash
pip install -r requirements.txt
```

> Este método es el más usado y funciona en todos lados, pero puede ser más lento y requiere manejar varios archivos (`venv`, `requirements.txt`, etc.).

---

## Configuración con `uv` (método moderno y rápido)

[`uv`](https://github.com/astral-sh/uv) es un **gestor de dependencias ultrarrápido** escrito en Rust. Busca ser un reemplazo moderno de `pip`, `pip-tools` y `venv`.

### Inicializar un proyecto

```bash
uv init
```

Esto crea la estructura básica:

- `.python-version` → fija la versión de Python.
- `pyproject.toml` → archivo estándar moderno (PEP 518) para la configuración del proyecto. Aquí se definen nombre, versión, dependencias, autores, etc.
- `uv.lock` → equivalente a `requirements.txt`, pero con información más precisa de dependencias y subdependencias.
- `main.py`, `README.md`, `.gitignore`.

Si quieres que cree una carpeta de proyecto automáticamente:

```bash
uv init <nombre_directorio>
```

### Tipos de proyectos

- `--app` (por defecto) → aplicación ejecutable.
- `--lib` → cuando quieres crear una librería.

### Instalar dependencias

```bash
uv add pandas numpy
```

- Se crea un entorno virtual automático en `.venv`.
- Se actualiza `pyproject.toml` y `uv.lock`.

### Eliminar dependencias

```bash
uv remove pandas
```

### Sincronizar dependencias

```bash
uv sync
```

Garantiza que tu entorno y `uv.lock` estén alineados.

### Ver árbol de dependencias

```bash
uv tree
```

### Exportar dependencias

```bash
uv export > requirements.txt
```

### Ejecutar scripts del proyecto

```bash
uv run main.py
```

### Actualizar la versión instalada de `uv`

```bash
uv self update
```

### Ventajas de `uv`

- Mucho más rápido que `pip`.
- Maneja un **cache global** para ahorrar espacio.
- Unifica funciones que normalmente requieren varias herramientas (`pip`, `pip-tools`, `venv`, `requirements.txt`).
- Basado en el estándar moderno `pyproject.toml`, más limpio y sostenible.

---
