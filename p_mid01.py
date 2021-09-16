# 클래스 메소드 심화
# 객체지향 -> 코드의 재사용, 코드 중복 방지


#딕셔너리 구조
#코드 반복 지속, 중첩 문제(키), 키 조회 예외처리 등

car_dict = [
    {'car_company': 'Ferrai', 'car_detail': {'color': 'White', 'horsepower':400, 'price': 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color': 'Black', 'horsepower':270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'Silver', 'horsepower':300, 'price': 6000}}
]

del car_dict[1]
print(car_dict)

print()
print()

#클래스 구조

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    #사용자 레벨에서 프린트 문으로 정보를 확인할때
    # str이 있으면 str이 먼저
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    #엔지니어 레벨에서 객체의 엄격한 타입 정보를 나타낼때에는
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)



car1 = Car('Ferrari', {'color': 'White', 'horsepower':400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower':270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower':300, 'price': 6000})
print(car1)
print(car2)
print(car3)

print(car1.__dict__)