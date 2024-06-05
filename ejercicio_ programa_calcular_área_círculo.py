# Programa para calcular el área de un círculo.
# El programa solicita al usuario el radio del círculo y calcula su área y su perímetro.
# Finalmente mostrará por la consola o terminal el resultado de los cálculos.

import math

# 1. Toma de datos

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 2. Solicitar al usuario el radio del círculo

radio = float(input("Introduce el radio del círculo: "))

# 3. Cálculo del área y el perímetro

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# 4. Mostrar resultados

print(f"El área del círculo con radio {radio} es {area:.2f}")
print(f"El perímetro del círculo con radio {radio} es {perimetro:.2f}")





