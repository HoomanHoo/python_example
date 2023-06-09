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







