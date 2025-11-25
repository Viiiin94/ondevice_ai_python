def add(x, y):
    return x + y


def sayHello():
    return "Hello world!"


def sayGoodbye():
    print("Good bye!")


def function_tuple(*wargs):
    print(type(wargs))
    print(wargs)


function_tuple(1, 2, 3, 4, 5, 6)


def function_dict(**kwargs):
    print(type(kwargs))
    print(kwargs)


function_dict(name="yyb", age=18, gender="Male")

# a = input("더할 첫 숫자 입력 : ")
# b = input("두 번째 숫자 입력 : ")
# print(a + b)  # 문자열끼리의 합
# print(int(a) + int(b))  # 정수로 치환해서 합쳐야 더해짐

# # 먼저 치환해도 됨
# a1 = int(input("더할 첫 숫자 입력 : "))
# b1 = int(input("두 번째 숫자 입력 : "))

# print("a", "b", "c", sep=" ")  # default가 띄어쓰기
# print(a, b)

for i in range(10):
    print(i, end=' ')  # default가 \n 지금은 띄어쓰기

for i in range(10):
    print(i, end='\n')

# 파일 자동 생성
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
line = f.readline()
print(line)  # 1번째 줄입니다.
line = f.readline()
print(line)  # 2번째 줄입니다.
line = f.readline()
print(line)  # 3번째 줄입니다.

while True:
    line = f.readline()
    if not line:
        break
    print(line)  # 1~10번째 줄까지 다 읽음

lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)

f.close()  # close가 없으면 파일이 생성되지 않음 / 파일은 생성이 되는데 저장하지 않아서 없어지는거라고함

# with : 자동으로 open되고 close가 된다.
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

# 한글 파일 쓰기
with open("한글파일.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요, 파이썬!")

# 한글 파일 읽기
with open("한글파일.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

a = input("두 수를 공백문자로 구분하여 입력하세요.")
print(a.split())
b = map(int, a.split())
print(list(b))

c = list(map(int, input("두 수를 입력하세요").split()))
print(c[0] + c[1])

print(sum(list(map(int, input("2개의 숫자를 입력하세요. : ").split()))))
