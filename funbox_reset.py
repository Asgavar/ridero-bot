import sys
import time
from selenium import webdriver

router_address = sys.argv[1]   # 0 to nazwa pliku
restart_page = router_address+"/supportRestart.html"
password = sys.argv[2]

browser = webdriver.Firefox()

browser.get(router_address)

# login jest sztywno ustawiony na "admin"
password_field = browser.find_element_by_id("PopupPassword")
password_field.send_keys(password)

login_button = browser.find_element_by_id("bt_authenticate")
login_button.click()

time.sleep(2)
browser.get(restart_page)

time.sleep(2)
yes_button = browser.find_element_by_id("bt_yes")
yes_button.click()

browser.quit()
