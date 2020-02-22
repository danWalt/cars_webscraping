import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from bs4 import BeautifulSoup
import openpyxl
import pprint

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

URL = 'http://pricelist.yad2.co.il/'

# Load yad2 cars prices page
page = requests.get(URL, headers=headers)
page.raise_for_status()  # make sure page loaded without problems

# load page content with BS
soup = BeautifulSoup(page.content, 'html.parser')

car_types = soup.select('select[name=CarType] > option')
car_dic = {}
for i in car_types:
    car_dic[i.text] = i['value']

manufacturer = soup.select('select[name=Manufactur] > option')
manufacturer_dic = {}
for i in manufacturer:
    manufacturer_dic[i.text] = i['value']

model = soup.select('select[name=CarModel] > option')
mod_dic = {}
for i in model:
    mod_dic[i.text] = i['value']

year = soup.select('select[name=Year] > option')
year_dic = {}
for i in year:
    year_dic[i.text] = i['value']

    