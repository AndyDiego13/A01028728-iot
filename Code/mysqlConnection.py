import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='samudeluque', host='127.0.0.1', database='iot')
    cursor = cnx.cursor()

    #query_data = (3,) #tuple cuartos menores a 3 en este caso, más parametro y cuidar el orden
    #query = (f"SELECT * FROM cuartos ;") #consulta %s en una consulta es un comodin
    query = (f"SELECT id_light FROM lights;")
    cursor.execute(query)

    #query = f"INSERT INTO rooms(id_room, name) values(8, 'Study Hall');"

    #for id_light in range(8,19):
      #query_data = (id_light, False, 0)
      #query = f"INSERT INTO lights(id_light, turn_on, intensity) values(%s, %s, %s);"
    
      #cursor.execute(query)#,query_data
      #cursor.execute(query,query_data)
    
    #update lights
    

    #List comprehesion
    last_id = [result[0] for result in cursor[-1]]
    ids = [result[0]for result in cursor]

    for result in cursor:
      ids.append(result[0])
    #cnx.commit()#insert,update,delete manda un commit 

except mysql.connector.Error as err:

  if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
    
finally:
  if 'cnx' in locals() or 'cnx' in globals():
    print("Something is wrong with your name or password")
    cnx.close()
