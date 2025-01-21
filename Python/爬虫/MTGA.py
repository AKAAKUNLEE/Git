import requests
from bs4 import BeautifulSoup
import ffmpy3
import re
import csv
from PIL import Image, ImageFilter

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
server = 'https://scryfall.com/sets'  # 首页的网址
req = requests.get(url=server, headers=headers).text

print(req)
'''//*[@id="js-checklist"]/tbody'''