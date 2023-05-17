import psycopg2
# Creamos el objeto de tipo conexion para conectarnos a postgresql
conexion = psycopg2.connect(user='postgres', password='admin',
                            host='127.0.0.1', port='5432', database='test_bd')

# https://www.psycopg.org/docs/usage.html - Psycopg 2.9.6 documentation
try:
    with conexion:
        with conexion.cursor() as cursor:
            # Placeholder
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            entrada = input(
                'Digite los id persona a buscar (separados por coma): ')
            llaves_primarias = (tuple(entrada.split(', ')),)
            # De esta manera ejecutamos la sentencia
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            # Este metodo permite recuperar un todos los registros
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close()
