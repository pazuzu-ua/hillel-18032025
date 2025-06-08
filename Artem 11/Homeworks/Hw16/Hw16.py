class MagicNumber:

    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return f"Total:{self.__value}"

    def __add__(self, other):
        return MagicNumber(self.__value + other.__value)


mn_1 = MagicNumber(3)
mn_2 = MagicNumber(9)
print(mn_1 + mn_2)
