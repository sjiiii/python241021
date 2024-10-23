#web1.py

#웹크롤링에 관련된 선언
from bs4 import BeautifulSoup

#웹페이지를 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()

#html 파서 : "상수값을 지정"
soup = BeautifulSoup(page, "html.parser")

#원하는 데이터 추출
#print(soup.prettify())

#<p> 태그 전체를 검색
#print(soup.find_all("p"))
#첫번째 <p> 태그 검색
#print(soup.find("p"))

#<p> 태그 중에서 class 속성이 outer-text인 것만 검색
#print(soup.find_all("p", class_="outer-text"))

#attrs 속성 검색 : attributes 속성
#print(soup.find_all("p", attrs={"class":"outer-text"}))

#태그 내부의 문자열 출력 : .text속성
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)

#id로 검색
print(soup.find_all(id="first"))



