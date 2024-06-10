#
# Funciones en Python
#

def siguiente_numero(x):
    '''
    Función para calcular el número siguiente x.
    '''
    return x + 1

y = siguiente_numero(6)

def area_triangulo(baxse, altura):
    '''
    Calcula el área de un triángulo dada su base y altura
    '''
    return base * altura / 2

#Calcular notas, basado en diccionarios.

def calcular_nota_final(**notas):
    '''
    Calcula la nota final con o sin recuperación.
    Debe indicarse el parámetro final = y/o recuperaciones=.
    '''
    nota = 0
    if 'final' in notas:
        nota = notas['final']
    if 'recuperacion' in notas and notas['recuperacioj'] > nota:
        nota = notas['recuperacion']
    return nota


    
