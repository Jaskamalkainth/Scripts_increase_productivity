from selenium import webdriver

print "Sign in to GitHub \n"

emailID = raw_input("Enter Email address: Example ( xyz@gmail.com ) \n" )
Password = raw_input("Enter your Password : Example ( jkthescriptman ) \n")

browser =webdriver.Chrome()
browser.get("https://github.com/login")

inputemail = browser.find_element_by_name('login')
inputpass = browser.find_element_by_name('password')

inputemail.send_keys(emailID)
inputpass.send_keys(Password)


login = browser.find_element_by_name('commit')
login.submit()

