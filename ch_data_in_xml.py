import requests
import zeep
import dump
import xmlbuilder
from xml.etree.ElementTree import (Element, SubElement, Comment, tostring,)

from datetime import date
import cba_api
import xml.etree.ElementTree as ET

today = date.today()
#print("Today's date:", today)
url = "http://api.cba.am/exchangerates.asmx?op=ExchangeRatesByDate"
headers = {'content-type': 'text/xml', 'charset': 'utf-8'}
main = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xmlns:xsd="http://www.w3.org/2001/XMLSchema"
		xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <ExchangeRatesByDate
				xmlns="http://www.cba.am/">
			<date>%(date)s</date>
		</ExchangeRatesByDate>   
     </soap:Body>
</soap:Envelope>"""
#
data = {'date':today}
#print (main%data)
#myfile = open("body.xml", "w")
#myfile.write(main%data)

#d = open("body.xml", 'rb')
#print(d.read())

data1 = {'date':today}
#zz = (main%data1, 'rb')
#print(zz)

response = requests.post(url, data=main%data, headers=headers)
pastebin_url = response.text
#print(pastebin_url)
##with open("curr.xml", "w") as file:
##    file.write(str(response.text))
##
###
##f = open("curr.xml", "rb")
root = ET.fromstring(pastebin_url)

#root = ET.fromstring(cba_api.response.text)
# printing attributes of the root tags 'neighbor'.
sid1 = root.findall(".//{http://www.cba.am/}Rate")
sid2 = root.findall(".//{http://www.cba.am/}ISO")
sid3 = root.findall(".//{http://www.cba.am/}Difference")
xml_date = root.findall(".//{http://www.cba.am/}CurrentDate")


date_of_rate = ("Current rates date is: " + xml_date[0].text)
#print(date_of_rate)
difference = sid3
USD =("Current Rates of"+ ' '   +sid2[0].text  +' is:' +" "+ sid1[0].text + ' '+'Diff:'+ difference[0].text)
#print (USD)
GBP = ("Current Rates of"+ ' ' + sid2[1].text  +' is:' +" "+ sid1[1].text + ' '+'Diff:'+ difference[1].text)
#print(GBP)
EUR = ("Current Rates of"+ ' ' + sid2[3].text  +' is:' +" "+ sid1[3].text + ' '+'Diff:'+ difference[3].text)
#print(EUR)
RUB = ("Current Rates of"+ ' ' + sid2[20].text  +' is:' +" "+ sid1[20].text + ' '+'Diff:'+ difference[20].text)
#print(RUB)

#rate = root.findall(".//{http://www.cba.am/}Rate")


