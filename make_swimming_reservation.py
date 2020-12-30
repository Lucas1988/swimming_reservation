from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--incognito")

driver = webdriver.Chrome(
    executable_path=ChromeDriverManager().install(), chrome_options=chromeOptions
)
driver.get("https://zwembaddekrommerijn.nl/reserveren/#/lesRooster/")

driver.set_window_size(2000, 1500)

# Move to the right item
actions = webdriver.common.action_chains.ActionChains(driver)
actions.send_keys(Keys.TAB * 27)
actions.perform()

element = driver.find_element_by_id("d4feed33-fba1-4bba-abbe-239c71c1c449_agenda_titel")
print(element.text)
# if 'Zondag 11:00 - 11:45' in element.text:
# Enter username
time.sleep(1)
inputElement = driver.find_element_by_id(
    "d4feed33-fba1-4bba-abbe-239c71c1c449_agenda_loginComponent_uidInput"
)
inputElement.send_keys("###")
# Enter password
inputElement = driver.find_element_by_id(
    "d4feed33-fba1-4bba-abbe-239c71c1c449_agenda_loginComponent_pwdInput"
)
inputElement.send_keys("###")
inputElement.send_keys(Keys.ENTER)
time.sleep(1)
# Subscribe for lesson
aanmeldknop = driver.find_element_by_id(
    "d4feed33-fba1-4bba-abbe-239c71c1c449_agenda_aanmeldknop"
)
aanmeldknop.click()

time.sleep(10)

driver.close()
