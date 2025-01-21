import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import service
# 1.打开一个浏览器页面
Edge = webdriver.Edge(r'D:\Git\Python\msedgedriver.exe')
# 2.输入网址
Edge.get('http://manhuatai.org/')
# 3.取数据
Edge.maximize_window()  # 最大化浏览器窗口
# 定位到百度首页的搜索框
search_input = Edge.find_element(By.ID, 'searchkey')
# 在搜索框内输入"Python"
search_input.send_keys("修真聊天群")
# 定位到搜索按钮
search_button = Edge.find_element(By.CLASS_NAME, 'search_btn')
# 点击搜索按钮
search_button.click()
# 阻塞，不让程序终止
input()

# url = "http://manhuatai.org/"
# response = requests.get(url)
# comic = input("请输入要搜索的漫画：")
# print(type(comic))
