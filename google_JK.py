import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.google.com")
search_box = browser.find_element_by_name('q')

search_box.send_keys('Jaskamal Kainth')
search_box.submit()



