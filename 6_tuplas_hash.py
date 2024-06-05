#Listas vs. tuplas

Tupla es inmutable, es una secuencia de valores que se define
con parentesis y no corchetes. Immutable Sequence Types
el hash es una huella de actilar de lo que es un objeto, mapea un número entero....

hash (). Es una funcion tal que dos objetos a y b que contienen lo mismo(mismo contenido),dan el muismo hash.
Son números enteros. Existe posibilidad remota que dos objetos diferentes den un mismo hash.

tupla = {1, 2, 3, 4, 5}
tupla[0]
1
tupla[3]
4
tupla[-1]
5
#No se puede hacer
#tupla{2} = 8

hash("algo")
-34848437475483839393
hash("AlGo")
-28467484848493923923

hash(tupla) == hash(tupla3)
True

tupla == tupla3
True

lista_a = [1, 2, 3]
lista_b = [1, 2, 3]
#Esto no se puede hacer; hash(lista_a)

lista_a == lista_b
True

#Ejemplo
días_meses = {
    'enero': 31,
    'febrero': 28,
    'marzo': 31,
    'abril': 30,
    'mayo': 31,
    'junio': 30,
    'julio': 31,
    'agosto': 31,
    'septiembre': 30,
    'octubre': 31,
    'noviembre': 30,
    'diciembre': 31

d = {(1,2,3):3 (4,5):6}
len(dias_meses)
dias_meses.keys()
sum(dias_meses.values())
dias_meses.items()
    'juan' in dias_meses
    #False

#Operaciones genéricas
    lambda :se utiliza para definir un predicado para procesar cada elemento de x.
    Que transformación hacemos en cada elemneto.
    En honor al cálculo Lambda.

x = [5, 4, 2, 6, 4]
    x_cuadrado = map(lambda x:x**2, x)
    print(list(x_cuadrado))

    #[25, 16, 4, 36, 16]
    
sorted(x)
min(x)
max(x)
    
    



