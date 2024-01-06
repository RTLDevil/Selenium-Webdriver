# Import the selenium Package
from selenium import webdriver
from selenium.webdriver.common.by import By
# Keep the Browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create the Webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com.au/Apple-iPhone-13-256GB-Starlight/dp/B09L7QQLPV/ref=sr_1_1_sspa?crid=6GUTLPLFPKDF&keywords=iphone&qid=1704511937&sprefix=iphon%2Caps%2C325&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
# Use the find_element methiord to locate the price of Product
Price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# Print the outcome
print(f"The price is {Price_dollar.text}.{price_cent.text}")

# Finally Quit the program by using quit() method.
driver.quit()