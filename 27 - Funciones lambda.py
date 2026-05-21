"""

Lambda es una funcion pequeña y anonima

Que puede tener muchos argumentos pero solo una expresion.

Sintaxis:
lambda argumentos: expresion
"""

x = lambda a : a + 10

print(x(5))

"""
El print toma la variable x, la cual contiene la funcion lambda
Le pasa el argumento 5, el cual es el valor que toma a en la funcion lambda
Entonces a + 10 se convierte en 5 + 10 = 15
Y el resultado se imprime

Multiples argumentos:
"""

x = lambda a, b : a * b

print(x(5, 6))

"""
El print pasa los argumentos 5 y 6 a la funcion lambda

Fabrica de funciones:
"""

def myfunc(n):
    return lambda a : a * n

double = myfunc(2)
triple = myfunc(3)

print(double(5))
print(triple(2))