#모듈


# import simple.mymodule
# print(simple.mymodule.name) #package_name.mudule_name.element 로 명시해야한다
# print(simple.mymodule.age)
# print(simple.mymodule.__version__)
#
# import simple.mymodule as mm    #module import 하면서 alias를 줄 수 있다
# print(mm.name)
# print(mm.age)
# print(mm.__version__)
#
# from simple import mymodule as mModule     #from package_name import module_name 으로도 쓸 수 있다
# print(mModule.name)
# print(mModule.age)
# print(mModule.__version__)
#
# from simple.mymodule import hello, bye, User    #from package_name.module_name import elemet 의 구조로도 쓸 수 있다
# hello()
# bye()
# user = User(name="커피")
# print(user.getName())
# user2 = User('우유', 50)
# print(user2.getName())
# print(user2.getAge())
#
# print("-----------------------------------------------")
# from simple.mymodule import hello, bye, User as u    #from package_name.module_name import elemet 의 구조로도 쓸 수 있다
# hello()
# bye()
# user = u(name="커피")
# print(user.getName())
# user2 = u('우유', 50)
# print(user2.getName())
# print(user2.getAge())

#자주 사용하는 모듈들
print("-----------------------------------------------")
#OS Module - 간단한 정보를 얻어옴
import os
#print(os.getcwd())

path = "/home/hooman"
#print(os.listdir(path))

for file in os.listdir(path):
    if os.path.isdir(path + "/" + file):
        print(file, "is directory")
    elif os.path.isfile(path + "/" + file):
        print(file, "is file", "and size is", "(", os.path.getsize(path + "/" + file), ")")
    else:
        print('what is this?')
print(os.path.abspath(".")) #현재 작업 폴더의 절대경로를 반환해줌
print(os.path.exists("./abc"))
print("-----------------------------------------------")

for file in os.listdir(os.getcwd()):
    print(file)
print("-----------------------------------------------")
#sys module
import sys
print(sys.path)
#print(sys.modules)
for key, value in sys.modules.items():
    print(key, ":", value)
print("-----------------------------------------------")

print(sys.version_info)
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())
print("-----------------------------------------------")

#Logging Module
#Logging Level  -   사용자가 설정을 할 수 있다 / 설정한 레벨 이상의 요소들을 전부 볼 수 있다
# CRITICAL    50
# ERROR       40
# WARNING     30
# INFO        20
# DEBUG       10
# NOTSET      0

import platform, logging
print(platform.platform())

if platform.platform().startswith("Windows"):
    logFilePath = os.path.join(os.getenv("HOMEDRIVE"), os.getenv("HOMEPATH"), 'test.log')
else:
    logFilePath = os.path.join(os.getenv("HOME"), "test.log")

print(logFilePath)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s : %(levelname)s : %(message)s",
    filename=logFilePath
    )

logging.critical("Start Program")
logging.error("Doing")
logging.warning("Warning")
logging.info("info")
logging.debug("debug")
print("-----------------------------------------------")
#datetime module
from datetime import date, time, datetime, timedelta

now = date.today()
print(now)
print(now.year, "년", now.month, "월", now.day, "일")
now = datetime.today()
print(now)
print(now.year, "년", now.month, "월", now.day, "일",
      now.hour, "시", now.minute, "분", now.second, "초")

print(now + timedelta(30)) #일 단위로 변경됨
print(now.strftime("%Y-%m-%d %H:%M:%S")) # 날짜 -> 문자열
s = '2023-12-02 15:30:54'
print(datetime.strptime(s, "%Y-%m-%d %H:%M:%S"))
print("-----------------------------------------------")
print("-----------------------------------------------")
#datetime module
from datetime import date, time, datetime, timedelta

now = date.today()
print(now)
print(now.year, "년", now.month, "월", now.day, "일")
now = datetime.today()
print(now)
print(now.year, "년", now.month, "월", now.day, "일",
      now.hour, "시", now.minute, "분", now.second, "초")

print(now + timedelta(30)) #일 단위로 변경됨
print(now.strftime("%Y-%m-%d %H:%M:%S")) # 날짜 -> 문자열
s = '2023-12-02 15:30:54'
print(datetime.strptime(s, "%Y-%m-%d %H:%M:%S"))
print("-----------------------------------------------")
#random module
import random
#random.seed(10) #seed 고정 안 시키면 출력되는 데이터가 프로그램 실행시 마다 달라진다
print(random.random())
for j in range(10):
    # for i in range(6):
    #     #print(int(random.random() * 45) + 1, end='\t')
    #     print(random.randint(1, 46), end='\t')
    lotto = random.sample(range(1, 46), 6) #중복요소 없이 랜덤값 출력하기
   # lotto.sort()
    lotto = sorted(lotto)
    print(lotto)
    if j == 4:
        print()
    print()
#FILE module
# f = open('a.txt', 'r')
# w = open("a1.txt", 'w')
# while True:
#     # data = f.read()
#     # if(data == ""):
#     #     break
#     # print(data, end='\t')
#     line = f.readline()
#     if not line:
#         break
#     print(line)
#     w.write(line)       #파일이 생성되고 데이터가 입력이됨
# print()
# f.close()
# w.close()

