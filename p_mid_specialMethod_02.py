# 파이썬의 핵심 1. 시퀀스 2. 반복(Iterator) 3. 함수 4. 클래스
# 클래스 안에 정의할 수 있는 특별한 빌트인 메소드
#벡터 


class Vector():

    def __init__(self, *arg):
        '''
        Create a vector, example : v = Vector(5,10)
        '''
        if len(arg) == 0:
            self.x, self.y = 0, 0
        else:
            self.x, self.y = arg

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __add__(self, other):
        '''
        Return the vector addtion of self and other
        '''
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, y):
            return Vector(self.x * y, self.y * y)
    
    def __bool__(self):
        return bool(max(self.x, self.y))


#Vector 인스턴스 생성
#     
v1 = Vector(5,7)
v2 = Vector(23, 25)
v3 = Vector()

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(bool(v1),bool(v2),bool(v3))