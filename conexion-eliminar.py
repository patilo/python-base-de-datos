import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='testdb')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM personas WHERE idpersona=%s'
            entrada = input('Proporciona el id_persona a eliminar: ')
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()