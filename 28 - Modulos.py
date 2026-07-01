# Modulos

"""
Un modulo es un archivo, externo a nuestro programa, que contiene funciones y variables que 
podemos utilizar en nuestro programa

Por ejemplo, podemos tener un modulo que contenga funciones para manejar archivos, otro para 
manejar fechas, otro para manejar numeros, etc.

Y estos podemos importarlos a nuestro script o programa principal.

Ejemplo:
"""

# ops.py

def addition(a, b):
    return a + b

# main.py

from ops import addition as add

print(add(1, 2))

"""
De esta manera, podemos importar la funcion addition del modulo ops y usarla como add en nuestro
programa principal.

Con as, podemos asignar un nombre alternativo a la funcion o variable que importamos.

Si lo omitimos, el nombre de la funcion o variable sera el mismo que el nombre del modulo.

Y asi con N cantidad de modulos y funciones que podemos importar a nuestro programa principal.
"""