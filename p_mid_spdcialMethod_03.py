#객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

#일반적인 튜플

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

print(pt1)

from math import sqrt

leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(leng1)

#네임드 튜플 사용

from collections import namedtuple
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# 데이터 모델 파트에서 제대로 알고 있어야 함
print(pt3)
print(pt4)

leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(leng2)

# 네임드 튜플 선언 방법


Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x,y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename= True) # defalut 는 false


#Dict to Unpacking
temp_dict = {'x' : 75, 'y' : 55}


# print(Point4) # class로 나옴

p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y = 20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict) #딕셔너리 형태의 자료형을 언패킹 해줌

print()
print(p1)
print(p2)
print(p3)

#rename test

print(p4) #_2=30, _3=40
print(p5)

# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields)

# _asdict() : 정렬된 딕셔너리를 반환
print(p1._asdict())


#실사용 실습
# 반 20명, 4개의 반(A,B,C,D)

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

#list Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

# 추천
students2 = [Classes(rank, number)
            for rank in 'A B C D'.split()
                for number in [str(n) for n in range(1, 21)]]

print(len(students2))
print(students2)

#출력
for s in students2:
    print(s)