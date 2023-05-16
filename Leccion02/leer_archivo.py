# 'r' read, 'a' append, 'w' write, 'x'
# En caso de no trabajar en la misma carpeta se debe especificar donde esta el archivo "c:/prueba.."
archivo = open('prueba.txt', 'r', encoding='utf8')  # r - Read
# print(archivo.read())
# print(archivo.read(16))  # Nos muestra los 16 primeros caracteres
# Nos muestra los 10 primeros caracteres despues del primer pedido
# print(archivo.read(10))
# Nos muestra la linea entera desde el pedido anterior
# print(archivo.readline())

# vamos a iterar el archivo, cada una de las lineas
# for linea in archivo:
# print(linea)

# print(archivo.readlines()) accedemos al archivo como si fuera una lista
# Anexamos informacion, copiamos a otro
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()  # cerramos el primer archivo
archivo2.close()  # cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos ')
