from selenium import webdriver

query = raw_input("Enter your Query ..\n")

browser = webdriver.Chrome()
browser.get("https://www.google.com")

search_box = browser.find_element_by_name('q')
search_box.send_keys(query)
search_box.submit()


