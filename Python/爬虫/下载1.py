import requests
from bs4 import BeautifulSoup
import ffmpy3
import re
import csv
from PIL import Image, ImageFilter
video_content = requests.get(url="https://sns-webpic-qc.xhscdn.com/202310292335/b4a3a044f46d5821ba1bdc72a9a7e8f0/1000g0082hmni6naiu0305oivobtoc30fmi1jl70!nd_whgt34_webp_wm_1").content
with open("1.jpg", mode='wb') as f:
    f.write(video_content)

