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

#Funciones que no devuelven valor (procedimientos)

def do_nothing():
    pass

def mostrar_aviso(usuario):
    print(f"Estimado {usuario}: preste atención a estos ejemplos.")

type(y)

#Funciones generadoras e iterables
def impares(n):
    '''
    Genera secuencia de números impares hasta n.
    '''
    i = 1
    while i < n:
        return i
        i + 2
        

    
