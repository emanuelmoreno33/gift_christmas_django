from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("headless")
options.add_argument("no-sandbox")
options.add_argument("disable-dev-shm-usage")

driver = webdriver.Edge(options = options)

#open the webpage
link = "https://articulo.mercadolibre.com.mx/MLM-1409531990-parches-bordados-metaleros-rock-pack-5-piezas-varios-_JM#reco_item_pos=2&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=754cee15-e598-46e4-8428-a9b7fbe45417"
cleanlink = link.split("#")
driver.get(cleanlink[0])
try:
    productTitle = driver.find_element(by=By.CLASS_NAME,value="ui-pdp-title")
    price = driver.find_element(by=By.CLASS_NAME,value="andes-money-amount__fraction")
    imageproduct = driver.find_element(by=By.XPATH,value="/html/body/main/div/div[4]/div/div[2]/div[1]/div/div/div/div[2]/span[1]/figure/img")
    print(productTitle.text)
    print(price.text)
    print(imageproduct.get_attribute("src"))

    driver.quit()
except Exception as ex:
    pass
