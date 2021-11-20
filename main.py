from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
s = Service('/Users/evankolberg/PycharmProjects/tinypoll-bot/chromedriver')

driver = webdriver.Chrome(service=s, options=options)

link = input('Enter a link to a tinypoll to bot the hell out of:  ')
bots = int(input('Now, how many bots would you like?: '))


def go(link, bots):
    for i in range(bots):
        driver.get(link)
        WebDriverWait(driver, 8).until(expected_conditions.presence_of_element_located((By.ID, 'ember4')))
        driver.find_element(By.ID, 'ember4').send_keys(f'BOT#{i+1}')


if __name__ == '__main__':
    go(link, bots)
