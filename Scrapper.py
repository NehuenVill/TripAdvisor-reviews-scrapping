from selenium import webdriver
from time import sleep

driver =  webdriver.Chrome()

driver.get('https://www.tripadvisor.com/Restaurants-g28970-Washington_DC_District_of_Columbia.html')

sleep(5)

Card = driver.find_element_by_class_name('bGnIM')

sleep(1)

Title = Card.find_element_by_class_name('bHGqj.Cj.b').text

Link = Card.find_element_by_class_name('bHGqj.Cj.b').get_attribute('href')

reviews = Card.find_elements_by_class_name('cJMPr.NE')

Raw = []

for review in reviews:

    rev = review.text

    Raw.append(rev)


print(Link)

print(Raw)

print(Title)