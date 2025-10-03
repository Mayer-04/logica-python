"""
Escribe un programa que muestre los números del 1 al 100, pero aplicando las siguientes reglas:

- Si el número es múltiplo de 3, mostrar "Fizz".
- Si el número es múltiplo de 5, mostrar "Buzz".
- Si el número es múltiplo de 3 y 5 a la vez, mostrar "FizzBuzz".
- En los demás casos, mostrar el número.

Salida esperada: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, ...
"""

for num in range(1, 101):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


multiplos = {15: "FizzBuzz", 3: "Fizz", 5: "Buzz"}

for num in range(1, 101):
    salida = ""

    for divisor, palabra in multiplos.items():
        if num % divisor == 0:
            salida = palabra
            break

    # print(salida if salida else num)

    if salida:
        print(salida)
    else:
        print(num)
