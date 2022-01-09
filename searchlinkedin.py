from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Edge(executable_path='C:\DEV\web-scrapy-Linkedin\msedgedriver')

browser.get("https://www.linkedin.com/login")

input_email = browser.find_element_by_id("username")
input_email.send_keys('my_account_mail')

input_pass = browser.find_element_by_id("password")
input_pass.send_keys('my_password')

btn_login = browser.find_element_by_xpath("//button[@type='submit']")
btn_login.click()

search = browser.find_element_by_xpath("//input[@placeholder='Pesquisar']")
search.send_keys("Python")
search.send_keys(Keys.RETURN)

time.sleep(3)

filter_jobs = browser.find_element_by_xpath("//button[@aria-label='Vagas']")
filter_jobs.click()

input('')