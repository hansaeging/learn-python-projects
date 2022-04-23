import  requests
from bs4 import BeautifulSoup
import pandas as pd  # pandas, openpyxl

def get_movie_review_naver(code, page):
    url = "https://movie.naver.com/movie/bi/mi/review.naver"
    params = { 'code':code, 'page':page}

    res = requests.get(url, params=params)

    # 파싱(parsing) - 구문분석
    soup = BeautifulSoup(res.text, 'lxml')

    # 리뷰가 담긴 영역 접근
    review_layer = soup.select_one('.rvw_list_area')
    reviews = review_layer.select('li')


    # 리스트 하나씩 출력하려면 보통 for문을 사용
    results = []
    for review in reviews :
        results.append([review.a.text])
    return results

def ger_movie_review_naver_pages(code, start, end):
    reviews = []
    for page in range(start, end+1) :
        data = get_movie_review_naver(code, page)
        reviews += data
    return reviews

def reviews_to_excel(reviews, title):
    data = reviews
    col = ['리뷰제목']
    data_frame = pd.DataFrame(data, columns=col)
    data_frame.to_excel(f'{title}.xlsx', sheet_name='샘플', startrow=0, header=True)  # index=False

reviews = ger_movie_review_naver_pages(44885, 10, 20)
reviews_to_excel(reviews, '아이언맨')
