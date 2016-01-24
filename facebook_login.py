from selenium import webdriver

emailID = raw_input("Enter Email address: Example ( xyz@gmail.com ) " )
Password = raw_input("Enter your Password : Example ( jkthescriptman )")

browser =webdriver.Chrome()
browser.get("https://www.facebook.com")

inputemail = browser.find_element_by_name('email')
inputpass = browser.find_element_by_name('pass')

inputemail.send_keys(emailID)
inputpass.send_keys(Password)


login = browser.find_element_by_id('u_0_l')
login.submit()
