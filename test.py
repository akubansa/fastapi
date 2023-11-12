from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel



# tworzenie modelu
class User(BaseModel):
    id: int
    name: str #jak podajemy wartosci to dajemy =
    singup: Optional[datetime] = None
    friends: List[int] = [] # pusta lista

#inicjowanie klasy User, np dictonary pytonowe
external_data = {
    'id' : '1233',
    'name': 'Adam',
    'singup' : '2023-10-01 12:30',
    'friends': [1,2,3]

}

# #inicjacja klasy
user = User(**external_data)
#odpakowywujemy dict external_data za pomoca **
# #zmienna user mamy zainicjowana klase User z danymi z external_data

#mozemy jeszcze inaczej stworzyc zmienna z klasy
user2 = User(id=321,name='ala')


print(user2.dict())
#print(user.id, user.name)
#mozna zmienic klase zeby byla reprezentowana jak dict slownik pytonowy
#print(user.dict())