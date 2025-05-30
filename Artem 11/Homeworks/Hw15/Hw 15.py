class Car:
    def __init__(self, colour, make, model, price) -> None:
        self.colour = colour
        self.make = make
        self.model = model
        self.price = price

    def get_info(self) -> str:
        return f"""        color: {self.colour}
        made by: {self.make}
        model: {self.model} 
        price: {self.price}"""


car_info = Car("Orange", "PythonCars", "Python_3XO", "5000 dollars")
print(car_info.get_info())
