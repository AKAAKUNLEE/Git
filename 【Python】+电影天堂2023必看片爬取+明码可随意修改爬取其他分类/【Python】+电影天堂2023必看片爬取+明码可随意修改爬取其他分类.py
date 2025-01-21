#   1.  定位到2023必看片
#   2.  从2020必看片提取子页面的链接地址
#   3.  请求子页面的链接地址，拿到我们想要的链接地址


import re
import requests

domain = "https://www.dytt89.com/"
resp = requests.get(domain, verify=False)  # verify=False    去掉安全验证
resp.encoding = 'gb2312'  # 指定字符编码

n = "电影天堂.txt"

#   拿到ul里面的li
obj1 = re.compile(r"2023必看热片.*?<ul>(?P<THING>.*?)"
                  r"</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<HREF>.*?)'", re.S)

obj3 = re.compile(r'◎片　　名(?P<MOVIE>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<DOWNLORD>.*?)">', re.S)

rt1 = obj1.finditer(resp.text)
child_href_list = []

for i in rt1:
    ul = i.group('THING')

    #   提取子页面链接
    rt2 = obj2.finditer(ul)
    for o in rt2:
        href = o.group('HREF')

        #   拼接子页面的url地址，    域名+子页面地址
        child_href = domain + href.strip('/')
        child_href_list.append(child_href)  # 把子页面保存进字典

    #   提取子页面内容
    for href in child_href_list:
        cd_rt = requests.get(href, verify=False)
        cd_rt.encoding = 'gbk'

        rt3 = obj3.search(cd_rt.text)

        print(rt3.group('MOVIE'))
        print(rt3.group('DOWNLORD'))

        # break   #测试用
        all_ = rt3.group('MOVIE') + "----->" + rt3.group('DOWNLORD')
        with open(n, "a", encoding="gbk") as f:
            f.write(all_ + "\n")
f.close()
print("采集结束！！！")
