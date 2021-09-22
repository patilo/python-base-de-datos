import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='testdb')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)' #creamos la query inster
            valores = ('pepito', 'lopez', 'pepe@correo.com')#le damos los values
            cursor.execute(sentencia, valores)#ejecutamos la query con la sentencia y los valores
            registros_insertados = cursor.rowcount #pregunta los reg instertados (rowcownt)
            print(f'Registros Insertados: {registros_insertados}')#imprimimos la variable
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()