from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests

# if text appears weird uncomment below line
# import os
# os.system("cls")

reset = '\033[0m'
bold = '\033[1m'
italic = '\x1B[3m'
cyan = '\033[36m'
darkgrey = '\033[90m'
white = '\u001b[37;1m'
red = '\u001b[31;1m'
yel = '\u001b[33;1m'

PARSER = 'html.parser'
URL = 'https://www.dictionary.com/e/word-of-the-day/'

try:
    resp = requests.get(URL)

    http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, PARSER, from_encoding=encoding)

    word_page = soup.find(class_='wotd-item-headword__anchors-link').get('href')

    word_resp = requests.get(word_page)

    http_encoding = word_resp.encoding if 'charset' in word_resp.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(word_resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    word_soup = BeautifulSoup(word_resp.content, PARSER, from_encoding=encoding)


    word = word_soup.find('h1', class_='css-1jzk4d9 e1rg2mtf8').text.strip()
    pron = word_soup.find('div', class_='pron-spell-container css-1hyfx7x evh0tcl1').text.strip()[:-8]
    kind = word_soup.find('span', class_='luna-pos').text.strip()


    print(bold+ yel +word.upper() + "  "+ cyan + pron+reset)
    print(italic+ darkgrey + kind + reset +'\n')
    parent = word_soup.find('div', class_='css-1o58fj8 e1hk9ate4')
    try:
        for definition in parent.find_all('div'):
            print(white + definition['value']+ ". " + red + definition.text.strip() + reset)
    except:
        for definition in parent.find('div', class_='default-content').find_all('div'):
            print(white + definition['value']+ ". " + red + definition.text.strip() + reset)
except :
    print("No Result Found")
