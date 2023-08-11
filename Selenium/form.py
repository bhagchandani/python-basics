from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.set_window_size(1500, 1500)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element(By.NAME, "fName")
fName.send_keys("Beena")

lName = driver.find_element(By.NAME, "lName")
lName.send_keys("Bhagchandani")

email = driver.find_element(By.NAME, "email")
email.send_keys("beenabhagcandani14@gmail.com")

button = driver.find_element(By.TAG_NAME, "button")
button.send_keys(Keys.ENTER)





