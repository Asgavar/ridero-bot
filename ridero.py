import time
from selenium import webdriver

book_url = "https://ridero.eu/pl/books/bicie_serc/"
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

time.sleep(5)   # zaczekaj piec sekund (zeby okienko mialo czas by wyskoczyc)
vote_by_email.click()
