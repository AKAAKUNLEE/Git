#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：url快速转换快捷方式.py 
@File    ：colamanga_spider.py
@IDE     ：PyCharm 
@Author  ：AKUNLEE
@Date    ：2024/9/21 12:31 
"""
import requests
import re
import json
import base64
from bs4 import BeautifulSoup
import os
import time
import urllib.request
import random
from urllib.parse import quote
from urllib.request import urlretrieve
import tkinter as tk


headers = {
    'Cookie': '_clck=1hsy5zv|1|ffn|0; qq_domain_video_guid_verify=e253f7e296790e16; pgv_pvid=4637341236; RK=XS15IR+NEt; ptcz=fe12046da6198b86a4d0a8d307f3655d2326cf59e382abb80ac1a54d48695d32; ETCI=851c38666cfb4ed8b8efa0f29a822436; fqm_pvqid=5681aee3-94fe-4f83-ad29-d0a85001513f; _qimei_q36=; _qimei_h38=2db829fcf45c42a4caf42bbb02000003817a1a; _qimei_fingerprint=de7304ce0faeff99f8f9ce2e4d341c80; _qimei_uuid42=181060f3730100c2aff038daa3bbf01d5a2c2a4f44; nav_userinfo_cookie=; ac_wx_user=; theme=dark; roastState=2; __BEACON_deviceId=rxGMN925fjKWDxHD3M5adaT1Z3WT42Sx; Hm_lvt_f179d8d1a7d9619f10734edb75d482c4=1707919126; Hm_lpvt_f179d8d1a7d9619f10734edb75d482c4=1707919126',
    'Referer': 'https://ac.qq.com/Comic/searchList?search=%E4%B8%87%E4%BA%8B%E4%B8%87%E7%81%B5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

Search0 = 'https://www.colamanga.com/search?type=2&searchString='
Search1 = input("请输入要搜索的漫画名:")
Search = Search0 + Search1
index = 'https://www.colamanga.com/'
res = requests.get(url=Search, headers=headers).text
