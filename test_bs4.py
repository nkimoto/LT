import requests
from bs4 import BeautifulSoup
URL = 'https://www.google.com/'
resp = requests.get(URL)
soup = BeautifulSoup(resp.text, features="html.parser")
# titleタグの取得
print(soup.title.text)
