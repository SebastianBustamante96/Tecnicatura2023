import psycopg2
# Creamos el objeto de tipo conexion para conectarnos a postgresql
conexion = psycopg2.connect(user='postgres', password='admin',
                            host='127.0.0.1', port='5432', database='test_bd')

# https://www.psycopg.org/docs/usage.html - Psycopg 2.9.6 documentation
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'  # Placeholder
            id_persona = input('Digite un numero para el id persona: ')
            # De esta manera ejecutamos la sentencia
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchone()
            # Este metodo permite recuperar un registro que sera una tupla
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close()
