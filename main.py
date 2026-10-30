import os
import time
from datetime import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Entrada import NAME, LASTNAME, EMAIL, MOBILE, COUNTRY, PASSWORD



options = webdriver.ChromeOptions()
options.add_argument("--start-fullscreen")
open_browser = webdriver.Chrome(options=options)


open_browser.get("https://qa-practice.netlify.app/bugs-form")


wait = WebDriverWait(open_browser, 10)


time.sleep(5)




name = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "firstName")
    )
)
name.send_keys(NAME)

lastname = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "lastName")
    )
)
lastname.send_keys(LASTNAME)

phone = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "phone")
    )
)
phone.send_keys(MOBILE)


Country = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "countries_dropdown_menu")
    )
)
Country.send_keys(COUNTRY)
Country.send_keys(Keys.TAB)


email = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "emailAddress")
    )
)
email.send_keys(EMAIL)



password = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "password")
    )
)
password.send_keys(PASSWORD)

submir = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "registerBtn")
    )
)
submir.click()


time.sleep(15)

open_browser.quit()
