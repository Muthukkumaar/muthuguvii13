from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open the Instagram profile
driver.get("https://www.instagram.com/guviofficial/")

# Wait for the page to load
driver.implicitly_wait(10)

# Extract total number of followers
followers = driver.find_element(By.XPATH, "//ul[@class='k9GMp ']/li[2]/a/span").text

# Extract total number of following
following = driver.find_element(By.XPATH, "//ul[@class='k9GMp ']/li[3]/a/span").text

# Print the results
print("Followers:", followers)
print("Following:", following)

# Close the webdriver
driver.quit()