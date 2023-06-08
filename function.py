#함수
#함수는 선언 구현 호출로 구성되어있다

def disp(): #선언
    print('hello python!!') #구현

disp() #호출
disp()
disp()

def max1(a, b):
    if a > b:
        print(a, ' is bigger then ', b)
    elif a < b:
        print( a, ' is smaller then ', b)
    else:
        print(a, ' is same ', b)

max1(5, 2)
max1(4, 7)
max1(5, 5)

def min1(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return 'same'

result = min1(5, 2)
print(result)

result = min1(5, 45)
print(result)

result = min1(5, 5)
print(result)

def calc(a, b):
    return a +b, a - b, a * b, a / b #튜플로 리턴하는 것이지 리턴값이 여러개인 것은 아니다

hap, cha, gop, mok = calc(10, 20)
print(hap, cha, gop, mok)

#오버로드
#매개변수의 자료형이 다르거나 갯수가 다르거나 순서가 다른 경우 다른 함수로 취급

"""
    C       int hapInt(int a, int b){return a + b}                  오버로드 불가능
            double hapDouble(double a, double b) {return a + b}
            
    C++     int hap(int a, int b){}                                 오버로드 가능
            double hap(double a, double b){}
            
    JAVA    public int hap(int a, int b){}                          오버로드 가능
            public double hap(double a, double b){}
            
    Python  오버로드 불가능 - 자료형 개념 자체가 없어서 오버로드의 의미가 없음 

    매개변수 갯수가 다른 경우
    
    C       int hap(int a = 0, int b = 0, int c = 0){}
            hap(5, 2)
            hap(5, 2, 7)        매개변수의 초깃값이라는 기능을 사용하여 매개변수의 갯수가 다른 경우에 대응할 수 있다
            
    C++     매개변수의 초깃값, 오버로드 둘 다 가능하다
    
    JAVA    오버로드만 가능하다 - 매개변수의 초깃값은 사용 불가
    
    Python  매개변수의 초깃값으로만 대응할 수 있다

"""

def hap(a, b = 0, c = 0):
    return a + b + c

print(hap(1,2))
print(hap(5))
print(hap(2, 4, 6))
#print(hap(2, 5, 6, 7))  에러남
#print(hap()) 에러남
"""
def cha(a, b= 0, c): #매개변수의 초깃값을 한 번 줬으면 뒤에 오는 매개변수들에도 초깃값을 줘야한다
    return a - b - c
"""
#Variable Argument 열거형을 매개변수로 받기 VarArgs 는 매개변수 중에서 가장 마지막에 와야한다 (가변이라 무한하게 받아줄 수 있기 때문)
def hap2 (*arg): #튜플을 매개변수로 받음 - arg = tuple
    sum = 1
    for a in arg:
        sum *= a
    return sum

print(hap2(2, 5))
print(hap2(2, 5, 6))
print(hap2(2, 5, 6, 7, 7))

#키워드 인수 - 매개변수에 넣을 데이터를 명시하는 기능
def mok(a, b = 1, c = 1):
    return a / b / c
print(mok(2, 5, 7))

print(mok(2))
print(mok(a = 2))
print(mok(c=2, b=3, a=40))
#print(mok(b = 10, c = 30))
#print(mok(b = 10, c = 20, 40))     둘 다 에러가 난다 키워드 인수 기능을 쓰면 해당 인수 이후의 인수들은 전부 키워드 인수로 등록해야한다




#키워드 인수 사전 - Dictionary 를 사용해서 키워드 인수를 함수에 대량으로 줄 수 있다

def display(a = 0, *args, **params): #args는 옵션, params는 데이터로 쓰임 항상 params가 맨 뒤에 와야한다
    print(a, end=" ")   #params는 dictionary형태의 데이터만 받을 수 있다
    for arg in args:    # args, params 둘 다 데이터를 안 넘기면 에러를 내지 않고 사용하지 않을 뿐이다
        print('args', arg, end=" ")
    for key, value in params.items():
        print('params', key, value, end=" ")
    print()

display(10, 20, 30, 40, 50)
display(10, b = 43, c = 312313)
display(10, 32434 ,34, 56, 24, 56834, 235633466,3527,4575,7,547,474,57,7,427,4,7547,457,457,  b = 43, c = 312313)
display('a', 'b', 'c' 'd', 'e', 543, 75312, value1=324, value2=342423)
#display(b=43, c=312, 10, 20, 30) SyntaxError: positional argument follows keyword argument
display()


l = [1, 2123, 23464, 5867, 10936, 342, 435]
print(l)
l.sort(reverse=True) #reverse 가 키워드 인수이다
print(l)
print('--------------------------------------------------------------------------------------------------')
#지역변수 / 전역변수
#영역 안에서 잡은 변수는 영역 안에서만 사용가능함 - 지역변수 / JAVA는 엄밀히 이야기하면 전역변수가 없음 - 클래스/영역 밖에서 코딩을 할 수 없기 때문이다
#Python은 영역 밖에서 코딩이 가능 - 전역변수가 존재함
vari = 10 #전역변수
print(vari, id(vari))

def show3():
    global b #global 키워드는 전역변수를 사용하겠다는 선언
    b = 1323
 #   vari = 1000
    print(vari, id(vari))
    print(b)
show3()
print(vari, id(vari))
print('--------------------------------------------------------------------------------------------------')

def show():
    global vari
    print(vari, id(vari))
    vari = 100 #지역변수
    print(vari, id(vari))
    print(b)
show()
print(vari, id(vari))
print('--------------------------------------------------------------------------------------------------')

def show2():
    print(vari, id(vari))
show2()
print(vari, id(vari))
print('--------------------------------------------------------------------------------------------------')

#내장함수
print(abs(-3))
print(all([1,2, 4])) #all()은 매개변수로 넣은 리스트의 요소 전부가 참인지를 물음 (0이 아닌지)
print(all([0, 1])) #0이 포함되어있으면 False를 리턴
print(any([0, 1])) #any()는 매개변수로 넣은 리스트의 요소 중 하나라도 참인지를 물음 (0이 아닌지)
print(any(["", 0, False])) #아무것도 없는 문자열(스페이스도 없어야함), 0, False는 False로 취급한다

import sys
print(dir())
print(dir(sys)) #사용 가능한 변수, 함수, 클래스를 출력해준다
a = 10
print(dir()) # a가 추가됨
print(help(sys)) #도움말

print(divmod(7, 3))
print('1 + 3')
print(eval('1 + 3'))
print(max("hello pythoN"))
print(pow(5, 2)) #제곱을 구해줌

#Sort
m = [20, 50, 30, 10, 7534, 2059]
print(m)
m.sort() #List가 가진 sort함수
print(m)
m.sort(reverse=True)
print(m)

m = sorted(m) #return값이 존재한다
print(m)
m = sorted(m)[::-1] #역순으로 정렬하기 위해 인덱싱을 해줘야 한다
print(m)

c = [1, 2, 3]
d = [7, 6, 9]
print(list(zip(c, d))) #zip만 해서는 값을 추출할 수 없기 때문에 list() 를 통해 리스트로 형변환 하고 사용한다 - 같은 인덱스끼리 모아 튜플로 만들어서 압축함
print('--------------------------------------------------------------------------------------------------')

#람다함수 - 익명함수
def add(a, b):
    return a + b

print(add(4, 6))다

add2 = lambda a, b : a + b #매개변수로 주거나 일회용으로 사용하기 때문에 이름을 잘 붙이지 않음
print(add2(4, 7))
print((lambda a, b : a * b)(4, 10)) #(lambda함수)(매개변수들) 의 형태로 자주 사용한다

