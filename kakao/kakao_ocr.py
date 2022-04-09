# kakao_ocr.py
import requests
from pprint import pprint
import config

API_KEY = config.rest_api_key
host = "https://dapi.kakao.com"
path = "/v2/vision/text/ocr"
headers = {
    "Authorization": f"KakaoAK {API_KEY}"
}

# POST -> form-data
filename = 'vision_ocr.png'
files ={
    'image' : open(filename, 'rb')
}

# POST로 통신 요청
res = requests.post(host+path, headers=headers, files=files)
print(res)

# 200이면 성공
if res.status_code == 200:
    data = res.json()
    pprint(data)