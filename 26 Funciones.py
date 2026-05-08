"""
Funcion

Es un bloque de codigo que se ejecuta cuando se le llama.

Permite modularizar el codigo y organizar el codigo en bloques

Una funcion esta compuesta por

Argumentos, que es el codigo con el que trabaja la funcion
Parametros: El codigo que se envia a la funcion
"""

            # Argumentos
def salute(name, last_name='', nationality='world'):
    print('Hi', name, last_name, 'from', nationality)

salute('Fer', 'Diaz', 'Mexico') # Parametros
salute('Fercho')

"""
Una funcion puede devolver resultaods
"""

def sum(a, b):
    print(a + b)

def sum(a, b):
    return a + b
    
sum(5,5)

"""
Asignacion de variable
"""
x = sum(2,2)

print(x)

def myfunc():
    pass