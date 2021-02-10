from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(5)

contacts = ['contact']
messsages = ['message']

##text = open('text.txt', 'r', encoding="utf8")

def search_contact(contact):
    search_field = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    search_field.click()
    search_field.send_keys(contact)
    time.sleep(0.5)
    search_field.send_keys(Keys.ENTER)

def send_message(message):
    message_field = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    message_field[1].click()
    message_field[1].send_keys(message)
    time.sleep(0.5)
    message_field[1].send_keys(Keys.ENTER)

for contact in contacts:
    search_contact(contact)
    for message in messsages:
         send_message(message)
    ##for line in text:
        ##send_message(line)

