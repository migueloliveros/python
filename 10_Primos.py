#
# Obtener números primos
#
MAX=100
contador = 0

#Recorremos todos los números entre 2 y MAX (no inclu.)
for n in range(2, MAX):
    #Empezamos asumiento que n pruede ser primo
    es_primo = True
    
    # Comprobamos si tiene divisores 
    for k in range(2, n):
        #Si el resto de dividir n entre k da 0, no es primo
        if n % k == 0:
            es_primo = False
            
    # Si no hubo divisores, es que es primo y lo ejecutamos:
    if es_primo:
        print(n)

print("Operaciones realizadas: ", contador)

#break - interrupción bucle

for i in range(10):
    if i > 6:
        break
    print(i)

#continue - salto siguiente 
    
  for i in range(10):
    if i > 6:
        continue
    print(i)

x 0 1500
while True:
    print(x)
    x /= 2 # equivale a: x = x / 2
    if x < 0.1: break


    
