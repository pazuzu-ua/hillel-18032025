class Car:
    def __init__(self, colour, make, model, price):
        self.colour = colour
        self.make = make
        self.model = model
        self.price = price

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}, Колір: {self.colour}, Ціна: {self.price} грн"
    
car = Car(
    colour="Зелений",
    make="Volkswagen",
    model="Tiguan",
    price=750000
)

print(car.get_info())
