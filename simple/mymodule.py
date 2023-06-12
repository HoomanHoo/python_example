__version__ = 1.0
name = "홍길동"
age = 30
def hello():
    print("hello")
def bye():
    print("bye")

class User:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age