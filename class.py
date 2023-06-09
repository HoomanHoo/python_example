#클래스
__a = 100 #일반변수
def get(): #일반함수
    return __a

class Test:
    __a = 200 #private 캡슐화
    b = 300
    def get(self):      #멤버함수
        return self.__a #self가 반드시 들어가야 한다
    def set(self, __a):
        self.__a = __a

print("__a: ", get())

test = Test()
print(test.b)
#print(test.__a) private라서 접근 못함
print(test._Test__a) #private에 접근하는 방법 제공 캡슐화가 의미가 없다

test.set(10)
print(test.get())

#생성자 / 소멸자
class User:
    def __init__(self, name="noname", age=0, tel=None): #생성자 - 클래스의 초기화를 담당함
        print("생성자")
        self.name = name
        self.age = age
        self.tel = tel

    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getTel(self):
        return self.tel
    def __del__(self): #메모리 정리
        print("소멸자")


kim = User('김유신', 30, '1111-2222')
print("이름: ", kim.getName())
print("나이: ", kim.getAge())
print("전화번호: ", kim.getTel())


lee = User("이순신", 50, "2222-3333")
print("이름: ", lee.getName())
print("나이: ", lee.getAge())
print("전화번호: ", lee.getTel())
print('------------------------------------------------')
#static
#모든 객체가 공유함
#static 영역에 할당되지 않음, 메모리가 하나만 할당되지 않으며 우선적으로 할당되지도 않는다
#인터프린터 언어라서 static을 명시할 필요가 없다
#사용할 때 static으로 사용한다

class Member:
    name = '홍길동' #스태틱 변수들 클래스 내부 - 멤버함수 외부에 작성한 변수들이 static 변수가 된다
    age = 20
    count = 0           #static으로 선언하면 모든 객체가 공유하게 됨
    cnt = 0
    def __init__(self, age = 0, cnt = 0):
        self.age = age
        self.cnt = cnt
        self.cnt += 1
        Member.count += 1

    def getCnt(self):
        return self.cnt

    def getCount(self):
        return self.count


print("이름: ", Member.count)
print(Member.age)

Member.name = "이순신"
lee = Member()
print("이름: ", lee.name)
print("이름: ", lee.getCnt())
print("이름: ", lee.getCount())

Member.name = "이순신"
lee = Member()
print("이름: ", lee.name)
print("이름: ", lee.getCnt())
print("이름: ", lee.getCount())

Member.name = "이순신"
lee = Member()
print("이름: ", lee.name)
print("이름: ", lee.getCnt())
print("이름: ", lee.getCount())
print('------------------------------------------------')

#static method = class method

class Car:
    cc = '2000cc'
    def get(self):    #일반 메서드
        return self.cc

    @staticmethod
    def getStatic():    #static 메서드 - self를 매개변수로 명시하지 않는다 전역에서 써야하기 때문에
        return Car()
    @classmethod
    def getClass(cls):  #클래스 메서드 - 매개변수로 클래스가 넘어옴 -> 클래스 객체를 반환함 - 다형성 구현
        return cls()    #넘겨받은 클래스로 인스턴스-객체를 생성해서 리턴함

class Truck(Car):   #Car Class를 상속받은 Truck Class
    cc = '3000cc'
car1 = Car()            #일반적인 인스턴스 생성 방법
print("cc: ", car1.get())
car2 = Car.getStatic()
print("cc: ", car2.get())   #static method 생성-사용 방법 Car instance 생성
car3 = Car.getClass()       #class method  - Car instance 생성
print("cc: ", car3.get())

truck1 = Truck()
print("cc: ", truck1.get()) #상속 받았을 땐 오버라이딩 한 요소에 우선권이 존재한다
truck2 = Truck.getStatic()
print("cc: ", truck2.get()) #Car Class 반환하라고 했기 때문에 Car Class가 생성됨
truck3 = Truck.getClass()
print("cc: ", truck3.get()) #class method - 명시하지 않아도 자동으로 클래스 이름을 넘겨받기 때문에 Truck 객체가 반환됨

#상속
class Animal:
    def __init__(self, name=""):    #생성자
        print("parent contructor")
        self.name = name  #non-static 멤버변수 생성 - 멤버변수로 명시 안해도 만들어짐

    def getName(self):
        return self.name

class Dog (Animal):
#    def __init__(self, name=""):
#        Animal.__init__(self, name)   #부모 생성자 호출 - 생략가능
#    None - Null 과 같은 의미
    pass

class Cat (Animal):
    def __init__(self, name=""):
        Animal.__init__(self, name)   #부모생성자 호출 - 생략가능
        print("child constructor")


cat = Cat("yaong-i")
print(cat.getName())
dog = Dog("mungmungi")
print(dog.getName())

#다중상속
class Gundam:
    def __init__(self, name=""):
        self.__name = name

    def getName(self):
        return self.__name

class Mercury:
    def __init__(self, mercury=""):
        self.mercury = mercury

    def getMercury(self):
        return self.mercury

