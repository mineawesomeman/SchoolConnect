#!/usr/bin/python3
import cgi
import xml.etree.ElementTree as ET
import functions as fun
import datetime

ID = 20207065
User = 'xxxx'
Pass = 'some pass'

fun.init()
classList = fun.getClassIDs(ID)
rawAnnounce = fun.getAnnouncements(classList)

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

print ("Content-type:text/xml\r\n\r\n")
test = ET.tostring(root)
print(str(test)[2:-1])


