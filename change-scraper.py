# libs
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import requests
import sys

# if i encode as encode in all files then it doesn't seems to work, so i do it in sys :)
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
# tab with scraped urls (diffrent countries as endpoints)
url=["https://www.change.com/dk/storefinder","https://www.change.com/es/storefinder","https://www.change.com/no/storefinder","https://www.change.com/pl/storefinder","https://www.change.com/fi/storefinder","https://www.change.com/se/storefinder","https://www.change.com/at/storefinder","https://www.change.com/en-ca/storefinder"]

# scraping script
def scrap_elements(url):
    driver = webdriver.Chrome()
    driver.get(url)
    # driver.wait.until(EC.elementToBeClickable(By.CLASS_NAME,"css-1958t9v"))
    elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1958t9v")))
    elem=driver.find_elements(By.CLASS_NAME, "css-1958t9v")
    names=driver.find_elements(By.CLASS_NAME, "css-vd5crj")
    contact=driver.find_elements(By.CLASS_NAME, "css-3eg9kf")
    addres=driver.find_elements(By.CLASS_NAME, "css-wdqb8a")
    count = (driver.find_elements(By.XPATH,"(//*[contains(@class, 'student-name')])"))

    return names,contact,addres

# converting returned data to arrays, also checking if the scraped data is correct (is the number div realy number etc..)
def convert_to_array(names,contact,address):
    array_data = []
    array_object=[]
    contact_valid=[]
    tel=[]
    email=[]
    name=[]
    adressses=[]
    for div in range(len(contact)):
        if (div%2==0) and (contact[div].text.isnumeric()==False) and (contact[div].text.find('+')==(-1) and contact[div].text.find('-')==(-1)):
            contact_valid.append("no number")
        contact_valid.append(contact[div].text)
    for div in range(0,len(contact_valid)-1,2):
        tel.append(contact_valid[div])
        email.append(contact_valid[div+1])
    for div in (names):
        name.append(div.text)
    for div in (address):
        adressses.append(div.text)
    return tel,email,name,adressses
# just HWDP thing
# h=[]
# w=[]
# d=[]
# p=[]
# # for x in url:

# converting to arrays
name,contact,addres=scrap_elements("https://www.change.com/no/storefinder")
phone_array,email_array,name_array,address_array=convert_to_array(name,contact,addres)
h.extend(name_array)
w.extend(address_array)
d.extend(phone_array)
p.extend(email_array)


# creating pandas dataframe
columns=['NAME','Address','Phone','e-mail']
df = pd.DataFrame(list(zip(h,w,d,p)),columns=columns)
print(df)

# output to excel
df.to_excel("output.xlsx",sheet_name='BaoBab')  



# still learning, meaby i will need this later :))

# data=scrap_elements(url)
# data_array=convert_to_array(data)
# # print(data_array)
# r1 = [subarray[0] for subarray in data_array]
# name = [''.join(sublist) for sublist in r1]


# r2 = [subarray[1] for subarray in data_array]
# street = [''.join(sublist) for sublist in r2]

# r3=[subarray[2] for subarray in data_array]
# zipcity = [''.join(sublist) for sublist in r3]

# r4=[subarray[3] for subarray in data_array]
# phone = [''.join(sublist) for sublist in r4]

# r5=[subarray[4] for subarray in data_array]
# email = [''.join(sublist) for sublist in r5]


# columns=['NAME','Address','Phone','e-mail']

# df = pd.DataFrame(list(zip(name,street,zipcity,phone,email)), columns=columns)
# print(df)
