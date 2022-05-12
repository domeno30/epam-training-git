import requests
import zeep
import dump
from datetime import date
today = date.today()
#print("Today's date:", today)
url = "http://api.cba.am/exchangerates.asmx?op=ExchangeRatesByDate"
headers = {'content-type': 'text/xml', 'charset': 'utf-8'}
#set in body ExnchangeRateByDate
body = """<?xml version="1.0" encoding="utf-8"?>
  <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ExchangeRatesByDate xmlns="http://www.cba.am/">
      <date>2021-10-09</date>
    </ExchangeRatesByDate>
  </soap:Body>
</soap:Envelope>"""
#import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ET
root = ET.fromstring(body)
for body in root.findall('date'):
    new_date = int(date.text) + 1
    date.text = str(new_date)
    date.set(today)

response = requests.post(url, data=body, headers=headers)

#print(response.text)
#tree = ET.parse('body')
#root = tree.getroot()
#print byte start
#print(response.content)

#tree.write('output.xml')
