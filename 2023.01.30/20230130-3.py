class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
        print(f'{self.breed}종인 {self.name}가 태어남!')

    def bark(self):
        print(f'{self.name} 월월')

    def __del__(self):
        Doggy.num_of_dogs  -= 1
        print(f'{self.name} 쥬금')

    @classmethod
    def get_status(cls):
        print(f'현재:{cls.num_of_dogs}, 태어남:{cls.birth_of_dogs}')

dog1 = Doggy('가람이', '말티즈')
dog1.bark()
Doggy.get_status()
dog2 = Doggy('몰라', '모른다구')
Doggy.get_status()
del dog2
Doggy.get_status()

