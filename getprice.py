from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("headless")
options.add_argument("no-sandbox")
options.add_argument("disable-dev-shm-usage")

driver = webdriver.Edge(options = options)

#open the webpage
driver.get("https://a.co/d/aj5DP51")
try:
    productTitle = driver.find_element(by=By.ID,value="productTitle")
    price = driver.find_element(by=By.CLASS_NAME,value="a-price-whole")
    imageproduct = driver.find_element(by=By.ID,value="landingImage")

    print(productTitle.text)
    print(price.text)
    print(imageproduct.get_attribute("src"))

    driver.quit()
except Exception as ex:
    pass