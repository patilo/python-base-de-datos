import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='testdb')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM personas WHERE idpersona IN %s'
            entrada = input('Proporciona los idpersona a eliminar (separados por coma): ')
            valores = (tuple(entrada.split(',')),)
            #volvemos a utilizar tupla y split para formas mas tuplas
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()