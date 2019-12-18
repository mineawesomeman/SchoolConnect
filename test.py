import pymysql as mc
import sys

num1 = 37
num2 = 17
str1 = 'Hello Mr. C!'

connection = mc.connect (host = "localhost",
                         user = "pytester",
                         passwd = "monty",
                         db = "SchoolConnect")
cursor = connection.cursor()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone()
print("server version:", row[0])
#cursor.execute("""INSERT INTO testTB VALUES (""" + str(num1) + """,""" + str(num2) + """, '""" + str1 + """');""")
#connection.commit()
cursor.execute("""SELECT ID FROM Students WHERE YearOfGraduation=2020;""")
bleh = cursor.fetchall()
for thing in bleh:
	for thingie in thing:
		try:
			print (thing[0])
			cursor.execute("""INSERT INTO StudentClass values (""" + str(thing[0]) + """, 4);""")
		except mc.err.IntegrityError:
			print ("already exists")
connection.commit()
cursor.close()
connection.close()
