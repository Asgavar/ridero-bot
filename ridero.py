import os
import time
from threading import Timer
from selenium import webdriver

t = Timer(180, os._exit, [255])   # jesli po drodze cos sie zawiesi
t.start()

book_url = "https://ridero.eu/pl/books/<url tutaj>"
tempmail_url = "https://temp-mail.org/pl/"

browser = webdriver.Firefox()

browser.get(tempmail_url)

address_field = browser.find_element_by_id("mail")   # tag <input> o id = mail
mail_address = address_field.get_attribute("value")

browser.get(book_url)

vote_button = browser.find_element_by_tag_name("button")
vote_button.click()

voting_method_buttons = browser.find_element_by_class_name("votingButtons").find_elements_by_tag_name("input")

vote_by_email = voting_method_buttons[2]

time.sleep(2)   # zaczekaj dwie sekundy (zeby okienko mialo czas by wyskoczyc)
vote_by_email.click()

time.sleep(2)   # j.w.
email_field = browser.find_elements_by_class_name("p-inner")[1].find_element_by_tag_name("input")
# TODO: zmienic zagniezdzone szukanie elementow na XPathy

email_field.send_keys(mail_address)
send_button = browser.find_elements_by_class_name("info-text")[1].find_element_by_tag_name("button")
send_button.click()

time.sleep(5)

browser.get(tempmail_url)

time.sleep(10)
view_mail_link = browser.find_element_by_partial_link_text("Misja")
view_mail_link.click()

time.sleep(3)
confirmation_link = browser.find_element_by_partial_link_text("ridero.eu")
confirmation_link.click()

time.sleep(5)
browser.quit()   # zamyka sie i czeka do odliczenia 60 sekund

os._exit(119)   # wszystko poszlo ok
