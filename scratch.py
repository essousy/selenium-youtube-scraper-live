import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL='https://www.youtube.com/feed/trending'

response = requests.get(YOUTUBE_TRENDING_URL)

print('Status Code', response.status_code)



doc = BeautifulSoup(response.text, 'html.parser')

print('Page Title:', doc.title.text)