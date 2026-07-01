# Try, Except y Finally

"""
Los errores en Python siempre ocurriran y como en todos los lenguajes, detienen la ejecucion del programa

Para esto fue creado try y except, para manejar los errores de una mejor manera

Este es un ejemplo muy sencillo de como funciona try-except:
"""

try:
    div = 10 / 0
except ZeroDivisionError:
    print("A number cannot be divided by zero")

"""
Aunque sabemos que una division por zero, no puede hacerse, puede que haya mas codigo que podamos ejecutar, entonces
Le pasamos al except el error que esperamos, y que nos devuelva, en este caso en consola, un mensaje que nos indique el error

Pero que permita aun asi la ejecucion del resto del programa

De no ponerlo, simplemente el programa se detiene
"""


"""
Para un script corto, no puede ser tan util

Pero programas grandes o aplicaciones web que no deberian detener su ejecucion muy facilmente, es importante tener una o muchas
alternativas para seguir con la ejecucion del programa
"""

try:
    print(name)
except NameError:
    name = "Freddy"
    print("The name of the variable hasn't been defined, defaulting the variable name to 'Freddy'")
    print(name)
finally:
    print("This print will be executed always, even the code is passing or failing")

"""
Aqui el error sucede, pero le ofrecemos al usuario un default, y listo, el programa falla, pero lo arreglamos en runtime
"""