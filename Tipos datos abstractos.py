#Tipos datos abstractos:

#*Listas
#*Tuplas
#*Diccionarios

lista = [1,2,3,4]
palabras = ["alpha", "charlie", "delta","foxtrot"]
type(lista)

lista[0]
#1

temperatura = [1, 3, 0.6, 0]
temperatura
temperatura_media = sum(temperatura) / len(temperatura)
temperatura_media

#Operaciones con secuencias (array)
palabras.index("bravo")
palabras
palabras.append("echo")

#añadir palabra al final de la lista
palabras.pop()
palabras[2]="foxtrot"
palabras
['delta', 'charlie', 'foxtrot', 'alpha']

#apilamiento elementos
type(cola)
list
type(pila)
list

pila = []
pila.append(6)
pila.append (5)
pila.append(8)

pila.pop()
8

#cola (que)
cola = []
cola.append(6)
cola.append (5)
cola.append(8)

cola.pop()
8

#join
palabras = ["alpha", "Charlie"]
"+".join(palabras)

#https://xkcd.com/

#split
palabras = msg.split()
print(palabras)
datos = "3,4,1,2,3,4,2,3,1"
datos.split(',')

#.format (f)
#format string syntax=https://docs.python.org/3/library/string.html#formatstrings
area = 6.1111111111111
perimetro = 7.555555555555
print("El area es", round(area,4), "n^2 y el perimetro es", round(perimetro, 4), "n")

print(f"El area es {area:.4f} m^2


