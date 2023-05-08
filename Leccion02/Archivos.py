# MANEJO DE ARCHIVOS:
# Declaramos una variable
# Metodo open - Sirve para abrir archivos existentes o para crearlos. Tambien para leer y/o escribir en un archivo.and
# Si no existe lo crea. La W es para escribir. Write
# El archivo por default se crea en la carpeta donde estemos trabajando.
# Finalmente ejecutamos y se haran las modificaciones.
try:
    archivo = open('prueba.txt', 'w')
    archivo.write(
        'Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Con esto terminamos.')
except Exception as e:
    print(e)
finally:
    archivo.close()  # Con esto se debe cerrar el archivo
