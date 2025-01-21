import requests
from bs4 import BeautifulSoup
import os

"""def download_comic_images(url, save_path):
    # 创建保存图片的目录
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    while url:
        # 发送请求获取页面内容
        response = requests.get(url)
        response.raise_for_status()

        # 使用BeautifulSoup解析页面
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找漫画图片的URL
        img_tag = soup.find('img', {'class': 'comicpic'})
        if img_tag:
            img_url = img_tag['src']
            # 下载图片
            img_response = requests.get(img_url)
            img_response.raise_for_status()

            # 保存图片
            img_name = os.path.basename(img_url)
            with open(os.path.join(save_path, img_name), 'wb') as f:
                f.write(img_response.content)

        # 查找下一页的URL
        next_page_tag = soup.find('a', {'class': 'next'})
        if next_page_tag:
            url = next_page_tag['href']
        else:
            url = None

# 指定漫画的URL和保存路径
comic_url = 'https://www.gufengmh.com/manhua/wozaijingshenbingyuanxuezhanshendiyiji/'
save_directory = 'comic_images'

# 调用函数下载漫画图片
download_comic_images(comic_url, save_directory)
"""