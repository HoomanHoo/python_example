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














