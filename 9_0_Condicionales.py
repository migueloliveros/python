#Estructuras condicionales

#Estructura sintáctica 'if'
#Cláusula else
#Cláusula elif

#Estructura sintáctica 'if'

condicion = True

if condicion:
    print("Estamos precensiando algo interesante")

condición = False

if condicion:
    print("Esto no va a pasar")

x = 3
if x < 5
    print("x es pequeño")

if x > 10 or not condicion:
    print("Puede ser")

#Cláusula else
#Cláusula elif
#int convierte a un número entero

temperatura = int(input("Escriba un número -> "))
if x < 5:
    print("x ten un valor pequeño")
else
    print("x tiene un valor grande")

#float convierte a un número decimal
    
temperatura = float(input("Celsius: "))
if temperatura < 15:
    print("frio")
elif temperatura > 15:
    print("calor")
else:
    print("Temperatura agradable")

#Bucles repetición 'while'

numero = 10
while numero > 0:
    numero = numero - 1 #Decrimento de una unidad
    print(numero)
    
print ('Lanzamiento')

#Bucle 'for' - Ideal para secuencias.

#contar secuencialmente de 0 a 19
for i in range(20):
    print(i, end=" ")
    
#print secuencialmente comandos
lista1 = ["alpha", "bravo", "charlie", "delta"]

for p in lista1:
          print(p.capitalized())

#secuencia Fibonacci

a = 0
b = 1
while a < 1000:
    c = a + b
    print(a, end=" ")
    #print(a, b, c)
    #yield
    #yield si se realiza función
    a, b = b, c

#funcion Fibonacci
for n in fibonacci(100):
    print(n)
    
#f = fibonacci(20)