class Witch(Gundam, Mercury):
    #def __init__(self, pilot):
    #    self.pilot = pilot
    def __init__ (self, name, mercury, pilot):
        Gundam.__init__(self, name)
        Mercury.__init__(self, mercury)
        self.pilot = pilot
    def getPilot(self):
        return self.pilot
class Darling(Gundam, Mercury):
   # pass
    def __init__ (self, name="", mercury=""):
        Gundam.__init__(self, name)
        Mercury.__init__(self, mercury)

sletta = Witch(name = 'sletta', mercury = 'spacian', pilot = 'pilot')
print(sletta.getName())
print(sletta.getMercury())
print(sletta.getPilot())

#darling = Darling() #Gundam, Mercury 생성자를 호출하나 아무것도 집어넣지 않아서 에러 발생(매개변수 기본값 주지 않은 경우)
#print(darling.getName())
#print(darling.getMercury())우자식 객체에 생성자 구현을 안 했을 경 두번째 상속받은 클래스는 인식을 못한다 - 매개변수를 주지 않았을 경우


darling = Darling()
print(darling.getName())
print(darling.getMercury())


#다형성 - Python에서 별로 의미는 없음
class Bread:
    def __init__(self, name=""):
        self.name = name

    def getName(self):
        return "Bread`s " + self.name

    @classmethod
    def getClass(cls, msg):
        return cls(msg)

class Toast(Bread):
    def getName(self):
        return "Toast`s " + self.name

class Cake(Bread):
    def getName(self):
        return "Cake`s " + self.name

class RedBean(Bread):
    def getName(self):
        return "RedBean`s " + self.name

toast = Toast("toast")
cake = Cake("cake")
redBean = RedBean("red bean")

print(toast.getName())
print(cake.getName())
print(redBean.getName())

toast2 = Toast.getClass('toast2')
cake2 = Cake.getClass('cake2')
redBean2 = RedBean.getClass('red bean2')

print(toast2.getName())
print(cake2.getName())
print(redBean2.getName())

bread = Bread()
toast3 = bread.getClass("toast3")
print(toast3.getName())

#@property

class Gamer:
    @property
    def setName(self, name=""):
        self.name = name
    @property
    def setAge(self, age=""):
        self.age = age
    @property
    def getName(self):
        return self.name
    @property
    def getAge(self):
        return self.age

gamer = Gamer()
#gamer.setName("홍길동") property로 등록하면 setMethod를 사용하면 안된다 - 에러 발생
#gamer.setAge(30)
gamer.name = "홍길동"  #property로 등록하면 변수명.변수 이름 으로 사용할 수 있다
gamer.age = 30
print(gamer.name)
print(gamer.age)


#추상메서드
from abc import abstractmethod, ABCMeta
class Food(metaclass=ABCMeta):  #추상클래스 - 규격-틀을 정하는 정도의 기능은 사용할 수 있다
    def __init__(self, name="", price=0):
        self.name = name
        self.price = price

    @abstractmethod
    def flavor(self):  #추상메서드 - 구현할 필요는 없다 - 구현은 가능
     #   print("flavor")
        pass

class Pizza(Food):
    def flavor(self):
        print("Pizza`s ", self.name, ":", self.price)

class Chicken(Food):
    def flavor(self):
        print("Chicken`s ",self.name, ":", self.price)

chicken = Chicken("노랑통닭", 20000)
chicken.flavor()

pizza = Pizza("도미노", 30000)
pizza.flavor()


#예외처리
import traceback
try:
    a = 4 / 'a'
except TypeError:
    print("숫자로만 나눌 수 있다")
else:
    print(a)
finally:
    print("프로그램 끝")
print("-------------------------------------------------------------")

import traceback
try:
    a = 4 / 0
except TypeError:       #실행할 때 나오는 에러만 잡으면 되기 때문에 안 쓰는 에러를 지정해놔도 에러가 안나온다
    print("숫자로만 나눌 수 있다")
except ZeroDivisionError:
    print("0으로 나눌 수 없다")
except Exception:
    traceback.print_exc()
else:
    print(a)
finally:
    print("프로그램 끝")

print("-------------------------------------------------------------")

try:
    a = 4 / 2
except TypeError:
    print("숫자로만 나눌 수 있다")
else:
    print(a)
finally:
    print("프로그램 끝")

print("-------------------------------------------------------------")
#사용자 정의 예외

class InputException(Exception):
    def __init__(self, msg):
        print(msg,  "는 사용할 수 없다")

class NumberException(Exception):
    def __init__(self, msg):
        print(msg, "는 숫자가 아니다")

try:

    msg = input("구구단: ")

    if not msg.isdigit():
        raise NumberException(msg)


    if eval(msg) < 2 or eval(msg) > 9:
        raise InputException(msg)


    for i in range(1, 10):
        print(msg, "*", i, "=", msg * i)

except InputException:
    print("2~9 사이로 입력해라")
except NumberException:
    print("숫자 입력해라")
else:
    pass
finally:
    print("프로그램 끝")


















