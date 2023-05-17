import psycopg2
# Creamos el objeto de tipo conexion para conectarnos a postgresql
conexion = psycopg2.connect(user='postgres', password='admin',
                            host='127.0.0.1', port='5432', database='test_bd')

# https://www.psycopg.org/docs/usage.html - Psycopg 2.9.6 documentation
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s,%s,%s)'
            valores = ('Alex', 'Rojas', 'arojas@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Gonzalo', 'Sanchez', 'gsanchez@mail.com', 9)
            cursor.execute(sentencia, valores)
except Exception as e:
    # No necesita un rollback, lo hace automaticamente
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()
print('Termina la transaccion')
