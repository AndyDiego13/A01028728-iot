import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='samudeluque', host='127.0.0.1', database='iot')
    cursor = cnx.cursor()

    query_data = (3,) #tuple
    query = (f"SELECT * FROM cuartos ;") #consulta
    
    cursor.execute(query)

    for result in cursor:
        print(result)

except mysql.connector.Error as err:

  if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
    
finally:
  cnx.close()
