#
# Simulador lotería
#
import random

#Funcion

def loteria():
    '''
    Generador secuencias oteria
    Son combinaciones de 6 bolas de un total de 49
    '''
    combinacion = set()

    while len(combinacion) < 6:
        numero = random.randint(1, 49)
        combinacion.add(numero)

    for numero in sorted(combinacion):
        yield numero

for n in loteria():
    print("Combinacion ganadora", n)
