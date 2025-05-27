# Принципи ООП:

# 1. Абстракція (приховуємо імплементацію / залишаємо користувачеві інтерфейс)
# faker = Faker
# faker.name()

# 2. Наслідування (батько - діти / нащадки)

# 3. Інкапсуляція (захист даних - атрибути і методи)
# публічно (відкрите) / захищене / приватне
# public / protected / private

# class Account:
#     def __init__(self, balance) -> None:
#         self.balance = balance

# ac = Account(500)
# ac.balance -= 200

# class Box:
#     def __init__(self, a, b, c) -> None:
#         self.my_public = a
#         self._my_protected = b
#         self.__my_private = c

# box = Box(1, 2, 3)
# # print(box.my_public)
# # print(box._my_protected)
# # print(box.__my_private)

# print( dir(box) )
# class BankAccount:
#     def __init__(self) -> None:
#         self.__balance = 0
    
#     def deposit(self, amount):
#         # ----- тут може бути будь-яка валідація
#         self.__balance += amount
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             raise ValueError("Not enough money...")
    
#     def get_balance(self):
#         return self.__balance

# a = BankAccount()
# print( a.get_balance() )
# a.deposit(200)
# print( a.get_balance() )
# a.withdraw(500)
# print( a.get_balance() )

class Square:
    def __init__(self, size) -> None:
        self.__size = size
        self.__square = None # lazy

    # utility
    def _calculate_sqr(self):
        if not self.__square:
            # print('-- CALCULATION --')
            self.__square = self.__size * self.__size # будемо вважати: дуже коштовна логіка
        return self.__square

    def get_size(self):
        return self.__size

    def set_size(self, value):
        self.__size = value
        self.__square = None

    def get_info(self):
        return f"Square({self.__size}x{self.__size}) with sq. {self._calculate_sqr()}"

sq = Square(6)
# info = sq.get_info()
# print(info)
# sq.set_size(10)
# info = sq.get_info()
# print(info)

# 4. Поліморфізм (різні класи, але однакові інтерфейси)

# class Animal:
#     def __init__(self, name) -> None:
#         self.name = name

#     # це по суті: інтерфейс
#     def cry(self):
#         raise TypeError("Should be implemented...")

# class Lion(Animal):
#     def cry(self):
#         print( f"{self.name} roars!" )

# class Bird(Animal):
#     def cry(self):
#         print( f"{self.name} chirps!" )
    
# class Dog(Animal):
#     def cry(self):
#         print( f"{self.name} barks!" )

# class Cat(Animal):
#     def cry(self):
#         print( f"{self.name} meows!" )

# zoo = [
#     Lion("Alex"),
#     Bird("Anzud"),
#     Dog("Billy"),
#     Cat("Chloe"),
# ]

# for animal in zoo:
#     animal.cry()

# композиція
# class Sword:
#     def attack(self):
#         print("Atacks with a sword!")

# class Sable:
#     def attack(self):
#         print("Atacks with a sable!")

# class Bow:
#     def __init__(self, arrows=0):
#         self.__arrows = arrows

#     def attack(self):
#         if self.__arrows:
#             print("Atacks with a bow!")
#         else:
#             print("No arrows...")

# class Pike:
#     def attack(self):
#         print("Atacks with a pike!")

# class Warrior:
#     def __init__(self, name):
#         self.name = name
#         self.__weapon = None
    
#     def wield(self, weapon):
#         self.__weapon = weapon
    
#     def attack(self):
#         if not self.__weapon:
#             print("You have no weapon...")
#         else:
#             self.__weapon.attack()

# warrior = Warrior("Denis")
# warrior.wield( Sable() )
# warrior.attack()
# warrior.wield( Bow(10) )
# warrior.attack()

# class Human -->  objects ( HumanA, HumanB ...  )
# class Human:
#     population = 0 # атрибут класу і належить виключно класу

#     def __init__(self, name):
#         Human.population += 1
#         self.name = name

#     # instance method
#     def get_name(self):
#         return self.name

#     # class method
#     @classmethod           # wrapper // decorator
#     def get_population(cls):
#         return cls.population

#     @staticmethod
#     def validate_name(name):
#         if name and len(name) < 10:
#             return True
#         return False

# a = Human("Adam")
# print(
#     a.get_name(),
#     a.get_population(),
#     sep="\n"
# )
# b = Human("Stepan")
# print(
#     b.get_name(),
#     b.get_population(),
#     a.get_population(),
#     Human.get_population(),
#     sep="\n"
# )

# population = Human.get_population()
# print(population)

# adam = Human("Adam")
# population = Human.get_population()
# print(population, adam.get_population())

# result = Human.validate_name("John")
# print(result)
# john = Human("John")
# population = Human.get_population()
# print(population, adam.get_population())

# class Math:

#     @staticmethod
#     def square_area(size):
#         return size * size

# print(  Math.square_area(6) )

# -------------------------------------------------
# dunder / magic __NAME__

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0
    
#     def deposit(self, amount):
#         self.__balance += amount
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             raise ValueError("Not enough money...")

#     def __str__(self):
#         # print(self)
#         return f"Bank Account with balance: {self.__balance}"
    
#     def __add__(self, other):
#         return self.__balance + other.__balance
    
#     def __sub__(self, other):
#         return self.__balance - other.__balance
    
#     def __gt__(self, other):
#         return self.__balance > other.__balance

# ba = BankAccount()
# ba.deposit(100)

# bb = BankAccount()
# bb.deposit(300)

# # print(ba + bb) # ba.__add__( bb )
# # print(ba - bb) # ba.__sub__( bb )
# print( ba > 100 )

class Box:
    def __init__(self):
        self.__box = []
    
    def put(self, ob):
        self.__box.append(ob)

    def show(self):
        return self.__box

    def __len__(self):
        return len(self.__box)

b = Box()
b.put(1)
b.put(2)

print( len(b) )
