from shlex import join
import tkinter as tk
import parsel
import requests
import re
import json
import base64
import os
import shutil

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('url快速转换快捷方式')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('400x300')  # 这里的乘是小x

# 第4步，用户信息
tk.Label(window, text='文件类型:', font=('华文新魏', 14)).place(x=10, y=170)
tk.Label(window, text='图标地址:', font=('华文新魏', 14)).place(x=10, y=210)
tk.Label(window, text='网络地址:', font=('华文新魏', 14)).place(x=10, y=250)


# 第5步，用户登录输入框entry
# 文件类型
var_file_type = tk.StringVar()
var_file_type.set('吾爱破解')
entry_file_type = tk.Entry(window, textvariable=var_file_type, font=('华文新魏', 14))
entry_file_type.place(x=120, y=170)
# 图标地址
var_icon_address = tk.StringVar()
entry_icon_address = tk.Entry(window, textvariable=var_icon_address, font=('华文新魏', 14))
entry_icon_address.place(x=120, y=210)
# 网络地址
var_network_address = tk.StringVar()
entry_network_address = tk.Entry(window, textvariable=var_network_address, font=('华文新魏', 14))
entry_network_address.place(x=120, y=250)



'''headers = {
    'Cookie': '_clck=1hsy5zv|1|ffn|0; qq_domain_video_guid_verify=e253f7e296790e16; pgv_pvid=4637341236; RK=XS15IR+NEt; ptcz=fe12046da6198b86a4d0a8d307f3655d2326cf59e382abb80ac1a54d48695d32; ETCI=851c38666cfb4ed8b8efa0f29a822436; fqm_pvqid=5681aee3-94fe-4f83-ad29-d0a85001513f; _qimei_q36=; _qimei_h38=2db829fcf45c42a4caf42bbb02000003817a1a; _qimei_fingerprint=de7304ce0faeff99f8f9ce2e4d341c80; _qimei_uuid42=181060f3730100c2aff038daa3bbf01d5a2c2a4f44; nav_userinfo_cookie=; ac_wx_user=; theme=dark; roastState=2; __BEACON_deviceId=rxGMN925fjKWDxHD3M5adaT1Z3WT42Sx; Hm_lvt_f179d8d1a7d9619f10734edb75d482c4=1707919126; Hm_lpvt_f179d8d1a7d9619f10734edb75d482c4=1707919126',
    'Referer': 'https://ac.qq.com/Comic/searchList?search=%E4%B8%87%E4%BA%8B%E4%B8%87%E7%81%B5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
url = input('输入要转换的链接:')
res = requests.get(url=url, headers=headers).text
print(res)
# 编码  utf-8编码格式 gbk编码格式
selector = parsel.Selector(res)
title_str = selector.xpath('/html/head/title/text()').getall()
ti_str = "".join(title_str)
ti_str = re.sub('[\\/:*?"<>|]', '_', ti_str)
print(ti_str)
write1 = '[{000214A0-0000-0000-C000-000000000046}]\n'
write3 = '[InternetShortcut]\n'
write2 = 'Prop3=19,11\n'
write4 = 'URL=' + url
write = write1 + write2 + write3 + write4
# print(write)
filename = ti_str + '.url'
with open(filename, "w") as file:
    file.write(write)
shutil.move(filename, 'D:\\Dawn Launcher\\URL')

# with open("str(ti_str).url", "w") as file:
# file.write(write)
# fold_dir = 'D:\\Git\\Python\\url快速转换快捷方式'  # 需要修改的文件所在的文件夹
# filename = os.listdir(fold_dir)  # 该文件夹中文件的名称
# print(filename)  # 在控制台输出原文件名称

# for number, temp in enumerate(filename):  # 编号，和得到各文件名
# new_filename = '/苍老师小电影001' + str(number + 1) + '.mp4'  # 新文件名（注意跟上文件后缀名）
# os.rename(fold_dir + '/' + temp, fold_dir + new_filename)  # 文件重命名后替换原文件名
# print(new_filename)  # 在控制台输出替换后的文件名称
'''
window.mainloop()

