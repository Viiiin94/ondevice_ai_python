str = "HELLO WORLD!"

list = [1, 2, 3, 4, 5]

list2 = [[1, 2], [3, 4], [5, 6]]

list3 = [[[1], 2], [3, 4], [5, 6]]

# [1, 2]
print(list2[0])

# [1]
print(list3[0][0])

# 1
print(list3[0][0][0])

# slicing idx
print(list[0:3])
print(list[:3])
print(list[2:])

# reverse idx
print(list[-1])

# list add
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# list 더하기 list는 list가 합쳐져서 나옴
print(list_a + list_b)  # [1, 2, 3, 4, 5, 6]
print(list_a * 3)

# list 더하기 숫자는 안됨
# print(list_a + 3) # 안됨

# calculation
numb = 3
print(numb + 1)
print(numb - 1)
print(numb * 2)
print(numb / 1)  # float 형태로 나옴
print(numb % 2)  # 나머지만
print(numb // 2)  # 몫만

# python에는 증감 연산자가 없음 --, ++

# list 요소의 갯수
print(len(list))

# list 바꾸기
list[3] = 11
print(list)

# list 지우기 del = python 내장 키워드(예약어)
# del list[4]
# del list[:2]
# del list[3:]

# list 추가하기 append
list.append(7)
list.append([5, 9])  # 2개가 하나의 배열로 들어감 [5, 9]

# list reverse
list.reverse()

# list index
list.index(2)  # 숫자 2의 인덱스

# list remove
list.remove(2)  # 숫자 2를 찾아서 지워라

# list pop
list.pop()  # 제일 마지막 index를 끄집어 냄
a = list.pop()  # 이런식으로 변수로 선언을 해주면 리스트에서 나와서 저장이 됨

# tuple t(1, 2, 3 'a')
# 불변성 = 안의 내용은 못 바꾸나 덮어쓰기만 가능
t1 = (1, 2, 3)
t2 = ('a', 5, 'k')
t3 = t1 + t2
print(t3)  # (1, 2, 3, 'a', 5, 'k')

t1 = t2 + t3
print(t1)  # ('a', 5, 'k', 1, 2, 3, 'a', 5, 'k')

# dictionary {key : value} 조합
# 튜플과 리스트와 다르게 index를 내 맘대루
dic = {'name': 'youngbin', 'age': 32, 'male': True}
print(dic['name'])

# dictionary.keys() 딕셔너리 키만 나오게
# dictionary.values() 딕셔너리 밸류만 나오게
# dictionary.items() 딕셔너리를 튜플로 키 밸류 표현

# 집합 자료형 Set
# 같은 값을 여러번 넣어도 한 번만 중복 x
# indexing이 안됨
seta = {1, 2, 3}
print(seta)
print(type(seta))

s1 = set([1, 2, 3])

# remove : 있으면 해당 숫자의 index를 찾아서 지워라

# discard : 있으면 지우고 없으면 말아라

# 불 자료형
a = True
b = False

print(1 == '1')  # False
print(a == True)  # True
c = ''
