import  requests
from bs4 import BeautifulSoup

# 영화 리뷰 페이지
url = 'https://movie.naver.com/movie/bi/mi/review.naver?code=207921'

#웹 요청 -> HTML 코드를 가져오자!
res = requests.get(url)

# 파싱(parsing) - 구문분석
soup = BeautifulSoup(res.text, 'lxml')

# 리뷰가 담긴 영역 접근
review_layer = soup.select_one('.rvw_list_area')
reviews = review_layer.select('li')


# 리스트 하나씩 출력하려면 보통 for문을 사용
count = 1
for review in reviews :
    print(f"[{count}] {review.a.text}")
    count += 1