import requests, json
from bs4 import BeautifulSoup

def get(url):
    request = requests.get(url)
    content = request.content
    return BeautifulSoup(content, "html5lib")