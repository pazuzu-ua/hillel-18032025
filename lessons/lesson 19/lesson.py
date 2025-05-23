# Об'єкто Орієнтовне Програмування (OOP)
# парадигма - це збірка методів

# 1. Абстракція - приховання імплементації (= як зроблено)
# Клас - креслення
# екземпляр класу - це об'єкт
# об'єкт: змінні (атрибути), функції (методи)
# В ПАЙТОНІ - УСЕ Є ОБ'ЄКТОМ

# tree = Tree()
# tree.att = "aaa"

# class НазваКласу
# class Tree:
#     ...

# my_tree = Tree()
# # print(my_tree)
# # print(type(my_tree))
# # print(dir(my_tree))

# my_tree.name = "Knowledge"
# print(my_tree.name)
# print(dir(my_tree))


# -- КОНСТРУКТОР       Class.__init__()    -> налаштовує екземпляр / об'єкт класу
# class Tree:
#     # Створи мені дерево!
#     # Кожне (self) дерево має мати листя!
#     #            ( self - обов'язковим, вказує на об'єкт   ---   атрибути які будуть обов'язкові )
#     def __init__(self, tree_type) -> None:
#         self.tree_type = tree_type

# my_tree1 = Tree("oak")
# my_tree2 = Tree("birch")
# # self = Tree.__init__(self, "oak")
# # my_tree.tree_type = "oak"
# print(my_tree1.tree_type)
# print(my_tree2.tree_type)

# class Cat:
#     # конструктором класу - налаштовує об'єкт
#     def __init__(self, name, collar_size, colour="black") -> None:
#         self.name = name
#         self.collar_size = collar_size
#         self.colour = colour
#         self.animal_type = "cat"
    
#     def meow(self):
#         print(f"{self.name} says meow!")

# cat_a = Cat("Mr. Cat", 12)
# cat_b = Cat("Mrs. Cat", 12)

# cat_a.meow()
# cat_b.meow()

# """ 
#    Коло:
#      кожне коло має радіус

#     площа:
#      радіус кожного кола в квадраті * ПІ
# """

# some_variable_radius = 10
# class Circle:
#     # атрибути = унікальні змінні в об'єкті
#     def __init__(self, radius_input_by_user) -> None:
#         self.radius = radius_input_by_user
    
#     # методі = функції
#     def area(self):
#         print(some_variable_radius)
#         return 3.14 * (self.radius ** 2)

# a = Circle(10)
# a_area = a.area()
# print(a_area)

# b = Circle(50)
# b_area = b.area()
# print(b_area)

class Warrior:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    # utility
    def get_damage(self, damage):
        if self.health > 0:
            self.health -= damage
        if self.health <= 0:
            print("The warrior is dead...")
    
    def attack_warrior(self, another_warrior):
        another_warrior.get_damage( self.attack )

archer = Warrior(40, 10)
pikeman = Warrior(25, 15)

print(archer.health)
pikeman.attack_warrior(archer)
# pikeman.attack_warrior(archer)
# pikeman.attack_warrior(archer)
# pikeman.attack_warrior(archer)
# print(archer.health)

# # pikeman.attack_warrior(archer)
# # archer.get_damage( pikeman.attack )

# 2. Наслідування
# батьківський клас
# class Animal:
#     def __init__(self, name, weight, size) -> None:
#         self.name = name
#         self.weight = weight
#         self.size = size
    
#     def call(self):
#         print("Animal noises")

# class Dog(Animal):
#     def __init__(self, name, weight, size, coller_size) -> None:
#         # можливість дістати методі батьківського класу - super()
#         super().__init__(name, weight, size)
#         self.coller_size = coller_size

#     def call(self):
#         print("Woof-woof!")

# class Cat(Animal):
    
#     def call(self):
#         print("Meow-meow")

# # ChildClass.method = ChildClass.method => ParentClass.method

# my_dog = Dog("Bobik", 16, 60, 11)
# my_cat = Cat("Barsik", 6, 22)
# # print(my_dog.name)
# # print(my_cat.name)

# my_dog.call()
# my_cat.call()
