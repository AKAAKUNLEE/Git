import requests
from bs4 import BeautifulSoup
import ffmpy3
import re
import csv
from PIL import Image, ImageFilter

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.zimuku.la',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
f = open('title.txt', 'r', encoding='GBK')
# readline()
# 将文件内容一行一行的读取出来，每次只读一行，读取结果是字符串
result_t = f.readline()
f = open('href.txt', 'r', encoding='GBK')
# readline()
# 将文件内容一行一行的读取出来，每次只读一行，读取结果是字符串
result_h = f.readline()
video_content = requests.get(url="http://www.zimuku.lahttps://dow.dowlz6.com/20221002/12544_8b5ed48b/仙王的日常生活第三季第1话.mp4").content
with open('video\\' + "仙王的日常生活第三季第1话.mp4", mode='wb') as f:
    f.write(video_content)

