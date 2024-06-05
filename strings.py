#cadenas de texto o cadenas de caracteres
PONER PRINT

msg = ("el veloz murciélago hindu comí feliz cardillo y kiwi")
print = msg
type(msg)

#print(msg._class_)

#Operaciones con strings
#https://docs.python.org/3/library/stdtypes.html#str

#msg.capitalize()
#msg.title()
#msg.upper()
#msg.lower()

#len(msg)

a = "Un texto"
b = "Otro texto"
a.upper()
b.lower ()
len(a)
len(b)

#Conversión de objetos

msg[0]
"e"
msg[1]
msg[-2]
#Slice
msg[0:6]
'el vel'

#ejemplo con NIF

nif = "00000001R"
numero = nif[0:8]
letra  nif (-1)
print(numero, letra)

msg[0:40:2]
msg[::-1]
msg.startswith("el veloz")
#true
msg.endswith("kiwi")
#true
msg.find("feliz")
msg[32:]
msg.find("el")
msg.rfind("el")
"cardillo" in msg
#True
"CARDILLO" in msg
#False

#Conversión de objetos a str
num = 3
type(num)
nums = str(num)
nums
type(nums)

#Ejemplo
a = 5
b = 3.4

s = a * b
print("El área de la figura es" + str(s) + "metros cuadrados"))
#El área de la figura es 19.04 metros cuadrados

#Repeticion
"Hola" * 3
#Concatenación
"unir" + "partes"
