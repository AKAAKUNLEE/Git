import requests
import re
import json
import base64

headers = {
    'Cookie': '_clck=1hsy5zv|1|ffn|0; qq_domain_video_guid_verify=e253f7e296790e16; pgv_pvid=4637341236; RK=XS15IR+NEt; ptcz=fe12046da6198b86a4d0a8d307f3655d2326cf59e382abb80ac1a54d48695d32; ETCI=851c38666cfb4ed8b8efa0f29a822436; fqm_pvqid=5681aee3-94fe-4f83-ad29-d0a85001513f; _qimei_q36=; _qimei_h38=2db829fcf45c42a4caf42bbb02000003817a1a; _qimei_fingerprint=de7304ce0faeff99f8f9ce2e4d341c80; _qimei_uuid42=181060f3730100c2aff038daa3bbf01d5a2c2a4f44; nav_userinfo_cookie=; ac_wx_user=; theme=dark; roastState=2; __BEACON_deviceId=rxGMN925fjKWDxHD3M5adaT1Z3WT42Sx; Hm_lvt_f179d8d1a7d9619f10734edb75d482c4=1707919126; Hm_lpvt_f179d8d1a7d9619f10734edb75d482c4=1707919126',
    'Referer': 'https://ac.qq.com/Comic/searchList?search=%E4%B8%87%E4%BA%8B%E4%B8%87%E7%81%B5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
# url = input('输入要爬取的漫画链接(仅限腾讯动漫):')
url = 'https://ac.qq.com/ComicView/index/id/631399/cid/2'
res = requests.get(url=url, headers=headers)
# print(res.text)
b4_str = re.findall("var DATA = '(.*?)'", res.text)[0]
print(b4_str)
# bs64 = base64.b64decode(b4_str)
# print(bs64)
for i in range(len(b4_str)):
    try:
        json_str = base64.b64decode((b4_str[i:]).encode('utf-8')).decode()
        # print(json_str)
        pictures = re.findall('"picture":(\[.*?\])', json_str)[0]
        json_list = json.loads(pictures)
        print(json_list)
        break
    except:
        pass
