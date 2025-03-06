import requests


def fetch_data(key):
    """调用API并返回数据"""
    API_URL = "https://api.okcode.vip/api/dev/html_link"
    params = {"key": key}

    try:
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return f"请求失败，状态码：{response.status_code}"
    except requests.RequestException as e:
        return f"请求异常：{e}"
