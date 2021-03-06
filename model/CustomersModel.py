import mysql.connector

# Model is incharge of interacting to the database
class CustomersModel:

	def __init__(self):
		self.__localhost     = "localhost"
		self.__username      = "root"
		self.__password      = ""
		self.__database_name = "python_mvc" 
		self.__table_name 	 = "customers" 
		self.createConnection()

	def create(self, name, address):
		cursor = self.__db.cursor()

		val = (name, address)
		cursor.execute("INSERT INTO "+self.__table_name+" (name, address) VALUES (%s, %s)", val)

		self.__db.commit()

		return str(cursor.rowcount) + " record inserted."

	def read(self):
		cursor = self.__db.cursor()

		cursor.execute("SELECT * FROM "+self.__table_name+"")

		myresult = cursor.fetchall()

		return myresult

	def update(self, name, address, id):
		cursor = self.__db.cursor()

		cursor.execute ("UPDATE "+self.__table_name+" SET name=%s, address=%s WHERE id=%s ", (name, address, id))

		self.__db.commit()

		return str(cursor.rowcount) + " record update."

	def delete(self, id):
		cursor = self.__db.cursor()

		cursor.execute ("DELETE FROM "+self.__table_name+" WHERE id = %s", (id,))

		self.__db.commit()

		return str(cursor.rowcount) + " record deleted."

	def createConnection(self):
		db = mysql.connector.connect(
		  host     = self.__localhost,
		  user     = self.__username,
		  passwd   = self.__password,
		  database = self.__database_name
		)

		self.__db = db