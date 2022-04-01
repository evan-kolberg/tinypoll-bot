from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
s = Service('/Users/evankolberg/PycharmProjects/tinypoll-bot/chromedriver')

driver = webdriver.Chrome(service=s, options=options)

link = input('Enter Link:  ')
name = input('Enter a Name:  ')
option = input('Enter Your Choice:  ')

# Note: You must find a way to clear the data of the current webdriver session, so you can re-login.
# At this current state, you can only log in once and select an option, but can't re-login due to cookies, cache, etc.

def login(arg_link, arg_name):
    driver.get(arg_link)
    WebDriverWait(driver, 8).until(
        expected_conditions.presence_of_element_located((By.ID, 'ember4'))).send_keys(arg_name)
    WebDriverWait(driver, 8).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//button[normalize-space()="Save"]'))).click()


def select_option(arg_option):
    WebDriverWait(driver, 8).until(
        expected_conditions.presence_of_element_located((By.XPATH, f'//span[text()="{arg_option}"]'))).click()


if __name__ == '__main__':
    login(link, name)
    sleep(2)
    select_option(option)
    driver.quit()
