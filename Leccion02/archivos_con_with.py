
from ManejoArchivos import ManejoArchivos
# MANEJO DE CONTEXTO WITH
# with open('prueba.txt', 'r', encoding='utf8') as archivo:
# De manera automatica abre el arcivo y lo cierra
# print(archivo.read())
# No hace falta ni el try ni el finally
# En el contexto de with lo que se ejecuta de manera automatica
# Utiliza diferentes metodos: __enter__ este es el que abre
# Ahora el siguiente metodo es el que cierra: __exit__
# Sin embargo nosotros tambien podemos programar nuestro propio manejo de recursos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
