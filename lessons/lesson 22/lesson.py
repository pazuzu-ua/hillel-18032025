from typing import Any, Literal
from decimal import Decimal

from pydantic import BaseModel, Field


# class Example(BaseModel):
#     # str, int, float, list, tuple, dict
#     # Class
#     example_str: str = Field(default="", min_length=0, max_length=22)
#     # gt >    ge >=    lt <    le   <=
#     example_int: int = Field(default=11, gt=6, le=150 )
#     example_float: float = Field(default=0)
#     # Decimal -> better float
#     example_decimal: Decimal = Field(default=10)
#     #-----------------------------------
#     # список стрічок
#     example_list: list[str]
#     example_list_2: list[ str | int | dict ] # [ 1, "hello", { "1": 1 } ]
#     # dict
#     example_dict: dict[str, int | str] # { "1": 1, "2": "2" }
#     # tuple - кортежі
#     example_tuple: tuple[ str, int, int ]  # ( "a", 1, 2 )
#     # -----------------------------------------
#     example_any: Any # будь-який тип
#     example_literal: Literal["hello"]
#     example_literal_2: Literal["cat", "dog", "fish", "parrot"]

# class Pet(BaseModel):
#     animal_type: Literal["cat", "dog", "fish", "parrot"]
#     name: str

# pet = Pet(name="Random", animal_type="cat")
# print(pet)

# enumaretion - перечислення
# from enum import Enum

# class AnimalTypeEnum(Enum):
#     # ключ = значення
#     cat = "cat"
#     dog = "dog"
#     fish = "fish"
#     parrot = "parrot"

# # print( AnimalTypeEnum.cat.value )
# class Pet(BaseModel):
#     animal_type: AnimalTypeEnum
#     name: str

# pet = Pet(name="Boo", animal_type="cat")
# print(pet)

# --------------------------------------- FACTORY - фабрики
# class FactoryExample(BaseModel):
#     name: str = Field(default="hello")
#     some_list: list = Field(default_factory=list)
#     some_dict: dict = Field(default_factory=dict)

# def some_funct(some_list=[]):
#     ...

# import random

# class Example(BaseModel):
#     # ЯКЩО ФУНКЦІЯ ПРИЙМАЄ ЯКІСЬ ПАРАМЕТРИ
#     # random.RANDINT( a, b )
#     # лямбда - анонімна функція
#     # lambda: функція(аргументи)
#     some_number: int = Field(default_factory=lambda: random.randint(3, 5))

# a = Example()
# print(a)

# import uuid

# class Receipt(BaseModel):
#     receipt_id: uuid.UUID = Field(default_factory=uuid.uuid4)

# print(Receipt())



# ================================
