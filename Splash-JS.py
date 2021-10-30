# Splash - Render JS
# Tutorial from John Watson Rooney YouTube channel

import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/s?k=nvidia+geforce+rtx+3080'

response = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title.text)