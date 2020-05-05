from selenium import webdriver

import time

url = "https://www.google.com/maps/search/?api=1&query=THE+DUFFEYROLL+CAFE+1290+S+PEARL+ST+DENVER+80210"

driver=webdriver.Chrome()
driver.get(url)
time.sleep(5)
elements = driver.find_elements("css selector",'button.widget-pane-link')

print(elements)
for elem in elements:
    print(elem.text)
