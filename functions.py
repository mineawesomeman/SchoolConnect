import pymysql as mc
import sys
from datetime import datetime as dt

connection = None
cursor = None

##Set up all of the variables
def init():
	global connection
	global cursor
	connection = mc.connect (host = "localhost",user = "pytester",passwd = "monty",db = "SchoolConnect")
	cursor = connection.cursor()


##Class Information
def getClassIDs(ID):
	global connection
	global cursor
	cursor.execute("SELECT ClassID FROM StudentClass WHERE StudentID=" + str(ID) + ";")
	classIDs = []
	fetch = cursor.fetchall()
	for row in fetch:
		classIDs.append(row[0])
	return classIDs

def getClassInfo(classID):
	global connection
	global cursor
	cursor.execute("SELECT * FROM Classes WHERE ID=" + str(classID) + ";")
	return cursor.fetchall()[0]

#Announcement Functions
def getAnnouncements(classes, sdate='1970-01-01 00:00:00', edate='', count=50):
	if edate == '':	
		edate = dt.now().strftime("%Y-%m-%d %H:%M:%S")
	classString = "(Class IN (-1"
	for ID in classes:
		classString = classString + "," + str(ID)
	classString = classString + "))"
	cursor.execute("SELECT * FROM Announcements WHERE " + classString + " AND (Time BETWEEN \"" + sdate + "\" AND \"" + edate + "\") ORDER BY Time DESC LIMIT " + str(count) + ";")
	return cursor.fetchall()
	
def getUser(username, password):
	cursor.execute("SELECT * FROM Accounts WHERE Username=\"" + str(username) + "\" AND Password=\"" + str(password) + "\";")
	return cursor.fetchone()
