import os
os.system('clear')

#클래스 선언
class Dog:
    name = 'default'
    gender = 'Male/female'
    owner = 'default name'

    def Bark(self):
        print(self.name + ':멍멍')

# 객체 생성과 사용 방법
dog = Dog()
dog.name = "노랑이"
dog.gender = "Male/female"