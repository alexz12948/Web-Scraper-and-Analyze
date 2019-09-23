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
Input: a list of lines from an html file
Output: N/A
Does: Removes the new line character form the list
'''
def remove_newline(s):
    for i in range(len(s)):
        if s[i] == '\n':
            del s[i]

'''
Input: a list of text
Output: a frequency list of letters
Does: counts the number of letters in an html file
'''
def count_letters(text):
    freq = [0] * 26

    for string in text:
        for char in string:
            if not is_alphanum(char):
                break
            else:
                freq[letter_index(char)] += 1

    return freq

'''
Input: a character
Output: a boolean
Does: checks whether the character is an letter of the alphabet
'''
def is_alphanum(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return True
    elif ord(c) >= 97 and ord(c) <= 122:
        return True

    return False

'''
Input: a character
Output: the index of that character
Does: returns the location in the freq array where the character 
      should be put
'''
def letter_index(c):
    return ord(c.upper()) % 65

'''
Input: a frequency list of characters
Output: N/A
Does: prints out the frequency of each character to the user
'''
def print_freq(freq):
    for i in range(len(freq)):
        print(f"{chr(i + 65)} is in the file {freq[i]} time(s)")

if len(sys.argv) != 2:
    print("Usage: python3 ./web_scrape.py <URL>")
    exit(1)

try:
    source = requests.get(sys.argv[1]).text
except Exception as e:
    print(f"Error: {e}")
    exit(1) 

try:
    soup = BeautifulSoup(source, 'lxml') 
except Exception as e:
    print(f"Error: {e}")
    exit(1)

text = soup.get_text().split('\n')

remove_newline(text)

freq = count_letters(text)

print_freq(freq)

exit(0)