# pydantic -> fastapi
# pydantic - валідація даних (!!!)

# pip install pydantic

from pydantic import BaseModel, Field

# class User(BaseModel):
#     # атрибут: тип_даних = Field( ліміт=значення )
#     id: int = Field(gt=0, lt=1000)
#     name: str = Field(min_length=1, max_length=50)

# user = User(id=44, name="John")
# print(user.model_dump())
# print(user.model_dump_json())
# print(user.name)
# print(user.id)

# class User(BaseModel):
#     id: int = Field(gt=0)
#     name: str = Field(min_length=1)
#     # 2 способи як діяти з необов'язковими данним: 
#     # 1) давати за замовчуванням
#     likes_dogs: bool = Field(default=True)
#     # 2) використовувати None
#     # Union -> декілька типів поставити в умову (або - або)
#     email: str | None = Field(default=None)

# user = User(id=222, name="John", likes_dogs=False)
# print(user)

class Item(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(default=0.0)

class Order(BaseModel):
    # items: список із Item
    items: list[Item] = Field(min_items=1)

order = Order(items=[
    { "name": "Car" }
])
print(order)
