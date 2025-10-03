"""
Diferencia de Sumas Divisibles y No Divisibles
------------------------------------------------

Se te dan dos enteros positivos `n` y `m`.
Debes definir dos números de la siguiente forma:

- num1: la suma de todos los enteros en el rango [1, n] (incluyendo ambos extremos) que NO sean divisibles
por `m`.

- num2: la suma de todos los enteros en el rango [1, n] (incluyendo ambos extremos) que SÍ sean divisibles
por `m`.

El resultado final será el entero num1 - num2.

Ejemplo 1:
------------
Entrada: n = 10, m = 3
Proceso:
- Números entre 1 y 10 que no son divisibles por 3: [1,2,4,5,7,8,10] → suma = 37.
- Números entre 1 y 10 que sí son divisibles por 3: [3,6,9] → suma = 18.

Resultado = num1 - num2 = 37 - 18 = 19.

Salida: 19

Ejemplo 2:
-----------
Entrada: n = 5, m = 6
Proceso:
- Entre 1 y 5, ninguno es divisible por 6.

Entonces:
----------
No divisibles = [1,2,3,4,5] → suma = 15.
Divisibles = [] → suma = 0.
Resultado = 15 - 0 = 15.

Salida: 15

Ejemplo 3:
-----------
Entrada: n = 5, m = 1
Proceso:

Todo número es divisible por 1.

Entonces:
----------
No divisibles = [] → suma = 0.

Divisibles = [1,2,3,4,5] → suma = 15.

Resultado = 0 - 15 = -15.

Salida: -15
"""
