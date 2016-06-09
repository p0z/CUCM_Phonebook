#!/usr/bin/env python
import requests
import argparse
import xml.etree.ElementTree as ET
import os
os.system('clear')
parser = argparse.ArgumentParser(description='Example: %(prog)s -t https://cucmserver:8443/', usage='%(prog)s -t https://cucmserver:8443/')
parser.add_argument("-t", "--target", help='URL host (ex: https://target:8443/)')
parser.add_argument("-l", "--lastname", help='Lastname search, default: none', default='',type=str)
parser.add_argument("-f", "--firstname", help='Firstname search, default: none', default='',type=str)
parser.add_argument("-n", "--number", help='Number, default: none', default='',type=str)
parser.add_argument("-s", "--start", help='Start records, default: 0', default='0',type=str)
parser.add_argument("-e", "--end", help='End records, default: 30', default='30',type=int)
args = parser.parse_args()

lName='&l='+args.lastname
fName='&f='+args.firstname
tNumber='&n='+args.number
start='&start='+args.start
end = args.end

count = 0
while count < end:
	start = '&start='+str(count)
	find_url='/ccmcip/xmldirectorylist.jsp?'+lName+fName+tNumber+start
	url=args.target+find_url
	req = requests.get(url, timeout = 3, stream = False, verify = False)
	xml = req.content
	try:
		tree = ET.fromstring(xml)
		DirEntr = tree.findall(".//DirectoryEntry")
		Prompt = tree.find(".//Prompt")
		print ' --> ' + Prompt.text + ' <-- '
		print '--------|---------------------'
		print ' Number | Lastname / Firstname'
		print '--------|---------------------'
		for tmp in DirEntr:
			UserName = tmp.find(".//Name")
			Telephone = tmp.find(".//Telephone")
			print u'{0:1}{1:6} | {2:50}'.format(' ', Telephone.text, UserName.text)
		count = count+30
	except IOError as e:
		print 'Error'
