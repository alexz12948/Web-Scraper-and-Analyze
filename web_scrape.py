'''
Author: Alexander Zsikla
Name: web_scrape.py
Fall 2019

Description: 

'''

from bs4 import BeautifulSoup
import requests
import sys

'''
Input:
Output:
Does:
'''
def remove_newline(s):
    for i in range(len(s)):
        if s[i] == '\n':
            del s[i]
    
    print(s)

'''
Input:
Output:
Does:
'''
def count_vowels(s):
    pass

if len(sys.argv) != 2:
    print("Usage: python3 ./web_scrape.py <URL>")
    exit(1)

try:
    source = requests.get(sys.argv[1]).text
except Exception as e:
    print(f"Error: {e}")
    #exit(1) 

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml') 

text = soup.get_text().split('\n')

remove_newline(text)

for word in text:
    if word == '':
        continue
    else:
        print(f"Word: {word}")





#print(soup.prettify())
#print(soup.title.text)
#print(soup.find('div', class_='footer').text)

