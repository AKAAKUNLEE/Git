import requests

url = "http://ovoa.cc/api/QQmusic.php"
# msg = input("请输入(音乐昵称)：")
params = {
    "msg": "永彬",
    "n": "1",
    "type": "json"
}
response = requests.get(url, params=params)
data = response.json()

songname = data["data"]["songname"]
name = data["data"]["name"]
cover = data["data"]["cover"]
songurl = data["data"]["songurl"]
src = data["data"]["src"]

print(songname)
print(name)
print(cover)
print(songurl)
print(src)
'''+ "n=1" + "&" '''
