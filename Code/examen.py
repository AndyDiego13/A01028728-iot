import mysql.connector
import random
import numpy as np
import datetime
import string

def random_char(y):
  return ''.join(random.choice(string.ascii_letters) for x in range(y))

try:
  #tengo que poner mi contraseña y host es la noexion de nuestr compu
  #aqui se guarda la conexion con tu base de datos de sql
    cnx = mysql.connector.connect(user='root', password='Iyzkw3927', host='127.0.0.1', database='librosData', auth_plugin='mysql_native_password')
    cursor = cnx.cursor()

    #PRIMERO INSERTARE EN LIBROS

    
    for j in range(0,100):

      titulo = random_char(5)
      fecha = datetime.datetime(2020,11,11) + datetime.timedelta(days = random.randint(1,30)) 
      
      precio = random.randint(60,100)

      
      query_libro= ( titulo, fecha, precio)
      query = (f"insert into libros (titulo,fecha,precio)  values( %s, %s, %s) ;")
        
      cursor.execute(query,query_libro)

      #para hacer cambios en database 
      cnx.commit()
    
    #ahora insertare en autores
    for a in range(0,10):

      nombre = random_char(7)
      apellido = random_char(8)

      query_autor= ( nombre, apellido)
      query2 = (f"insert into autores (nombre, apellido) values( %s, %s) ;")
        
      cursor.execute(query2,query_autor)

      #para hacer cambios en database 
      cnx.commit()
    
    for t in range(0,10):

      tag = random_char(7)

      query_tag = (tag,)
      query3 = (f"insert into tags (tag) values( %s) ;")
        
      cursor.execute(query3,query_tag)

      #para hacer cambios en database 
      cnx.commit()

    #---------------llenar tablas de relación--------

    #guardar ids de libros en una lista
    queryID_libros = (f"select id_libro from libros;")
    cursor.execute(queryID_libros)
    idsLibros =  [result[0] for result in cursor]

    #guardar ids de autores en una lista
    queryID_autor = (f"select idAutor from autores;")
    cursor.execute(queryID_autor)
    idsAutor =  [result[0] for result in cursor]

    #guardar ids de tags en una lista
    queryID_tag = (f"select idTag from tags;")
    cursor.execute(queryID_tag)
    idsTag =  [result[0] for result in cursor]

    #para cada 
    for j in range(0,10):
      for i in range(0,100,10):

        #agregar a Libros_tags
        queryLibrosTag = (idsLibros[i],idsTag[j])
        query4T =  (f"insert into libros_tags  values( %s, %s) ;")
        cursor.execute(query4T,queryLibrosTag)
        cnx.commit()

        #agregar a Libros_autor
        queryLibrosAutores = (idsLibros[i],idsAutor[j])
        query5a =  (f"insert into libros_Autores  values( %s, %s) ;")
        cursor.execute(query5a, queryLibrosAutores)
        cnx.commit()



  




except mysql.connector.Error as err:
#si hay un error ocurrira esto
#en caso de que se niegue el acceso a la base de datos
  if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
    #si no existe la base de datos
  elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
    
finally:
  #esto se hará si o sí 
  if 'cnx' in locals() or 'cnx' in globals():
    cnx.close()