import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='testdb')
#aqui creamos la conexion y la consulta a la bd (intenta conectar)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM personas WHERE idpersona IN %s' #creamos la variable que ejecuta la query
            # llaves_primarias = ((1,2,3),)
            entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            #creamos tuplas con la funcion split para consultar los que consulte el usuario
            cursor.execute(sentencia, llaves_primarias)#el objeto cursor ejecuta la query pasando los datos del usuario
            registros = cursor.fetchall() #guardamos los resultados de la consulta y usamos fetchall para llamar a todos
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()