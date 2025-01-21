import re

import requests
from lxml import etree
import time
import urllib3
import parsel

Scva = []  # selector-video-address
Scvia = []  # selector-video-image-address
Scvt = []  # selector-video-title
Scvda = []  # selector-video-download-address
urllib3.disable_warnings()
name = input("请输入要搜索的影视名称：")
headurl = 'http://www.zimuku.la'
url = 'http://www.zimuku.la/index.php/vod/search.html' + "?wd=" + name
# url1 = 'http://www.zimuku.la/index.php/vod/search.html?wd=仙王'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.zimuku.la',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers).text
selector = parsel.Selector(response)
# CSS
Scva = selector.css(
    '#main > div > div.module > div > div > div.module-search-item> div.video-cover > div > div > a').getall()
Scvt = selector.css(
    '#main > div > div.module > div > div > div.module-search-item> div.video-cover > div > div >img').getall()
Scvda = selector.css(
    '#main > div > div.module > div > div > div.module-search-item > div.video-info > div.video-info-footer > a.btn-aux.btn-aux-o.btn-base').getall()
Scvia = selector.css(
    '#main > div > div.module > div > div > div.module-search-item> div.video-cover > div > div >img').getall()
"""
print(response)

"""
'''
for Scva in Scva:
    Scva = re.findall('href(.*?)title')
'''
print(Scvia)
print(Scva)
print(Scvt)
print(Scvda)
'''re_Scva.findall
re_Scvt.findall
re_Scvda.findall
re_Scvia.findall'''
