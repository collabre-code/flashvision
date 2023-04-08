# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:46:40 2023

@author: TherinYoung
"""




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#import pandas as pd
import os
import time

#set up beautiful soup
from bs4 import BeautifulSoup

import itertools

import pyodbc
print(pyodbc.drivers())

import pandas as pd


#########################################################################################################################
#                    Use Selenium and Python to download camera data from vision.flashparking                           #
#########################################################################################################################


url = 'https://vision.flashparking.com/'
userName = "collaborative-real-estate@flashparking.com"
passWord = "eTC2:vrL,U"
loginbutton_class = "MuiButton-label"
reportstab_xpath = "/html/body/div/div/div[1]/header/div/div[2]/div/a[3]/p"
eventsfield_class = "_t4n3lg"
camname_xpath = "//li[@data-value='cam_name']"
eventtime_xpath = "//li[@data-value='event_time']"
location_class = "_t4n3lg"





print('creating chrome driver')
#create driver
chrome_options = Options()
#chrome_options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
#chrome_options.binary_location = '\Google\\Chrome\\Application\\chrome.exe'
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_driver_binary = "chromedriver.exe"


driver = webdriver.Chrome(chrome_options = chrome_options)
#driver = webdriver.Chrome(executable_path = 'chromedriver.exe',options = chrome_options)

print("created chrome driver")
driver.get(url)
#assert 'Chrome' in browser.title

driver.implicitly_wait(5)


print('Entering Flash Vision Credentials')
# find and enter username
username = driver.find_element(By.ID, "userName")
username.send_keys(userName)

# find and enter password
password = driver.find_element(By.ID,"pword")
password.send_keys(passWord)


print ('Logging in............')
#login
driver.find_element(By.CLASS_NAME, loginbutton_class).click()


print('Accessing Flash Vision Reports..........')
#select reports tab
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, reportstab_xpath))).click()

#select event fields dropdown
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, eventsfield_class))).click()


#check boxes to include in report
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, camname_xpath))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, eventtime_xpath))).click()

#click arbitray location to hide drop down list
homeLink = driver.find_element(By.CLASS_NAME, location_class)
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(homeLink, 500, 0) #move 150 pixels to the right to access Help link
action.double_click()
action.perform()


#save camera locations to list

location_lst = ['1637612666670','1637612685464','1637612702872','1637612717708','1637612734268','1637612800645',
               '1637612861370','1637612879883','1637612893502','1637612911992']






#create beautiful soup driver
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
print("created beautiful soup driver")


location = []
locationtime = []
timeofday = []
month = []
day = []
year = []


print("Data scraping started.......")
for cam_location in location_lst:
    print("Scraping Cam#" + " " + "%s" % (cam_location))
    if cam_location == location_lst[0]:
        wait = WebDriverWait(driver,10)
        rows = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#ifmcontentstoprint > div._1h9d79c > div > div._22eazw > table > tbody'))).text.split()


        #append location and time to lists
        for element in rows:
            if ('Aber' in element) or ('Will' in element) or ('Ingress' in element) or ('Egress' in element):
                location.append(element)
            elif (':' in element):
                locationtime.append(element)
            elif ('AM' in element) or ('PM' in element):
                timeofday.append(element)


        #append date to lists


        month.append(rows[2::7])
        day.append(rows[3::7])
        year.append(rows[4::7])



        #click camera location dropdown
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div._m4b91i"))).click()

        time.sleep(5)

        #click location
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value= %s]" % (cam_location)))).click()

        time.sleep(5)



        action.double_click()
        action.perform()

    else:

        time.sleep(2)

        #click camera location dropdown
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div._m4b91i"))).click()

        time.sleep(1)

        #click location
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value= %s]" % (cam_location)))).click()

        time.sleep(5)

        action.double_click()
        action.perform()


        wait = WebDriverWait(driver,10)

        rows = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#ifmcontentstoprint > div._1h9d79c > div > div._22eazw > table > tbody'))).text.split()

        for element in rows:
            if ('Aber' in element) or ('Will' in element) or ('Ingress' in element) or ('Egress' in element):
                location.append(element)
            elif (':' in element):
                locationtime.append(element)
            elif ('AM' in element) or ('PM' in element):
                timeofday.append(element)


        #append date for each camera to a list (the list, month, will include 10 lists (1 list for each camera))
        month.append(rows[2::7])
        day.append(rows[3::7])
        year.append(rows[4::7])

        #click camera location dropdown
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div._m4b91i"))).click()

        time.sleep(1)

        #click location
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value= %s]" % (cam_location)))).click()


        time.sleep(3)

        action.double_click()
        action.perform()

        time.sleep(1)


driver.close()


#create empty dataframe
result = pd.DataFrame()

#join lists into a single list
month = list(itertools.chain.from_iterable(month))
day = list(itertools.chain.from_iterable(day))
year = list(itertools.chain.from_iterable(year))

#add columns to empty dataframe
result['Cam_ID'] = location
result['Time'] = locationtime
result['Timeofday'] = timeofday
result['Month'] = month
result['Day'] = day
result['Year'] = year

datetime = []
for i in range(0,result.shape[0]):
    datetime.append(result['Month'][i]+'-'+result['Day'][i]+'-'+
                   result['Year'][i] + ' '+ result['Time'][i] + ' ' + result['Timeofday'][i])

result['camTime'] = datetime

#convert field to datetime format
result['camTime'] = pd.to_datetime(result['camTime'])

#add currrent days timestamp as a field
result['currentTime'] = pd.Timestamp.today()

#get only columns needed for results
result = result[['Cam_ID','camTime','currentTime']].reset_index(drop=True)

#filter for the most recent camera ID
result_cleaned = result.groupby(by=['Cam_ID','currentTime'])['camTime'].max().reset_index()

#calculate time delta
result_cleaned['timeDelta'] = result_cleaned['currentTime'] - result_cleaned['camTime']

#convert time delta to minutes
minutes = []
for i in range(0,result_cleaned.shape[0]):
    minutes.append(result_cleaned['timeDelta'][i].seconds/60.0)

result_cleaned['timeDelta'] = minutes

#send email alert if camera down for more than 120 minutes



#convert UTC docker time to local time
result_cleaned['currentTime'] = result_cleaned['currentTime'].dt.tz_localize('utc').dt.tz_convert('US/Eastern')
result_cleaned['camTime'] = result_cleaned['camTime'].dt.tz_localize('utc').dt.tz_convert('US/Eastern')




#push data to azure database


print('Connecting to Azure SQL DataBase.........')
#connect to azure database
os.environ["ODBCSYSINI"] = "/home/collabre85"


#sqldriver = [item for item in pyodbc.drivers()][0]
server = 'collabserver.database.windows.net'
database = 'collabDataBase'
username = 'collabuser'
password = 'YTc@3364'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#cnxn = pyodbc.connect('DSN=sqlserverdatasource;Uid=collabuser@collabserver.database.windows.net;DATABASE=collabDataBase;Pwd=YTc@3364;Encrypt=yes;Connection Timeout=30;')

print('Azure SQL Database Connection Complete........')

cursor = cnxn.cursor()
#Insert Dataframe into SQL Server:

#clear current data
cursor.execute('delete from FlashVisionStatus')



print('Pushing data to SQL Database.........')
for index, row in result_cleaned.iterrows():
     cursor.execute("INSERT INTO FlashVisionStatus (Cam_ID,currentTime,camTime,timeDelta) values(?,?,?,?)", row.Cam_ID, row.camTime, row.currentTime,row.timeDelta)


cnxn.commit()
cursor.close()

print('Data transfer COMPLETE..........    :)')

'''
#combine list of dataframes into one dataframe
result = pd.concat(frame_lst,axis=0, ignore_index=False)
'''