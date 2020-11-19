'''
Andrea Serrano Diego
- A01028728 -
19/Nov/2020

Examen Modulo 2 Base de datos 
Profesor: Octavio Navarro Hinojosa

'''

import mysql.connector
import numpy as np
import random
import datetime
import itertools

def insertarAutores(id_autor, nombre, apellido):
   queryAutores = (f"INSERT INTO autores values(%s,%s,%s);")
   guardar_queryAutores = (id_autor,nombre,apellido)
   cursor.execute(queryAutores, guardar_queryAutores)
   cnx.commit()

#------------------------------------

def insertarLibros(id_libro, titulo, fecha_publicacion, precio):
    queryLibros = (f"INSERT INTO libros values(%s,%s,%s,%s);")
    guardar_queryLibros = (id_libro, titulo, fecha_publicacion, precio)
    cursor.execute(queryLibros, guardar_queryLibros)
    cnx.commit()

#-------------------------------------

def insertarTags(id_tag, tag):
    queryTags = (f"INSERT INTO tags values(%s,%s);")
    guardar_queryTags = (id_tag, tag)
    cursor.execute(queryTags, guardar_queryTags)
    cnx.commit()

#-------------------------------------

try:
    cnx = mysql.connector.connect(user='root', password='samudeluque', host='127.0.0.1', database='biblioteca')
    cursor = cnx.cursor()

    idAutores = [result[0] for result in cursor]
    cantidadAutores = len(idAutores)+1

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

