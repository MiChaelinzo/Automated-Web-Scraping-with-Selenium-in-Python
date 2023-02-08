from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Set up the web driver
driver = webdriver.Firefox()

# Navigate to the target website
driver.get("https://www.google.com")

# Find the search bar
search_bar = driver.find_element(By.NAME, value="q")

# Enter the search keyword
search_bar.send_keys("DragonBall")
search_bar.send_keys(Keys.RETURN)

# Wait for the results to load
wait = WebDriverWait(driver, 10)
results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='g']")))

# Extract the information from the results
for result in results:
    # Extract the title
    title = result.find_element(By.XPATH, value=".//h3").text

    # Extract the description
    description = result.find_element(by=By.XPATH, value=".//span[@class='st']").text

    # Extract the link
    link = result.find_element(By.XPATH, value=".//a").get_attribute("href")

    # Do something with the extracted information (e.g. print it, write it to a file, etc.)
    print(f"Title: {title}\nDescription: {description}\nLink: {link}\n")

# Close the web driver
driver.quit()


