#
#Estadísticas

#Toma de datos de entrada. Los datos se almacenan
#inicialment en la variable de datos tipo str.
#Estos datos hay que separarlos y convertirlos a float.

datos = input("Introduce las muestras, separadas por espacios:")
muestras = datos.split()

X = list(map(lambda x:float(x), muestras))

#Procesamiento de datos
numero_muestras = len(X)
suma = sum(X)
media = suma / numero_muestras
esperanza2_x = media**2
esperanza_x2 = sum(map(lambda x:x**2, X))/numero_muestras
varianza = esperanza_x2 - esperanza2_x

#Mostrar resultados
print(f"Número de muestras: {numero_muestras}")
print(f"Suma: {suma:g}")
print(f"Media: {media:g}")
print(f"Varianza: {varianza:g}")


#https://pypi.org/
