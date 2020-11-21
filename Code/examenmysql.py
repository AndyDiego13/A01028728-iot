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

    nombre = ["Howard Phillips", "Stephen", "Dean", "Junji", "Pedro Antonio", "Clive", "Edgar", "Jojo", "Cassandra", "J.K."]
    apellido = ["Lovecraft", "King", "Koontz", "Ito", "De Alarcón","Barker", "Allan Poe","Moyes", "Clare", "Rowling"]

    for u in range(10):
      insertarAutores(u+1, nombre[u], apellido[u])
    
    titulo = ["The Little Glass Bottle", "The Secret Cave", "The Mystery of the Grave-Yard", "The Dream-Quest of Unknown Kadath", "The Case of Charles Dexter Ward", "The Whisperer in Darkness", "At the Mountains of Madness", "The Shadow over Innsmouth", "The Shadow Out of Time", "The Silver Key",
    "Carrie", "The Shining", "The Dead Zone", "Pet Sematary", "It", "Gerald's Game", "Insomnia", "Dreamcatcher", "The Mist", "Under the Dome",
    "Blood Risk", "Fear Nothing", "Odd Thomas", "Final Hour", "The Silent Corner", "Fear That Man", "The Fall of the Dream Machine", "The Dark Symphony", "Hell's Gate", "Soft Come the Dragons",
    "Tomie", "Flesh-Colored Horror", "The Face Burglar", "Souichi's Diary of Delights", "Souichi's Diary of Curses","Slug Girl", "Blood-bubble Bushes", "Hallucinations", "House of the Marionettes", "The Town Without Streets",
    "El final de Norma", "El sombrero de tres picos", "El escándalo", "El niño de la bola", "El capitán Veneno", "La pródiga","La Buenaventura", "Cuentos amatorios", "Historietas nacionales", "Narraciones inverosímiles",
    "The Damnation Game", "Weaveworld", "Cabal", "Imajica", "The Thief of Always", "Sacrament", "Galilee", "Coldheart Canyon", "Tortured Souls", "Mister B. Gone",
    "MS. Found in a Bottle", "King Pest", "The Fall of the House of Ushe", "The Man of the Crowd", "A Descent into the Maelström", "The Murders in the Rue Morgue", "The Masque of the Red Death", "The Pit and the Pendulum", "The Oval Portrait", "The Gold Bug",
    "The Peacock Emporium", "The Ship of Brides","Silver Bay", "Night Music", "The Last Letter from Your Lover", "The Horse Dancer", "Me Before You", "After You", "Still Me","Honeymoon in Paris",
    "Clockwork Angel", "Clockwork Prince", "Clockwork Princess", "City of Bones", "City of Ashes", "City of Glass", "ity of Fallen Angels", "City of Lost Souls", "City of Heavenly Fire", "Lady Midnight",
    "Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban","Harry Potter and the Goblet of Fire","Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince","Harry Potter and the Deathly Hallows","Fantastic Beasts and Where to Find Them", "Quidditch Through the Ages","The Tales of Beedle the Bard"]

    for x in range(100):
      precio=np.random.randint(200, 300)
      fecha = datetime.datetime(2020,11,11) + datetime.timedelta(days = random.randint(1,30))
      insertarLibros(x+1,titulo[x],fecha,precio)
    
    tag=["Horror","Science Fiction","Fantasy","Suspense","Crime","Manga","Prosa","Novels","Gótica","Bibliografico"]
    for n in range(10):
      insertarTags(n+1,tag[n])
    
    #tablas de relación

    #libros
    queryidlibros = (f"SELECT id_libros FROM libros;")
    cursor.execute(queryidlibros)
    id_libros = [result[0] for result in cursor]

    #autores
    queryidautor = (f"SELECT id_autor FROM autores;")
    cursor.execute(queryidautor)
    id_autor = [result[0] for result in cursor]

    #tags
    queryidtag = (f"SELECT id_tag FROM tags;")
    cursor.execute(queryidtag)
    id_tag = [result[0] for result in cursor]

    for j in range(0,10):
      for i in range(0,100,10):

        #agregar a libros_tags
        queryLibrosTags = (id_libros[i],id_tag[j])
        querylibros_tags =  (f"INSERT INTO libros_tags  VALUES(%s, %s);")
        cursor.execute(querylibros_tags,queryLibrosTags)
        cnx.commit()

        #agregar a ibros_autores
        queryLibrosAutores = (id_libros[i],id_autor[j])
        querylibros_autores =  (f"INSERT INTO libros_autores  VALUES(%s, %s);")
        cursor.execute(querylibros_autores, queryLibrosAutores)
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

