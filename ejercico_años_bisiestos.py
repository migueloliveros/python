def es_bisiesto(año):
    # Un año es bisiesto cuando es divisible por 4, me comenta chatgpt
    # pero no si es divisible por 100, a menos que también sea divisible por 400...no se si creer a esta máquina :-).
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Definimos rango de años
inicio = 1800
fin = 2100

print(f"Años bisiestos entre {inicio} y {fin}:")
for año in range(inicio, fin + 1):
    if es_bisiesto(año):
        print(año)
