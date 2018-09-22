from bs4 import BeautifulSoup
import requests
from django.utils.encoding import smart_str, smart_unicode
import re

source = requests.get('https://www.remitly.com/us/en/india/pricing').text

soup = BeautifulSoup(source, 'lxml')
rate = soup.find('div')
try:

    express = (soup.select("tbody.providerList_f1mjsvhw > tr:nth-of-type(1) td.f1cdddfp  div.feeValue_fcoij7e")[0].text)
    economy = (soup.select("tbody.providerList_f1mjsvhw > tr:nth-of-type(2) td.f1cdddfp  div.feeValue_fcoij7e")[0].text)   

    currentRateExpress = re.findall(r'\d{2}.\d{2}', smart_str(express))
    currentRateEconomy = re.findall(r'\d{2}.\d{2}', smart_str(economy))

    print("Current express rate: {}, economy rate: {}".format(currentRateExpress[0], currentRateEconomy[0])) 

except:
    print("Skipped, cannot find the requested rate on the website. Try again later.")
