# ¿Qué es CPython?

`CPython` es la implementación oficial y más ampliamente utilizada del lenguaje de programación Python. Está desarrollada y mantenida por la _Python Software Foundation_.

## ¿Qué significa CPython?

CPython está escrita principalmente en el `lenguaje C`, de ahí su nombre **("C" + "Python")**. Esto incluye:

- El intérprete que ejecuta los programas (código) escritos en Python.
- Muchos de los módulos estándar, aunque algunos otros están escritos en Python puro.

## ¿Cómo funciona?

Cuando ejecutas un archivo `.py`, no se convierte directamente en código máquina ni en código C. El proceso funciona así:

1. El código Python se compila a un formato intermedio llamado **bytecode**.
2. Ese **bytecode** es luego interpretado por la máquina virtual de CPython, que está escrita en C.

> [!IMPORTANT]
> Aunque Python se ejecuta gracias a un motor en C, tu código no se transforma en C durante la ejecución.

## ¿Es CPython la versión más rápida?

No necesariamente. **CPython** es la más estable y compatible, pero existen otras versiones enfocadas en el rendimiento, como:

- `PyPy`, que utiliza técnicas de compilación JIT (_Just-In-Time_) para ejecutar programas más rápido en muchos casos.

## ¿Dónde se encuentra instalado?

- En Linux, CPython suele venir preinstalado.
- En macOS, también viene incluido, pero se recomienda usar herramientas como **Homebrew** para instalar una versión más actualizada.
- En Windows, sin embargo, no viene incluido por defecto, pero su instalación es sencilla desde la Microsoft Store o el sitio oficial de Python.
