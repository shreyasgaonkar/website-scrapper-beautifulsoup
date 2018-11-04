from bs4 import BeautifulSoup
import requests
from django.utils.encoding import smart_str, smart_unicode
import re

source = requests.get('https://www.remitly.com/us/en/india/pricing').text

soup = BeautifulSoup(source, 'lxml')
rate = soup.find('div')
try:
    try:
        express = (soup.select("tbody.providerList_f1mjsvhw > tr:nth-of-type(2) > td:nth-of-type(1) > div.fnsgms5")[0].text)
        economy = (soup.select("tbody.providerList_f1mjsvhw > tr:nth-of-type(2) > td:nth-of-type(2) > div.fnsgms5")[0].text)
    except:
        print("Unable to parse website for current rate. Check CSS tag names from https://www.remitly.com/us/en/india/pricing")    

    currentRateExpress = re.findall(r'\d{2}.\d{2}', smart_str(express))
    currentRateEconomy = re.findall(r'\d{2}.\d{2}', smart_str(economy))

    print("Current express rate: {}, economy rate: {}".format(currentRateExpress[0], currentRateEconomy[0])) 

except:
    print("Skipped, cannot find the requested rate on the website. Try again later.")
