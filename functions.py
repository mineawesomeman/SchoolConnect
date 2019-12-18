import pymysql as mc
import sys

connection = None
cursor = None

def init():
	global connection
	global cursor
	connection = mc.connect (host = "localhost",user = "pytester",passwd = "monty",db = "SchoolConnect")
	cursor = connection.cursor()

def getClasses(ID):
	global connection
	global cursor
	cursor.execute("SELECT * FROM StudentClass WHERE ID=" + str(ID) + ";")
	cursor.fetchall()
