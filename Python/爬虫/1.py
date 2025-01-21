import requests
from bs4 import BeautifulSoup
import ffmpy3
import re

Scva_list = []  # selector-video-address
Scvia_list = []  # selector-video-image-address
Scvt_list = []  # selector-video-title
Scvda_list = []  # selector-video-download-address
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
search_html = BeautifulSoup(r.text, 'html.parser')  # beautifulsoup是一个可以从HTML文件中提取数据的库，lxml用于解析HTML语言。
Scva = search_html.find("div", "module-items")
Scvas = Scva.find_all("div", "module-item-pic")
Scvia = search_html.find("div", "module-items")
Scvias = Scvia.find_all("div", "module-item-pic")
Scvt = search_html.find("div", "module-items")
Scvts = Scvt.find_all("div", "module-item-pic")
Scvda = search_html.find("div", "module-items")
Scvdas = Scvda.find_all("div", "video-info-footer")
print(Scvias)
# print(Scvas)
# print(Scvts)
# print(Scvdas)
"""for i, img_url in enumerate(iu):
        # 用requests库下载图片，并获取二进制数据
        img_data = requests.get(img_url).content
        # 用PIL库打开图片，并转换为RGB模式
        img = Image.open(img_data).convert("RGB")
        # 对图片进行灰度化
        img_gray = img.convert("L")
        # 对图片进行边缘检测
        img_edge = img_gray.filter(ImageFilter.FIND_EDGES)
        # 保存图片到本地，命名为"img_i.jpg"，其中i为序号
        img.save(it+".jpg")
        # 保存灰度化后的图片到本地，命名为"img_gray_i.jpg"，其中i为序号
        img_gray.save("img_gray_" + str(i) + ".jpg")
        # 保存边缘检测后的图片到本地，命名为"img_edge_i.jpg"，其中i为序号
        img_edge.save("img_edge_" + str(i) + ".jpg")"""
'''for S_l in Scvda_list:
    S_l_re = requests.get(url=S_l).text
    soup_1 = BeautifulSoup(S_l_re, 'html.parser')
    for soup_2 in soup_1.find_all("div", "video-info-footer display"):
        for soup_3 in soup_2.find_all("a", class_="btn-aux btn-aux-o btn-large gotodownloadlist"):
            soup_4.append(server + soup_3.get("href"))
    print(soup_4)
for soup_5 in soup_4:
    soup_5_re = requests.get(url=soup_5).text
    soup_6 = BeautifulSoup(soup_5_re, 'html.parser')
    for soup_7 in soup_6.find_all("div", "module-row-one"):
        for soup_8 in soup_7.find_all("a", class_="btn-pc btn-down"):
            href = server + soup_8.get("href")
            soup_9.append(server + soup_8.get("href"))
            title = href.split("/")[-1]
            titles.append(href.split("/")[-1])
            """video_content = requests.get(url=href, headers=headers).content
            with open('video\\' + title, mode='wb') as f:
                f.write(video_content)"""
            filename = "href.txt"
            with open(filename, "w") as file:
                for line in soup_9:
                    file.write(line + "\n")
            filename = "title.txt"
            with open(filename, "w") as file:
                for t in titles:
                    file.write(t + "\n")'''