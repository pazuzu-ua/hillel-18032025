class Car:
    def __init__(self, colour, make, model, price):
        self.colour = colour
        self.make = make
        self.model = model
        self.price = price

    def get_info(self):
        return f"Авто: {self.make} {self.model}, Колір: {self.colour}, Ціна: ${self.price}"
