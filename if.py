##제어문
#조건문
#a = eval(input("정수: "))
#b = eval(input("정수: "))
#print(a +b)

a = 10
if a > 10:
    pass #pass는 아무것도 하지 않겠다는 예약어이다

if a > 10:
    print('big')
else:
    print('small')

if a < 20:
    print('young')
elif a < 40:
    print('adult')
elif a < 60:
    print('old adult')
else:
    print('older')


#반복문
for i in range(10):
    print(i, end='\t')
print()

for i in range(0, 10, 2):
    print(i, end='\t')
print()

for i in range(10, 0, -1):
    print(i, end='\t')
print()
#나열형
s = 'ABCDEF'
for a in s:
    print(a, end='\t')
print()
t = 10, 20, 30, 40, 50
for a in t:
    print(a, end='\t')
print()

l = [1, 2 ,3, 4, 5]
for a in l:
    print(a, end='\t')
print()

s = {12, 34, 45, 56, 67, 78, 89}
for a in s:
    print(a, end='\t')
print()

d = {'a':34, 'b':21, 'c':76, 'd':544}
for a, b in d.items():
    print(a, b, end='\t')
print()

m = [(1, 2), (56, 83), (332, 6753)] #dictionary의 items() 형태가 m과 같다 - 변수를 하나만 주면 튜플을 출력하게된다
for a in m:
    print(a)

#리스트 축약
w = [i for i in range(1, 101)] #리스트 안에서 for문을 돌려서 자동으로 리스트를 만들 수 있다
print(w)

w = [i**2 for i in range(1, 101)] #간단한 연산도 가능하다
print(w)

scores = {'kim':89, 'lee':75, 'jung':65, 'park':90, 'hong':85, 'choi':88,
          'sung':55, 'cho':44, 'hwang':105}

for name, score in scores.items():
    if 70 <= score <= 100:
        print(name +'님은 합격입니다')
    elif score < 70 and score >= 0:
        print(name + '님은 불합격입니다')
    else:
        print('잘못 입력하셨습니다')
i = 0
while(i < 10):
    i += 1
    print(i, end='\t')
print()

i = 0
while True:
    i += 1

    if i % 2 == 1:
        continue

    if i == 50:
        break

    print(i, end='\t')

print()

users = {'kim':'yousin', 'lee':'sunsin', 'hong':'gildong', 'kang':'gamchan'}
for key, value in users.items():
    print(key, value, end='\t')
print()

for i, value in enumerate(users):
    print(i, value, users.get(value), end='\t')
print()

for i, value in enumerate(users, 100): #enumerate()는 시작 인덱스를 사용자가 지정할 수 있다
    print(i, value, users.get(value), end='\t')
print()

