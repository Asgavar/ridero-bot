from robobrowser import RoboBrowser

book_url = "https://ridero.eu/pl/books/na_marginesie/"   # ukryty, ale fizycznie przycisk juz tam jest xD
browser = RoboBrowser()

browser.open(book_url)

# print(browser.parsed)

vote_button = browser.get_link(u"Zagłosuj na książkę")
print(vote_button)
