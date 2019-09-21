from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())
print(soup.title.text)
print(soup.find('div', class_='footer').text)

