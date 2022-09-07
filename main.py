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

element = driver.find_element(By.XPATH, '//*[@id="mainmenua_econn_0"]/span/a')
element.click()

#clique sur le bouton Documents de la liste du bouton Browse
element = driver.find_element(By.XPATH, '//*[@id="mainmenua_econn_0"]/span/a/ul/li[3]')
element.click()


time.sleep(2)
element = driver.find_element(By.XPATH, '//*[@id="314dl854ecc4d77ad4162b67cfc07d62db473"]/table/tbody/tr/td/table')
element.click()
# /html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr/td/table/tbody/tr/td[1]
# /html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div[3]/table/tbody/tr/td/table/tbody/tr/td[1]
# /html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div[4]/table/tbody/tr/td/table/tbody/tr/td[1]

# time.sleep(2)
#
# element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[3]/input[2]')
# element.click()
#
# time.sleep(2)
# element = driver.find_element(By.XPATH, '/html/body/div[13]/div[16]/div/form/div/div[1]/div/div[8]/input')
# element.click()
