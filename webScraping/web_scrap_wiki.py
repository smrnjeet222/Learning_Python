from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

android_url = "https://en.wikipedia.org/wiki/Android_version_history"

android_data = urlopen(android_url)

android_html = android_data.read()

android_soup = soup(android_html, 'html.parser')
# print (android_soup)
# android_soup.h1
# android_soup.findAll('h1', {})

tables = android_soup.findAll('table',{'class':'wikitable'})
print(len(tables))

android_table = tables[0]
# print(android_table)
# print (android_html)

headers = android_table.findAll('th')[:-1]
print (len(headers))

column_titles = [ct.text[:-1] for ct in headers]
print (column_titles)

rows_data = android_table.findAll('tr')[3:]
# print(rows_data)

first_row = rows_data[0].findAll('td', {})
for d in first_row:
    print(d.text[:-1])


table_rows = []
for row in rows_data:
    current_row = []
    rows_data = row.findAll('td',{})[:-1]
    for idx,data in enumerate(rows_data):
        current_row.append(data.text[:-1])

    table_rows.append(current_row)

# print(table_rows)

filename = 'android_ver_hist.csv'

with open(filename, 'w', encoding = 'utf-8') as f:
    header_string = ','.join(column_titles)
    header_string += '\n'
    f.write(header_string)

    for row in table_rows:
        row[2] = row[2].replace(',','')
        row_string = ""
        row_string = ','.join(row)
        row_string += '\n'
        f.write(row_string)

android_data.close()

df = pd.read_csv(filename)

print(df)