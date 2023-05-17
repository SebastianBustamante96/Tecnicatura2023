import psycopg2
# Creamos el objeto de tipo conexion para conectarnos a postgresql
conexion = psycopg2.connect(user='postgres', password='admin',
                            host='127.0.0.1', port='5432', database='test_bd')

# https://www.psycopg.org/docs/usage.html - Psycopg 2.9.6 documentation
try:
    with conexion:
        with conexion.cursor() as cursor:
            # Placeholder
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Digite el id a eliminar: ')
            valores = (entrada,)  # Es una tupla de valores
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Los registros eliminados son: {registros_eliminados}')


except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close()
