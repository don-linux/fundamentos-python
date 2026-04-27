"""
Coleccion de pares clave-valor
Ordenados a partir de Python 3.7
"""

cafe = {
    "grano": "geisha",
    "pais": "colombia",
    "año": 2025,
}
print(cafe)


"""
Recorrer un diccionario

Buscar una clave en el diccionario
"""

if "grano" in cafe:
    print('Si hay!')

for k in cafe:
    print(k)

for v in cafe.values():
    print(v)

"""
Bucle anidado
"""
for k, v in cafe.items():
    print(k, v)


"""
Acceder a los valores del diccionario, usando corchetes 
para acceder a la clave y obtener el valor.
"""
print(cafe["pais"])

"""
Usando el metodo get()
"""
print(cafe.get("grano"))

"""
Imprimir las claves del diccionario
"""
print(cafe.keys())

"""
Imprimir los valores del diccionario
"""

print(cafe.values())


"""
Agregar un nuevo par clave-valor
"""
cafe["tostado"] = "Suave"
print(cafe)

"""
Actualizar un par clave-valor (claves existentes)
"""
cafe["año"] = 2020
print(cafe)

"""
Actualizar o agregar un par clave-valor con update()
"""
cafe.update({"año": 2022, "grano": "arabica"})


"""
Eliminar un par clave-valor
"""
cafe.pop("año")
print(cafe)

"""
Eliminar el ultimo par clave-valor
"""
cafe.popitem()
print(cafe)

"""
Eliminar todos los pares clave-valor
"""
cafe.clear()
print(cafe)

"""
Eliminar el diccionario completo
"""
#del cafe
#print(cafe)

"""
Diccionario anidado
"""
autos = {
    "tesla" : {
        "model" : "X"
    },
    "cybertruck" : {
        "model" : "Founders"
    }
}

print("Model", autos["tesla"]["model"])