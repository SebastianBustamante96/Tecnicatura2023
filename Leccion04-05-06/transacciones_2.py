import psycopg2
# Creamos el objeto de tipo conexion para conectarnos a postgresql
conexion = psycopg2.connect(user='postgres', password='admin',
                            host='127.0.0.1', port='5432', database='test_bd')

# https://www.psycopg.org/docs/usage.html - Psycopg 2.9.6 documentation
try:
    conexion.autocommit = False  # Inicia la transaccion
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s,%s,%s)'
    valores = ('Ruben', 'Santos', 'rsantos@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Gonzalo', 'Sanchez', 'gsanchez@mail.com', 9)
    cursor.execute(sentencia, valores)
    conexion.commit()  # Hacemos el commit manualmente. Cierra la transaccion
    print('Termina la transaccion')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')

finally:
    conexion.close()
