from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def get_video_url_selenium(url):
    try:
        # 设置Chrome选项
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 无头模式，不打开浏览器窗口
        chrome_options.add_argument("--disable-gpu")

        # 指定ChromeDriver路径
        service = Service('path/to/chromedriver')

        # 创建WebDriver对象
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # 打开目标URL
        driver.get(url)

        # 等待页面加载完成
        time.sleep(5)  # 根据实际情况调整等待时间

        # 查找视频链接
        video_node = driver.find_element(By.TAG_NAME, 'video') or driver.find_element(By.CLASS_NAME, 'video-link')

        if video_node:
            video_url = video_node.get_attribute('src') or video_node.get_attribute('href')
            return video_url
        else:
            print("未找到视频链接")
            return None
    except Exception as e:
        print(f"请求失败: {e}")
        return None
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://www.kkys02.com/play/54125-35-25552.html"
    video_url = get_video_url_selenium(url)

    if video_url:
        print(f"视频链接: {video_url}")
    else:
        print("未能获取视频链接")