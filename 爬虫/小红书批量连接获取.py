import requests
from bs4 import BeautifulSoup
import ffmpy3
import re
import csv
from PIL import Image, ImageFilter

name = input("请输入要搜索的笔记：")
headers = {
    ':authority': 'www.xiaohongshu.com',
    ':method': 'GET',
    ':scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'abRequestId=f8df6504-4a4b-5c17-b715-684d5c84ec4f; xsecappid=xhs-pc-web; a1=18b5febf163d0noemj7yi3l7co0jwp9e48iz3g6pp50000343004; webId=8e15259856a772526c9d4fa1e16872a8; gid=yYD2idDfdK48yYD2idDiyYkKKqf8Ild6VWv33UUq1WSl8u28VEUjdq888q4q8848qf02j44J; web_session=040069b0025bed5bf77abf8a02374bc3ab4f01; webBuild=3.13.5; cache_feeds=[]; unread={%22ub%22:%22653da2b7000000002500b4ce%22%2C%22ue%22:%22653ddc1300000000250153cb%22%2C%22uc%22:40}; websectiga=3633fe24d49c7dd0eb923edc8205740f10fdb18b25d424d2a2322c6196d2a4ad; sec_poison_id=f90d67f1-99c3-488f-a4b6-bf99fa6a067b',
    'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}
seach_url = 'https://www.xiaohongshu.com/search_result?keyword=' + name + "&source=web_search_result_notes"
server = 'https://www.xiaohongshu.com'  # 首页的网址
r_seach_url = requests.get(url=seach_url, headers=headers).text
print(r_seach_url)
