class Cars:
    def __init__(self, colour, make, model):
        self.colour = colour
        self.make = make
        self.model = model

    def get_info(self):
        return(
        f"{self.make} {self.model}\n"
        f"Колір: {self.colour}\n"
        )
somecar = Cars(
    colour="Black",
    make="Dodge",
    model="Challenger",
)

print(somecar.get_info())
