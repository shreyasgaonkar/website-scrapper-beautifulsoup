import re
from bs4 import BeautifulSoup
import requests
from django.utils.encoding import smart_str, smart_unicode

source = requests.get('https://www.remitly.com/us/en/india/pricing').text

soup = BeautifulSoup(source, 'lxml')
rate = soup.find('div')

rate = rate.find('div', class_='f1a8qg93').td.text

string = (soup.select("tbody.providerList_f1mjsvhw  td.f1cdddfp  div.feeValue_fcoij7e")[0].text)
currentRate = re.findall(r'\d{2}.\d{2}', smart_str(string))

print (currentRate)
