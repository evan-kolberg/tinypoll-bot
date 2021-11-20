from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
s = Service('/Users/evankolberg/PycharmProjects/tinypoll-bot/chromedriver')

driver = webdriver.Chrome(service=s, options=options)

link = 'https://vote.usetinypoll.com/?poll=eyJwb2xsSUQiOiJDRTg3QzZEQy1GNjkzLTQ4NEEtQjI3NC02NTdEOTBFMzAxQzYiLCJ0aXRsZSI6IldoYXQgdG8gZG8iLCJvcHRpb25zIjpbeyJuYW1lIjoiR28gdG8gdG93biIsIm9wdGlvbklEIjoiMDE4Nzc0QjgtMEJGNy00NDI3LUEwRTUtMjJBQzc2RjEwMDVFIn0seyJuYW1lIjoiSWNlIHNrYXRpbmciLCJvcHRpb25JRCI6IkU0QTI0MUQyLTA3NUUtNEYxNC04NURDLTZFMkVFOTcyNzIyNCJ9LHsibmFtZSI6Ikhhbmcgb3V0Iiwib3B0aW9uSUQiOiIwODI1MDczQi04M0ZELTQ3RkYtOEUxRi1EMDhFQjcxQThBQzQifV19'
title = 'Hang out'


def go(link, title):
    driver.get(link)
    WebDriverWait(driver, 8).until(expected_conditions.presence_of_element_located((By.ID, 'ember4')))
    driver.find_element(By.ID, 'ember4').send_keys('H4CK3R')
    driver.find_element(By.XPATH, '//button[normalize-space()="Save"]').click()
    driver.find_element(By.XPATH, f'//span[text()="{title}"]').click()


if __name__ == '__main__':
    go(link, title)
