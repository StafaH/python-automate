from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebElement

import time
import sys

if len(sys.argv) == 1:
    print("Enter Username:")
    username = input()
    print("Enter Password:")
    password = input()


if len(sys.argv) == 2:
    sys.exit("Arugment Syntax Error: arg1=username, arg2=password")

if len(sys.argv) == 3:
    username = sys.argv[1]
    password = sys.argv[2]

driver = webdriver.Chrome('C:\Code\python-automate\chromedriver')
driver.get("https://uozone2.uottawa.ca/?language=en")

elem_username = driver.find_element_by_id('userNameInput')
elem_password = driver.find_element_by_id('passwordInput')

elem_username.clear()
elem_username.send_keys(username)

elem_password.clear()
elem_password.send_keys(password)
elem_password.send_keys(Keys.RETURN)

driver.get("https://www.uocampus.uottawa.ca/psp/csprpr9www/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_GRADE.GBL?languageCd=ENG")

frame = driver.find_element_by_tag_name('iframe')
driver.switch_to_frame(frame)

gradetable = driver.find_element_by_xpath("//table[@class='PSLEVEL1GRID']")

for row in gradetable.find_elements_by_xpath(".//tr"):
    print([td.text for td in row.find_elements_by_xpath(".//td")])

#optional
#driver.close()