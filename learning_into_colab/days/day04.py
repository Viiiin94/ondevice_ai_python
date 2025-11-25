from module.mode1 import *
import datetime


class Car:
    def __init__(self):
        self.door_n = 4
        self.color = 'red'
        self.gear_mode = None

    def start(self):
        if self.gear_mode == 'parking':
            print('stop')
        else:
            print('start')


my_car = Car()
# print(my_car.color)
# print(my_car.door_n)


class Calculator:
    def __init__(self, a, b):
        self.result = 0
        self.a = a
        self.b = b

    def add(self):
        self.result = self.a + self.b
        return self.result

    def sub(self):
        self.result = self.a - self.b
        return self.result

    def mul(self):
        self.result = self.a * self.b
        return self.result

    def div(self):
        if self.b == 0:
            return "0으로 나눌 수 없습니다"
        self.result = self.a / self.b
        return self.result


# calc1은 객체라고 표현하고 calc1은 Calculator의 인스턴스이다
calc1 = Calculator(1, 5)
calc2 = Calculator(2, 8)

# print(calc1.add())
# print(calc2.mul())

# 클래스의 상속 MoreFourCal은 Calculator를 상속 받음 아들과 아빠의 차이


class MoreFourCal(Calculator):
    def pow(self):
        result = self.a ** self.b
        return result


calc3 = MoreFourCal(2, 0)
# print(calc3.pow())
# print(calc3.div())


class Family:
    lastname = '김'

    def __init__(self, name):
        self.name = name

    # lastname을 파라미터로 참조를 안해도 Family 클래스 안의 lastname을 알아서 참조함
    def printname(self):
        print(self.lastname, self.name)


철수 = Family('철수')
# 철수.printname()
Family.lastname = '이'
# 철수.printname()

print(add(5, 9))
