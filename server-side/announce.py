#!/usr/bin/python3
import cgi, cgitb
import xml.etree.ElementTree as ET
import functions as fun
from datetime import datetime
import os, sys

fun.init()
print ("Content-type:text/xml\r\n\r\n")

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')


user = fun.getUser(username,password)

if user == None:
	print ("<error>Username and Password do not match up</error>")
	sys.exit()

if user[3] == 1:
	ID = user[4]
elif user[3] == 2:
	ID = form.getvalue('ID')
	if ID == None:
		print('<error>No Student ID Given On Teacher Account</error>')
		sys.exit()

sdate = form.getvalue("sdate")
edate = form.getvalue("edate")
count = form.getvalue("count")

if sdate == None or edate == 'None':
	sdate = '1970-01-01 00:00:00'

if edate == None or edate == 'None':
	edate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if count == None or count == 'None':
	count = 50

classList = fun.getClassIDs(ID)
rawAnnounce = fun.getAnnouncements(classList, sdate, edate, count)

root = ET.Element('Announcements')
root.set('count',str(len(rawAnnounce)))
for raw in rawAnnounce:
	announce = ET.SubElement(root, 'announcement')
	announce.set('notify', str(raw[4]))
	announce.set('id', str(raw[0]))
	title = ET.SubElement(announce, 'title')
	title.text = str(raw[1])
	stClass = ET.SubElement(announce, 'class')
	stClass.text = str(fun.getClassInfo(raw[3])[1])
	stClass.set('classID', str(raw[3]))
	date = ET.SubElement(announce, 'date')
	date.text = str(raw[5].date())
	time = ET.SubElement(announce,'time')
	time.text = str(raw[5].time())
	text = ET.SubElement(announce, 'text')
	text.text = str(raw[2])
	
tree = ET.ElementTree(root)


test = ET.tostring(root)
print(str(test)[2:-1])


