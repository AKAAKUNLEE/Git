import requests
from bs4 import BeautifulSoup
import ffmpy3
import re
import csv
from PIL import Image, ImageFilter

html = input("请输入要爬取的视频链接：")  # 当前页面的网址
data = {"buid": "vinfoad",
        "vinfoparam": "charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fjo9b2oxhk5f3jlx%2Fv0020cq94ic.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fjo9b2oxhk5f3jlx%2Fv0020cq94ic.html&sphttps=1&encryptVer=9.2&cKey=oVcfnAV1NwO1281Orq2-LnCjnpb8Ocr0cPTc-pZczEul_f4uOWcpWmJMR8Gu77I-PQBCj0BWxWraCp7VHCeQghpmp7rG5tiHjLv_PnnatnPaZfSCyImD_JfQk7s9pI6ZkV33_IMI4ZInFjOj-NmZhE-NjjawCzIdF66cdsFdzz5jk70UOmynTHDptaxqIemxrSlkg-M_BbDaBoWwiX7uSsBkDK_qlv9BvC71Ch6ixh2gniDG5LKtpya6ny_WlRnPhtW2R-Cqz5Y8tGTr2rFp56lxzzDtPFKhwYCtsQcaQ5txIefj4bzaway4kar5rswVM4Yi2vMx4JDVSaSl29Zyy7900ICoeOJZY6b_P75Em4nh9wpcKyMc2-ZSG3YOk0hnCuc2Zr8bNdIi0MIn9qwngv68dNaB6oi96ASJy5AjxN0GmZunIA2U2-O4sSS-7vVWSPDZ13OYcM4AEVwxpm3Jz0VO8Pm591tDGo2_EoqrNITcAeS2xZq-C8tmCTHWG3QVXUHzMj7X8tg4kiBSoFT2OuwjL5u6BCcuA7kS34srgXittOQs-WWKqfme7gUFBQUFK8DX1w&clip=4&guid=e253f7e296790e16&flowid=50ef28f0c70a901c509f090cc8b24253&platform=10201&sdtfrom=v1010&appVer=1.28.2&unid=&auth_from=&auth_ext=&vid=v0020cq94ic&defn=&fhdswitch=0&dtype=3&spsrt=2&tm=1698323342&lang_code=0&logintoken=&spvvpay=1&spadseg=3&spav1=15&hevclv=28&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&drm=40",
        "sspAdParam": "{\"ad_scene\":1,\"pre_ad_params\":{\"ad_scene\":1,\"user_type\":-1,\"video\":{\"base\":{\"vid\":\"v0020cq94ic\",\"cid\":\"jo9b2oxhk5f3jlx\"},\"is_live\":false,\"type_id\":0,\"referer\":\"https://v.qq.com/x/search/?q=%E4%B9%90%E9%AB%98%E5%B9%BB%E5%BD%B1%E5%BF%8D%E8%80%85\",\"url\":\"https://v.qq.com/x/cover/jo9b2oxhk5f3jlx/v0020cq94ic.html\",\"flow_id\":\"50ef28f0c70a901c509f090cc8b24253\",\"refresh_id\":\"\",\"fmt\":\"shd\"},\"platform\":{\"guid\":\"e253f7e296790e16\",\"channel_id\":0,\"site\":\"web\",\"platform\":\"in\",\"from\":0,\"device\":\"pc\",\"play_platform\":10201,\"pv_tag\":\"|video:series_poster_v_pic\",\"support_click_scan_integration\":true},\"player\":{\"version\":\"1.28.1\",\"plugin\":\"3.4.18\",\"switch\":1,\"play_type\":\"0\"},\"token\":{\"type\":0,\"vuid\":0,\"vuser_session\":\"\",\"app_id\":\"\",\"open_id\":\"\",\"access_token\":\"\"}}}",
        "adparam": "adType=preAd&vid=v0020cq94ic&sspKey=dsao"}
headers = {
    'Cookie': '_clck=1hsy5zv|1|ffn|0; qq_domain_video_guid_verify=e253f7e296790e16; pgv_info=ssid=s4724927324; pgv_pvid=4637341236; o_minduid=n-lb8yGLlHb87GNFuDpL5C4x6BSayIFx; appuser=432DB1D2C56BA5A6; vversion_name=8.2.95; video_omgid=e253f7e296790e16; Lturn=454; LVINturn=625; LPHLSturn=828; LDERturn=474; LZTturn=387',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
# json=data 是post请求
# params=data 是get请求
r = requests.post(url=html, json=data, headers=headers).json()
m3u8_url = re.findall('url":"(.*?)"', r['vinfo'])
m3u8_text = requests.get(m3u8_url).text
m3u8_text_re = re.sub('#E.*', '', m3u8_text).split()
print(r)
