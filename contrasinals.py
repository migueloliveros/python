#
#Random Passwords - Xerador de contrasianis
#https://docs.python.org/3/library/random.html#module-random

import random

#Definimos lista de palabras candidatas para las contraseñas
palabras = ['casa', 'can', 'gato', 'cadro', 'boligrafo', 'rato', 'gafas']

#Obtenemos lista 3 palabras elegidas al azar
eleccion = random.choices(palabras, k=3)

#Juntamos palabras de la lista
contrasinal = "-".join(eleccion)

#Mostramos resultado
print(contrasinal)
