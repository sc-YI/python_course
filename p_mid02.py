
class Car():
    """
    Car class
    Author : Kim
    Date: 2021.07.30
    """

    #클래스 변수
    car_count = 0

    def __init__(self, company, details):
        self._company = company #인스턴스 변수
        self._details = details
        Car.car_count += 1

    #사용자 레벨에서 프린트 문으로 정보를 확인할때
    # str이 있으면 str이 먼저
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    #엔지니어 레벨에서 객체의 엄격한 타입 정보를 나타낼때에는
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Currnet ID : {}'.format(id(self)))
        print('car Detail Info : {} {}'.format(self._company, self._details.get('price')))


#self 의미 self가 있어야 자기 인스턴스 안에 있는 애트리뷰트의 벨류를 따로따로 관리할 수 있음.

car1 = Car('Ferrari', {'color': 'White', 'horsepower':400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower':270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower':300, 'price': 6000})

# ID 확인 각자 고유의 값을 가지고 있음
print(id(car1))
print(id(car2))
print(id(car3))

#dir & __dict__ // 
print(dir(car1))
print(dir(car2))

#Doctring
print(Car.__doc__)


# 공유확인
Car.detail_info(car1)
print(car1.__dict__)
print(car1.car_count)
print(dir(car1))


# 접근

print(car1.car_count)
print(Car.car_count)