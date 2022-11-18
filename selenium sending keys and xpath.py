import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.binary_location = r'firefox.exe' # path to firefox.exe file

s = Service('geckodriver.exe') # path to geckodriver.exe file
driver = webdriver.Firefox(service=s, options=options)
driver.get('https://hyperskill.org/tracks')
sign_in = driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']")
sign_in.click()

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.XPATH, "//h2[normalize-space()='Sign in to JetBrains Academy']") ,
        "Sign in to JetBrains Academy"
    )
)

email = driver.find_element(By.XPATH, "//input[@id='__BVID__58']")
email.send_keys("test@test.com")
password = driver.find_element(By.XPATH, "//input[@id='__BVID__60']")
password.send_keys("testtset")
sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
sign_in_button.click()