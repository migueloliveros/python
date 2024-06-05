import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

# Ejemplo de uso:
radio = 5  # Puedes cambiar este valor por el radio que desees
area = calcular_area_circulo(radio)
print(f"El área de un círculo con radio {radio} es {area:.2f}")
