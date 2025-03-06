import json
import os
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 支持的平台
PLATFORMS = {
    "bilibili": "https://www.bilibili.com",
    "youtube": "https://www.youtube.com",
    "youku": "https://www.youku.com",
}

def get_cookie(platform_url, platform_name):
    """
    获取指定平台的cookie
    """
    # 配置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无头模式
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # 启动Chrome浏览器
    driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=chrome_options)

    try:
        # 打开目标平台
        print(f"正在访问 {platform_name}...")
        driver.get(platform_url)
        time.sleep(10)  # 等待页面加载

        # 获取cookie
        cookies = driver.get_cookies()
        print(f"成功获取 {platform_name} 的cookie！")

        # 保存cookie到本地文件
        save_cookie(cookies, platform_name)
    finally:
        driver.quit()

def save_cookie(cookies, platform_name):
    """
    将cookie保存为JSON文件
    """
    if not os.path.exists("cookies"):
        os.makedirs("cookies")  # 创建存储目录

    # 保存文件
    file_path = f"cookies/{platform_name}_cookies.json"
    with open(file_path, 'w') as file:
        json.dump(cookies, file, indent=4)
    print(f"Cookie已保存到 {file_path}")

def main():
    """
    主程序
    """
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="QuickCookie: 快速获取视频平台cookie")
    parser.add_argument("--platform", required=True, choices=PLATFORMS.keys(), help="目标平台名称")
    args = parser.parse_args()

    # 获取平台URL
    platform_url = PLATFORMS[args.platform]

    # 获取cookie
    get_cookie(platform_url, args.platform)

if __name__ == "__main__":
    main()
