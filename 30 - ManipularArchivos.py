"""
open(nombreArchivo, modo)

R = Read - Lectura
W = Write - Escribe o sobreescribe en archivos existentes
X = Execute - Crea archivos nuevos, si existe, genera un error
"""

try:
    f = open("file.txt", "r")
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("File not found")