# 시퀀스형
# 컨테이너(container : 서로다른 자료형[list, tuple, deque ])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array, memoryview])
# 가변(list, bytearray, array, memoryview, deque) 
# 불변(tuple, str, bytes)으로 나눌 수 있다

#리스트 및 튜플 고급!

#지능형 리스트(Comprehending list)

chars = '+_)(*&^%$#@!' # str/flat/불변
#chars[2] = 'h' # 불가능 불변형이기 때문에

code_list1 = []

for s in chars:
    code_list1.append(ord(s))
print(code_list1)

# 지능형 리스트
code_list2 = [ord(s) for s in chars]
print(code_list2)

# 지능형 리스트 + map + filter

code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars))) # 람다 다시 공부

print(code_list3)
print(code_list4)


#generator 생성

import array
 
 #Generator : 한 번에 한 개의 항목을 생성 (메모리 유지 x)

tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(array_g)
print(array_g.tolist())

#제너레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

# 리스트 주의
# 증명
marks1 = [['~'] * 3 for n in range(4)]
marks2 = [['~'] * 3] * 4
print(marks1)
print(marks2)

print()

marks1[0][1] = 'x'
marks2[0][1] = 'x'
print(marks1) 
print(marks2)

print([id(i) for i in marks1]) # 전부 다른 주소를 가지고 있음
print([id(i) for i in marks2]) #같은 주소를 가지고 있는 하나의 객체를 복사한 것