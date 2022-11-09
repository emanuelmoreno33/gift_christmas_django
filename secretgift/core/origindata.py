from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def getdataAmazon(link):
    try:

        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        #open the webpage
        driver.get(link)
        try:
            productTitle = driver.find_element(by=By.ID,value="productTitle")
            price = driver.find_element(by=By.CLASS_NAME,value="a-price-whole")
            imageproduct = driver.find_element(by=By.ID,value="landingImage")
            pricestring = price.text.replace(',', '')

            dictdata={
                "link":link,
                "name":productTitle.text,
                "imagelink":imageproduct.get_attribute("src"),
                "price":float(pricestring)
            }
            driver.quit()

            return dictdata
        except Exception as ex:
            print(ex)
            return {"link":link}
        
    except Exception as e:
        return None

def getDataML(link):
    try:

        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

        #open the webpage
        cleanlink = link.split("#")
        driver.get(cleanlink[0])
        try:
            productTitle = driver.find_element(by=By.CLASS_NAME,value="ui-pdp-title")
            price = driver.find_element(by=By.CLASS_NAME,value="andes-money-amount__fraction")
            imageproduct = driver.find_element(by=By.CLASS_NAME,value="ui-pdp-gallery__figure__image")
            pricestring = price.text.replace(',', '')   

            dictdata={
                "link":link,
                "name":productTitle.text,
                "imagelink":imageproduct.get_attribute("src"),
                "price":float(pricestring)
            }
            driver.quit()

            return dictdata
        except Exception as ex:
            print(ex)
            cleanlink = link.split("#")
            return {"link":cleanlink[0]}
    except Exception as e:
        return None
