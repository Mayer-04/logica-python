# Variables

En Python, una variable no es más que un `nombre` que hace referencia a un `objeto` en memoria. Cuando creas una variable, en realidad estás creando una **referencia** a un valor almacenado en una ubicación específica de la memoria, no almacenando el valor directamente.

**Veamos un ejemplo:**

```py
# Creamos una variable llamada "cantidad"
cantidad = 5
```

1. **Evaluación:** Python primero evalúa la `expresión` a la derecha del signo igual (=), en este caso, el número 5.
2. **Creación del Objeto:** Dado que 5 es un número entero, Python crea un `objeto de tipo int` que almacena este valor.
3. **Asignación:** Este `objeto int` que contiene el valor 5 se almacena en una ubicación específica de la memoria. Luego, Python asigna la variable cantidad para que apunte a esa dirección de memoria.
4. Cuando decimos que cantidad `apunta` a una dirección de memoria, simplemente estamos diciendo que `cantidad` es una `etiqueta` o nombre que señala dónde está guardado el valor 5 en la memoria de la computadora.
5. **Reutilización:** Si asignas el valor 5 a otra variable, Python podría reutilizar el objeto existente en lugar de crear uno nuevo. Esto es posible gracias a una técnica llamada "interning" o "internado" en Python.

Esto significa que las variables en Python no contienen los datos directamente, sino que actúan como `punteros` a objetos en memoria.

## Interning o Internado

El `interning` es una técnica en Python que optimiza el uso de la memoria al reutilizar objetos `inmutables` que tienen el mismo valor, en lugar de crear nuevos objetos cada vez que se usa un valor idéntico. Esta técnica es comúnmente utilizada con números enteros, cadenas de caracteres y algunas tuplas.

**Beneficios:**

- Al reutilizar objetos, se evita la creación de múltiples instancias de objetos idénticos, lo que ahorra memoria.
- Reutilizar objetos ya existentes puede acelerar las operaciones, ya que no es necesario crear y almacenar nuevos objetos para valores idénticos.

- **NOTA:** Puedes _forzar_ el interning manualmente para cadenas de caracteres utilizando la función `intern()` del `módulo sys` (esto fue común en versiones anteriores de Python 3.9).

**Ejemplos:**

```py
# Números enteros
numero = 78900
numero2 = 78900
print(numero is numero2)  # True
print(id(numero))  # 2547033022640
print(id(numero2))  # 2547033022640

# Cadenas de caracteres
nombre = "Mayer"
nombre2 = "Mayer"
print(nombre is nombre2)  # True
print(id(nombre))  # 2259066708368
print(id(nombre2))  # 2259066708368

# Tuplas
cuidades = ("Bogotá", "Medellín", "Cali", "Pasto")
cuidades2 = ("Bogotá", "Medellín", "Cali", "Pasto")
print(cuidades is cuidades2)  # True
print(id(cuidades))  # 2090137619408
print(id(cuidades2))  # 2090137619408
```

## Contador de referencias

Cada vez que creas un objeto **(como un número, una cadena, una lista, etc.)**, Python necesita saber cuántas variables o `referencias` están apuntando a ese objeto. Este conteo ayuda a determinar cuándo un objeto ya no es necesario y puede ser eliminado para liberar memoria.

**Funcionamiento del Contador de Refencias:**

1. **Inicialización:** Al crear un nuevo objeto, Python establece su contador de referencias en 1.
2. **Aumento:** Cada vez que se crea una nueva referencia a este objeto (por ejemplo, al asignar el objeto a una nueva variable), el contador aumenta.
3. **Disminución:** Si una referencia al objeto se elimina (por ejemplo, al reasignar la variable o al usar `del`), el contador disminuye.
4. **Recolección de Basura:** Cuando el contador de referencias llega a 0, significa que ninguna variable o referencia está apuntando a ese objeto. Python lo considera "innecesario" y libera la memoria que estaba ocupando 1.

**Ejemplo:**

```py
# Creamos un número entero
# El contador de referencias para el `objeto 11` es 1
numero = 11
print(f"ID de numero: {id(numero)}")  # 140705818737400

# Asignamos la misma referencia a otra variable `otro_numero`
# El contador de referencias para el `objeto 11` ahora es 2
otro_numero = numero
print(f"ID de otro_numero: {id(otro_numero)}")  # 140705818737400

# Reasignamos la variable 'otro_numero' a un nuevo número
# El contador de referencias para el `objeto 11` disminuye a 1
# `El objeto 4` ahora tiene un contador de referencias de 1
otro_numero = 4
print(f"ID de otro_numero: {id(otro_numero)}")  # 140705818737176

# Finalmente, eliminamos la variable 'numero'
del numero

# El contador de referencias para el `objeto 11` llega a 0.
# Python libera la memoria ocupada por el número 11.
```
