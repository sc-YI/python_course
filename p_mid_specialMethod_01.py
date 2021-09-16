# 파이썬의 핵심 1. 시퀀스 2. 반복(Iterator) 3. 함수 4. 클래스
# 클래스 안에 정의할 수 있는 특별한 빌트인 메소드

print(int)

# 모둔 속성 및 메소드 출력
print(dir(int))

n = 10

print(n + 100)
print(n.__add__(100))
print(n.__doc__)


# 클래스 예제1

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return 'Fruit Class Info : {} {}'.format(self.name, self.price)
    
    def __add__(self, x):
        print('call add')
        return self.price + x.price

    def __sub__(self, x):
        print('call sub')
        return self.price - x.price

    def __le__(self, x):
        print('call le')
        if self.price <= x.price:
            return True
        else:
            return False

    def __ge__(self, x):
        print('call ge ')
        if self.price >= x.price:
            return True
        else:
            return False

#인스턴스 생성

s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1 + s2)
print(s1 - s2)
print(s1 >= s2)
print(s1 <= s2)

#일반적안 계산
#print(s1.price + s2.price)