#이미지 긁어오기
import time
import urllib.request
# url = "https://imgnews.pstatic.net/image/445/2023/06/12/0000119719_001_20230612113601586.jpeg?type=w647"    #이미지 경로
# savename = "쪽후.jpeg"    #이미지 저장할 이름
# urllib.request.urlretrieve(url, savename)   #이미지 저장, 실행중인 경로로 다운로드됨
# print("save")   #확인용

#텍스트 긁어오기
# url2 = "https://www.google.com/robots.txt"
# robots = urllib.request.urlopen(url2)
# data = robots.read()
# data2 = data.decode("utf-8")    #한글이 넘어올 시를 대비하여 인코딩을 설정해준다
# print(data2)

#매개변수를 주고 크롤링 요청하기
import urllib.parse
#url3 = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
url3 = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId' : 109
}
params = urllib.parse.urlencode(values)
ur3 = url3 + "?" + params
data = urllib.request.urlopen(url3).read().decode("utf-8")
#print(data)

from bs4 import BeautifulSoup as bs
html = """
    <html>
        <head>
            <title>BeautifulSoup</title>
            <meta charset="utf-8">
        </head>
        <body>
            <h2>BeautifulSoup</h2>
            <p id="first" class="strong"> zzazangmyoun </p>
            <p class="strong">zzambbong</p>
            <p class="point"> tangsuyuk </p>
            <p id="second"> ulmyon </p>
        </body>
    </html>
"""
soup = bs(html, 'html.parser')
print("<<", soup.html.body.h2.string, ">>")

#find(), find_all()
h2 = soup.find("h2")
print("<<", h2.string, ">>")
p1 = h2.next_sibling.next_sibling
print(p1.string, " =p1")
p2 = p1.next_sibling.next_sibling
print(p2.string)

body = h2.parent
print(body)
nodes = body.children
for node in nodes:
    print(node.string.strip())  #여백도 같이 찍히는데 여백 역시 자식노드기 때문에 지울 수 없

ps = soup.find_all("p")
for p in ps:
    print(p.string.strip()) #strip()은 앞뒤 여백을 지우는 함수다 = JAVA의 trim

#findChild()
h2_1 = body.findChild()    #DOM에서는 firstChild
print(h2_1.string)

p1 = soup.find(id="first")
print(p1.string)

p2 = soup.find(class_="point")
print(p2.string)

p3 = soup.find(id="first", class_="strong")
print(p3.string)

#select_one(), select() - id, class 선택해서 가져올 때 더 많이 사용함
print("########################################################################################")
header = soup.select_one("body h2") #CSS 선택자 형식으로 사용함
print('body h2:', header.string)
cls = soup.select_one("#second")
print("#second:", cls.string)

strong = soup.select(".strong")
for s in strong:
    print(".strong:", s.string)

p4 = soup.select_one("p#first")
print("p#first:",p4.string)

#url3 = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
url3 = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId' : 109
}
params = urllib.parse.urlencode(values)
url3 = url3 + "?" + params
data = urllib.request.urlopen(url3).read().decode("utf-8")
soup = bs(data, "html.parser")  #xml도 html parser 사용함
cities = soup.find_all("city")
for city in cities:
    print(city.string)

datas = soup.find_all("data")
for data in datas:
    city = data.parent.find("city")
    tmef = data.find("tmef")
    wf = data.find("wf")
    print(city.string, ":", tmef.string, ":", wf.string, end="\t")
print()

#네이버 환율정보 출력
url4 = "https://finance.naver.com/marketindex/exchangeList.naver"
data = urllib.request.urlopen(url4).read().decode ("euc-kr")
urllib.request.urlretrieve(url4, "exchange.txt")
soup = bs(data, "html.parser")
exchanges = soup.select("td.tit a")
sales = soup.select("td.sale")

for i in range(len(exchanges)):
    sale2 = sales[i].next_sibling.next_sibling
    sale3 = sale2.next_sibling.next_sibling
    sale4 = sale3.next_sibling.next_sibling
    print(exchanges[i].string.strip(), ":", sales[i].string.strip(), end="\t")
    print(sales[i].next_sibling.next_sibling.string.strip(), end="\t")
    print(sale2.next_sibling.next_sibling.string.strip(), end="\t")
    print(sale3.next_sibling.next_sibling.string.strip(), end="\t")
    print(sale4.next_sibling.next_sibling.string.strip(), end="\t")
    print()

#다음 실시간 뉴스
url = "https://news.daum.net/"
data = urllib.request.urlopen(url).read().decode("utf-8")
urllib.request.urlretrieve(url, 'news.txt')
soup = bs(data, "html.parser")
titles = soup.select("strong.tit_g a.link_txt")
for i, title in enumerate(titles):
    if i > 4:   #기사를 한 번에 5개씩만 출력
        break
    print(title.string.strip())
    article_url = title["href"]
 #   print(article_url)
    article_data = urllib.request.urlopen(article_url).read().decode("utf-8")
    article_soup = bs(article_data, "html.parser")
    article_resources = article_soup.select("p")
    for article_resource in  article_resources:
        print(article_resource.string)
    time.sleep(1)   #초 단위임