from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# create a new instance of the Chrome driver
driver = webdriver.Firefox()

# navigate to the web application
driver.get("https://www.google.com")

# find the search bar element
search_bar = driver.find_element(by="xpath", value="//li[@class='serp-item']")

# enter the keyword you want to search for
search_bar.send_keys("DragonBall")

# submit the form
search_bar.submit()

# wait for the results to load
time.sleep(5)

# find all the results on the page
results = driver.find_elements(by="xpath", //div[@class='result']")

# loop through the results and print the text of each result
for result in results:
    print(result.text)

# press the 'Page Down' key to load the next page of results
search_bar.send_keys(Keys.PAGE_DOWN)

# wait for the next page of results to load
time.sleep(5)

# find all the results on the second page
results = driver.find_elements(by="xpath", //div[@class='result']")

# loop through the results and print the text of each result
for result in results:
    print(result.text)

# close the browser
driver.close()
