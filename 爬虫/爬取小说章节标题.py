import requests
import parsel

url = "http://www.77nt.info/kehuan"  # 用自定义的变量接收字符串数据内容 url
#
response = requests.get(url)
response.encoding = "utf-8"
# 编码  utf-8编码格式 gbk编码格式

# print(response.text)
selector = parsel.Selector(response.text)
# response.text是字符串数据
# selector将其转换成可解析的对象
"""for i in range(30):
    Scl = selector.css('body > div.main > div.books > div > div > h2 > a').get()
    print(Scl)"""
"""
CSS
Scl = selector.css('body > div.main > div.books > div > div > h2 > a').get()
print(Scl)
Sct = selector.css('body > div.main > div.books > div > div > h2 > a::text').get()
print(Sct)"""
# xpath
x_Scl = selector.xpath('//*[@class="title"]/h2/a').getall()
print(x_Scl)
x_Sct = selector.xpath('//*[@class="title"]/h2/a/text()').getall()
print(x_Sct)
