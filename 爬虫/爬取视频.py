import requests
from bs4 import BeautifulSoup
import ffmpy3
import re
import csv
from PIL import Image, ImageFilter

Scva_list = []  # selector-video-address
Scvia_list = []  # selector-video-image-address
Scvt_list = []  # selector-video-title
Scvda_list = []  # selector-video-download-address
Scvda_3 = []
soup_9 = []
titles = []
name = input("请输入要搜索的影视名称：")
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.zimuku.la',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
seach_url = 'http://www.zimuku.la/index.php/vod/search.html' + "?wd=" + name  # 当前页面的网址
server = 'http://www.zimuku.la'  # 首页的网址
r = requests.post(url=seach_url, headers=headers)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, 'html.parser')
for Scva in soup.find_all("div", "module-item-pic"):
    for Sva in Scva.find_all("a"):
        Scva_list.append(server + Sva.get("href"))
# print(Scva_list)
for Si in soup.find_all("div", "module-item-pic"):
    for img_urls in Si.find_all("img"):
        Scvia_list.append(img_urls.get("data-src"))
    for img_titles in Si.find_all("img"):
        Scvt_list.append(img_titles.get("alt"))
# print(Scvia_list, Scvt_list)
for Scvda in soup.find_all("div", "video-info-footer"):
    for Svda in Scvda.find_all("a", class_="btn-aux btn-aux-o btn-base"):
        Scvda_list.append(server + Svda.get("href"))
        for Scvda_1 in Scvda_list.find("div", _id="glist-1"):
            for Scvda_2 in Scvda_1.find_all("div", "scroll-content"):
                Scvda_3.append(server + Scvda_2.get("href"))
        print(Scvda_3)

# print(Scvda_list)



