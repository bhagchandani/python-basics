from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.python.org/")

events_dates = driver.find_elements(By.CLASS_NAME, "event-widget time")
#events_years = driver.find_elements(By.CLASS_NAME, "event-widget .say-no-more")
events_titles = driver.find_elements(By.CLASS_NAME, "event-widget li a")
upcoming_events = {}


for n in range(len(events_dates)):
	upcoming_events[n] = {
		"time" : events_dates[n].text,
		"name" : events_titles[n].text
	}

print(upcoming_events)
driver.quit()