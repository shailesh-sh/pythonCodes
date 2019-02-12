import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:\\Users\\sk\\Desktop\\chromedriver_win32\\chromedriver.exe")
time.sleep(2)
driver.get("http://www.vado.com/stockists")
assert "Stockists List| Vado"
city = ["London","New York","Delhi"]

for i in city :
    elem = driver.find_element_by_id("search_field")
    elem.send_keys(i)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    print (driver.current_url)
    time.sleep(1)
