import parsel
import requests
from bs4 import BeautifulSoup
import ffmpy3
import re
import csv
from PIL import Image, ImageFilter
xhs = []
xhs1 = []
xhs2 = []
xhs3 = []

name = input("请输入要批量获取的链接(只能粘贴作者首页)：")
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'abRequestId=f8df6504-4a4b-5c17-b715-684d5c84ec4f; xsecappid=xhs-pc-web; a1=18b5febf163d0noemj7yi3l7co0jwp9e48iz3g6pp50000343004; webId=8e15259856a772526c9d4fa1e16872a8; gid=yYD2idDfdK48yYD2idDiyYkKKqf8Ild6VWv33UUq1WSl8u28VEUjdq888q4q8848qf02j44J; web_session=040069b0025bed5bf77ab60e02374babb53641; webBuild=3.12.0; unread={%22ub%22:%2265153ac7000000001e03224d%22%2C%22ue%22:%2265329ab2000000001e00f94f%22%2C%22uc%22:26}; cache_feeds=[]; websectiga=6169c1e84f393779a5f7de7303038f3b47a78e47be716e7bec57ccce17d45f99; sec_poison_id=2775a7e0-e3c1-44ef-85be-f5054c36f2ec',
    'Referer': 'https://www.xiaohongshu.com/explore/653742d4000000002402ef20',
    'Sec-Ch-Ua':  '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Sec-Fetch-Dest': "document",
    "Sec-Fetch-Mode": 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
seach_url = name
server = 'https://www.xiaohongshu.com'  # 首页的网址
r = requests.get(url=seach_url, headers=headers).text
# r.encoding = "utf-8"
soup = BeautifulSoup(r, 'html.parser')
for xhs3 in soup.find_all("div", "footer"):
    for xhs2 in xhs3.find_all("a", class_="title"):
        xhs.append(server + xhs2.get("href"))
        for html in xhs:
            href = requests.get(url=html, headers=headers).text
            # print(href)
            soup = BeautifulSoup(href, 'html.parser')
            for picture2 in soup.find_all("div", "swiper-wrapper"):
                picture = picture2.find_all("style")
                print(picture)


