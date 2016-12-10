# import re

# from robobrowser import RoboBrowser

book_url = "https://ridero.eu/pl/books/bicie_serc/"   # ukryty, ale fizycznie przycisk juz tam jest xD
tempmail_url = "https://temp-mail.org/pl/"


# browser = RoboBrowser()
#
# browser.open(tempmail_url)
#
# address_field = browser.select("#mail")   # tag <input> o id = mail
#
# address_pattern = r"value=\".*\""   # wyrazenie regularne, szuka atrybutu value
#
# mail_address = re.findall(address_pattern, str(address_field))[0]   # zwraca liste z jednym elementem
# mail_address = mail_address[7:len(mail_address)-1]   # wyciecie value= i zostawienie samej wartosci atrybutu
#
# print(mail_address)

# browser.open(book_url)

# vote_button = browser.get_link(u"Zagłosuj na książkę")

# inp = browser.get_forms()

# print(inp)
