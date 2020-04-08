import requests 
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")

src = result.content
soup = BeautifulSoup(src , "html.parser")

urls = []
headlines = []
for h2_tags in soup.findAll("h2"):
    a_tag = h2_tags.find('a')
    headlines.append(a_tag.text)
    urls.append(a_tag.attrs["href"])

print(headlines[0])
print(urls[0])