import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='testdb')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE idpersona=%s'
            #indicamos que hara la query para ejecutarla mas adelante (update, los valores a modificar y el id que se modificara)
            valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()