from selenium import webdriver
user = "6428546570921905819"
pwd = "nakki1234nakki"
driver = webdriver.Firefox()
driver.get("https://hel-jobs.eu/signup/")

username = driver.find_element_by_xpath('//*[@id="solver"]')
password = driver.find_element_by_xpath('//*[@id="password"]')

username.send_keys("6428546570921905819")
password.send_keys("nakki1234nakki")

input("press key to continue")

driver.find_element_by_id("setpassword").click()

# while True:


driver.close()
