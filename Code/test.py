import mysql.connector
from mysql.connector import Error
import numpy as np
import random
import datetime
'''
def insertarvariablesautores(id_autor, nombre, apellido):
        mySql_query = """ INSERT INTO autores (id_autor, nombre, apellido)
                            VALUES
                            (%s, %s, %s) """

        record = (id_autor, nombre, apellido)
        cursor.execute(mySql_query, record)
        connection.commit()

def insertarvariableslibros(id_libro, titulo, fecha_publicacion, precio):

        mySql_insert_query = """INSERT INTO libros (id_libro, titulo, fecha_publicacion, precio) 
                                   VALUES 
                                   (%s, %s, %s, %s) """
        record = (id_libro, titulo, fecha_publicacion, precio)
        cursor.execute(mySql_insert_query, record)
        connection.commit()

def insertarvariablestags(id_tag,tag):
    
        mySql_insert_query = """INSERT INTO tags (id_tag,tag) 
                                   VALUES 
                                   (%s, %s) """
        record = (id_tag,tag)
        cursor.execute(mySql_insert_query, record)
        connection.commit()

''' 
'''
try:
        connection = mysql.connector.connect(host='localhost',
                                             database='examen',
                                             user='root',
                                             password='alina2013')

        cursor = connection.cursor()
        nombres = ["Ivan", "Sofia", "Lia", "Juan", "Jose","Andrea","Antonio","Felipe","Louissa","William"]
        apellidos = ["Manzano", "Rojas", "Nuñez", "Hormaza", "Carranza","Serrano","Cordoba","May","Gonzalo","Shakespeare"]
        for i in range (10):
            insertarvariablesautores(i+1,nombres[i],apellidos[i])

        titulos=["Poema de Gilgamesh","Libro de Job (de la Biblia)","Las mil y una noches","Saga de Njál","Todo se desmorona","Cuentos infantiles ","Divina Comedia","Orgullo y prejuicio",
        "Papá Goriot Molloy","Malone muere","Decamerón ","Ficciones","Cumbres","Borrascosas","El extranjero","Poemas","Viaje al fin de la noche","Don Quijote de la Mancha",
        "Los cuentos de Canterbury","Relatos cortos","Nostromo","Grandes Esperanzas","Jacques el fatalista","Berlin","Alexanderplatz","Crimen y castigo","El idiota","Los endemoniados",
        "Los hermanos Karamazov","Middlemarch","El hombre invisible","Medea","¡Absalom, Absalom!","El ruido y la furia","Madame Bovary ","La educación sentimental ","Romancero gitano",
        "Cien años de soledad","El amor en los tiempos del cólera ","Fausto Almas muertas","El tambor de hojalata","Gran Sertón: Veredas","Hambre",
        "El viejo y el mar ","Ilíada","Odisea","Casa de muñecas",
        "Ulises","Relatos cortos","El proceso","El castillo","Shakuntala","El sonido de la montaña","Zorba, el griego",
        "Hijos y amantes","Gente independiente ","Poemas","El cuaderno dorado","Pippi Calzaslargas","Diario de un loco","Hijos de nuestro barrio",
        " Los Buddenbrook ","La montaña mágica","Ensayos","Moby-Dick","La historia","Beloved","Genji Monogatari","El hombre sin atributos","Lolita",
        "1984","Las metamorfosis","Libro del desasosiego","Cuentos","En busca del tiempo perdido","Gargantúa y Pantagruel",
        "Pedro Páramo","Hijos de la medianoche ","Masnavi","Bostan","Tiempo de migrar al norte","Ensayo sobre la ceguera","Hamlet","El rey Lear","Otelo","Edipo rey",
        "Rojo y negro","Vida y opiniones del caballero Tristram Shandy","La conciencia de Zeno","Los viajes de Gulliver","Guerra y paz ","Ana Karenina","La muerte de Iván Ilich",
        "Las aventuras de Huckleberry","Finn Ramayana","Eneida","Mahabhárata","Hojas de hierba",
        "La señora Dalloway","Quik Potosky","Memorias de Adriano"]

  

        for j in range(100):
            precio=np.random.randint(200, 300)
            fecha = datetime.datetime(2020,11,11) + datetime.timedelta(days = random.randint(1,30))
            insertarvariableslibros(j+1,titulos[j],fecha,precio)


        tags=["Horror","Romance","Comedia","Ciencia Ficcion","Aventura","Suspenso","Policiacas","Fantasia","Gótica","Bibliografico"]      
        for n in range(10):
            insertarvariablestags(n+1,tags[n])
        #id de libros
        query_id_libros = ("select id_libro from libros;")
        cursor.execute(query_id_libros)
        id_libros = [result[0] for result in cursor]

        # id de autores 
        query_id_autor = ("select id_autor from autores;")
        cursor.execute(query_id_autor)
        id_autor = [result[0] for result in cursor]

        #id de tags
        query_id_tag = ("select id_tag from tags;")
        cursor.execute(query_id_tag)
        id_tag = [result[0] for result in cursor]

        for i in range(10):
            for j in range(10):
                query_libros_tag = (id_libros[j],id_tag[i])
                query_T =  ("INSERT INTO  libros_tags  VALUES( %s, %s) ;")
                cursor.execute(query_T,query_libros_tag)
        for i in range(10):
            for j in range(10):
                query_libros_autores = (id_libros[j],id_autor[i])
                query_a =  ("INSERT INTO  libros_autores  VALUES( %s, %s) ;")
                cursor.execute(query_a, query_libros_autores)
     
        connection.commit()
        cursor.close()
        connection.close()
        print("Record inserted successfully into tables")
    

    except mysql.connector.Error as error:

        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
'''