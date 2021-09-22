import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='testdb')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (
                ('pepito', 'filomeno', 'pepito@mail.com'),
                ('jose', 'perez', 'jperez@mail.com'),
                ('ana', 'guaska', 'anag@mail.com')
                )  #como son tuplas debemos ingresarlos asi ((),(),())
            cursor.executemany(sentencia, valores) #utilizamos executemany como son varios archivos
            registros_insertados = cursor.rowcount #almacenamos la cantidad insertada correctamente
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()