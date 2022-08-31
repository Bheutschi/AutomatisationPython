import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import *

driver = webdriver.Chrome()

driver.get("https://accounts.zoho.eu/signin?servicename=ZohoRecruit&signupurl=https://www.zoho.eu/recruit/signup.html")

driver.maximize_window()


def recupererUneValeur(id, nomId):
    element = driver.find_element(id, nomId)
    return element


recupererUneValeur("id", "login_id").send_keys("ro@itadvanced.ch")

recupererUneValeur("id", "nextbtn").click()

time.sleep(3)
element = driver.find_element("id", "password")
f = open("../../secret.txt", "r")
fichier = f.read()
element.send_keys(fichier)

recupererUneValeur("id", "nextbtn").click()

time.sleep(5)
recupererUneValeur("id", "tab_Leads").click()

time.sleep(5)
recupererUneValeur("id", "importButton").click()

time.sleep(3)
element = driver.find_element(By.XPATH, "//*[@data-zrqa=\'importFromDoc\']")

element.click()

time.sleep(2)

element = driver.find_element(By.XPATH, '//*[@id="customButtonDetailsHead"]')

element_click = element.click()
time.sleep(2)
element_click.send_keys("/Users/BH-PCIT001/CV_Test.pdf")
