from NumerosIgualesException import NumerosIgualesException
resultado = None

try:
    a = int(input("Digite el primer numero: "))
    b = int(input(("Digite el segundo numero: ")))
    if a == b:
        raise NumerosIgualesException('Son numeros iguales') #raise nos permite arrojar una excepcion
        #Si son numeros iguales no los divide. Esta es una excepcion personalizada
    resultado = a / b 
except TypeError as e: #Un TypeError puede ser lanzado cuando: 
    #Un operando o argumento pasado a una función es incompatible con el tipo esperado por el operador o función
    print(f'TypeError-Ocurrio un error: {type(e)}')
except ZeroDivisionError as e:#Este error se produce cuando realizamos una división entre dos números y el resultado es cero
    print(f'ZeroDIvisionError - Ocurrio un error: {type(e)}')
except Exception as e: #Usamos la clase padre Exception, la cual es abarcativa. Va al final o se usa sola
    print(f'Ocurrio un error: {e}')
else:
    print('No se arrojo ninguna excepcion')
finally:
    print('Ejecucion de este bloque finally')#El finally siempre se ejecutar
print(f'El resultado es: {resultado}')
print('seguimos...')