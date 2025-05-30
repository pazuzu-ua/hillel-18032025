# __method__ -- dunder // magic

# class Person:

#     # конструктор
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.species = "human"

#     # print(self) --> str(self)
#     def __str__(self):
#         return f"Person(name={self.name}, age={self.age})"

#     # ==
#     # person_a == person_b
#     # person_a.__eq__( person_b )
#     # def __eq__(person_a, person_b)
#     def __eq__(self, value):
#         return self.age == value.age
    
#     # lt <     le    <=    gt >      ge >=          ne   !=
#     def __lt__(self, value):
#         return self.age < value.age

#     def __gt__(self, value):
#         if isinstance( value, (int, float) ):
#             #    self.age   > 11
#             return self.age > value
#         else:
#             return self.age > value.age

# person_a = Person("John", 11)
# person_b = Person("Tom", 22)

# # print(person_a, person_b)

# # print( person_a == person_b )
# # print( person_a < person_b )

# print( person_a > 4 )
# print( person_a > 18.0 )
# print( person_a > person_b )

# class MagicNumber:

#     def __init__(self, number):
#         self.__number = number

#     def __str__(self):
#         return f"Magic({self.__number})"

#     # + - / *
#     def __add__(self, other):
#         return MagicNumber(self.__number + other.__number)

#     # __sub__   -
#     # __mul__   *
#     # __div__   /

# mn_a = MagicNumber(10)
# mn_b = MagicNumber(22)

# print( mn_a + mn_b )

# class Team:

#     def __init__(self):
#         self.__members = []

#     def add_member( self, member ):
#         self.__members.append(member)

#     def __str__(self):
#         return f"Team({str(self.__members)})"

#     def __len__(self):
#         return len(self.__members)

#     def __iter__(self):
#         return iter(self.__members)

#     def __getitem__(self, index):
#         return self.__members[index]

# t = Team()
# t.add_member("John")
# t.add_member("Andy")
# print(len(t))

# # for member in t:
# #     print(member)

# print( t[0] )

