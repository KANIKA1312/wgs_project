import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime
import wgs_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.chrome.options import Options


s = Service(executable_path='C:\wegostudy\chromedriver.exe')
driver = webdriver.Chrome(service=s)

def setUp():
    print(f'This We Go Study Test Start at : {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
          f' on {datetime.datetime.today().strftime("%A")}')
    print('-----------------~~~~~~-------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.web_url)
    assert driver.current_url == locators.web_url
    assert driver.title == locators.web_title
    print('We Go Study Launched Successfully!!')
    print('')
    sleep(1)

def log_in():
    sleep(2)
    driver.find_element(By.LINK_TEXT,'LOGIN').click()
    sleep(0.25)
    driver.find_element(By.ID,'user_email').send_keys('chris.velasco78@gmail.com')
    sleep(0.25)
    driver.find_element(By.ID,'user_password').send_keys('123cctb')
    sleep(0.25)
    driver.find_element(By.NAME,'commit').click()
    sleep(1)
  bbbb nb b       

setUp()
log_in()