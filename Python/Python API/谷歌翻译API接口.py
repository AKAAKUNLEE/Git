import requests


def translate_text(text):
    url = f"https://findmyip.net/api/translate.php?text={text}"
    response = requests.get(url)
    data = response.json()
    return data["data"]["translate_result"]


text = "Iloveyoumybaby."
translation = translate_text(text)
print(translation)
