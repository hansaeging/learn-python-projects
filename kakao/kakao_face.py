# kakao_face.py
import requests, config
from pprint import pprint

API_KEY = config.rest_api_key
host = "https://dapi.kakao.com"
path = "/v2/vision/face/detect"
headers = {
    "Authorization": f"KakaoAK {API_KEY}"
}

# POST -> form-data
filename = 'sample.jpg'
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