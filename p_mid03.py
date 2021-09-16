
class Car():
    """
    Car class
    Author : Lee
    Date: 2021.08.02
    Description : class, Static, Instance Method
    """


    #클래스 변수
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company #인스턴스 변수
        self._details = details

    #사용자 레벨에서 프린트 문으로 정보를 확인할때
    # str이 있으면 str이 먼저
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    #엔지니어 레벨에서 객체의 엄격한 타입 정보를 나타낼때에는
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    #Instance Method
    #self 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Currnet ID : {}'.format(id(self)))
        print('car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price')* Car.price_per_raise)
    #class Method

    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price incresased!')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        else:
            return 'Sorry. This car isn\'t Bmw'


#self 의미 self가 있어야 자기 인스턴스 안에 있는 애트리뷰트의 벨류를 따로따로 관리할 수 있음.

car1 = Car('Ferrari', {'color': 'White', 'horsepower':400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower':270, 'price': 5000})

print()
#전체정보
car1.detail_info()
car2.detail_info()

# 가격정보(직접 접근) - 이런 접근은 좋지 않음. 메소드 사용
print(car1._details.get('price'))

# 가격정보(간접 접근)

#인상 전
print(car1.get_price())
print(car2.get_price())

raising = float(input())
Car.raise_price(raising)

#인상 후
print(car1.get_price_culc())
print(car2.get_price_culc())


#인스턴스 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))


#클래스로 호출
print(Car.is_bmw(car2))