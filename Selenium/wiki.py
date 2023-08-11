from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.set_window_size(1500, 1500)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

history = driver.find_element(By.LINK_TEXT, "View history")
#history.click()

input_text = driver.find_element(By.NAME, "search")

driver.implicitly_wait(5)
input_text.send_keys("Python")
input_text.send_keys(Keys.ENTER)

