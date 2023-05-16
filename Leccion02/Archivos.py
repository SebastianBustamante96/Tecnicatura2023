# MANEJO DE ARCHIVOS:
# Declaramos una variable
# Metodo open - Sirve para abrir archivos existentes o para crearlos. Tambien para leer y/o escribir en un archivo.and
# Si no existe lo crea. La W es para escribir. Write
# El archivo por default se crea en la carpeta donde estemos trabajando.
# Finalmente ejecutamos y se haran las modificaciones.

try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write(
        'Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('Como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Con esto terminamos.')
    archivo.write(
        '\nLas letras son:\n r read - leer\n a append - anexa\n w write - escribe\n x - crea un archivo')
    archivo.write(
        '\nt para texto o text, \nb para archivos binarios, \nw+ escribe y lee, \nr+leer y escribir')
    

except Exception as e:
    print(e)
finally:  # Siempre se ejecuta
    archivo.close()  # Con esto se debe cerrar el archivo