with open('a.txt', 'r', encoding='utf-8') as f2 : #close()를 해줄 필요가 없다
    w2 = open('a1.txt', 'w')
    # while True:
    #     line = f2.readline()
    #     if not line:
    #         break
    #     print(line)
    for line in f2: # == f2.readline()
        print(line)
        w2.write(line)
    print()
    w2.close()

with open('a.txt', 'r', encoding='utf-8') as f3 :
    lines = f3.readlines()
    print(lines)


#CSV 파일 입출력 - , 를 이용하여 강제로 입출력 - panadas 에서 with csv 사용함
#Pickle - 객체단위(row)로 데이터 입출력을 함

class User:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

import pickle
hong = User(name="홍길동", age=30)
with open("b.txt", "wb") as f7: #as 뒤의 이름은 마음대로 지정(변수임)
    pickle.dump(hong, f7)
    print("출력성공")

with open("b.txt", "rb") as file: #읽기 쓰기 모드 설정의 -b는 바이너리 형태로 저장하고 불러오겠다는 의미이다
    user = pickle.load(file)      # -b는 바이너리, -t는 텍스트 형태
print(user.getName())
print(user.getAge())
print('-------------------------------------------------')

users = [
    User("김유신", 20),
    User("대조영", 50),
    User("이순신", 42)
]
with open("c.txt", "wb") as pickling:
    pickle.dump(users, pickling)
    print("쓰기 성공")

with open("c.txt", "rb") as pickling2:

    for name in pickle.load(pickling2):
        print(name.getName())
        print(name.getAge())

print('--------------------------------------')
#정규식 모듈
import re
p = re.compile("[a-z]+")
print(p.match(""))
print(p.match(" "))
print(p.match("abckd"))
print(p.match("dsfVfwf"))
s = p.match("abckd")
s2 = (p.match("dsfVfwf"))
print(s.span()) #매칭되는 위치 인덱스를 표시해줌
print(s.group())    #매칭되는 문자열을 반환해줌
print(s2.span())
print(s2.group())
print(p.match("python"))
print(p.match("Python")) #맨 처음부터 매칭되는 글자를 찾기 때문에 맨 처음에 정규식에 어긋나는 글자가 있으면 None을 반환함
print(p.match("pythOn"))
print(p.match(" python")) #띄어쓰기 역시 문자로 인식한다 - 정규식은 소문자 a~z까지만 찾기 때문에 None 반환
print('====================================================================================')
print(p.search("abdgas"))   #search 함수는 중간에서도 문자를 찾는다
print(p.search("Python"))
print(p.search(" python"))
result = p.search("pythOn")
print(result.span())
print(result.group())
print(result.start())
print(result.end())
print('====================================================================================')
s = "Life is too short"
print(p.match(s))
print(p.search(s))
print(p.findall(s))
print("--------")
result = p.findall(s)
#print(p.finditer(s)) iterator로 반환함

for w in result:
    print(w)
print("--------")
ite = p.finditer(s)
for w in ite:
    print(w)
print("--------")
for w in ite:
    print(w.group())
print("--------")
p = re.compile("a.b")
print(p.search("abc"))
print(p.search("a342224234dsfsfsfsdfsfdvfdfdvdfvdfd_)*)(*)&*(^*bc"))
print(p.search("a342224234dsfsfsfsdfsbc"))
print(p.search("a3bc"))
print(p.search("erdfa3bcwqeqw"))
print(p.search("erdfa&bcwqeqw"))
print(p.search("erdfa bcwqeqw"))
print(p.search("erdfa@bcwqeqw"))
print(p.search("erdfa\tbcwqeqw"))
print(p.search("erdfa\nbcwqeqw")) #\n은 인식을 못함
print("--------")
s = "abc abd aab aaab a\tb a\nb a#b"
print(p.findall(s))
p = re.compile("a.b", re.DOTALL)    #\n도 문자로 인식한다
print(p.findall(s))
print("--------")
p = re.compile("^python\s\w+", re.M)    #옵션 두개 이상 주고 싶을때는 or 연산자를 사용한다
s = """
python one
pythontwo
python as
python
you need python
life is too short
python$$$

"""
print(p.findall(s))
#이메일 유효성 검사
print("=======================================================")
emails = """
aaa@aaa.com
aaa@a.com
AAA@AAA.com
1AA@aaa.com
&&&@&&&.com
aaa@aa@.com
aaa@@aaa.com
asdsdfdksjfldskahfsiheufslkuifneuinjfdksbjkldhbd@aaa.com
aa1@aaa.com
aaa@aaa.7com
aaa@aaa.co.kr
aaasdsa dff@aaa.com
aaa@ fsd.com
"""
p = re.compile("^[a-z][a-z0-9]{2,17}@[a-z0-9]{2,}\.[a-z]{2,}$", re.M)
print(p.findall(emails))

p = re.compile("^[a-z][a-z0-9]{2,15}@[a-z0-9]{2,}\.[a-z0-9]{2,15}\.[a-z]{2,}$", re.M)
print(p.findall(emails))















