#Funciones lógicas sobre listas

all()
any()

#Conjuntos
#Set y Frozen sets.

len(s)
x in s
x not in s

a = {'alpha', 'charlie', 'delta'}
b = {'bravo', 'charlie'}
c = {'charlie', 'delta'}

type(a)
'bravo' in a
'bravo' in b
c < a
a < b
a - c

#Añadir elemnetos
a.add('foxtrot')

#Se puede hacer un conjunto de tuplas, pero no de listas ya que
#tiene que ser hasheable

