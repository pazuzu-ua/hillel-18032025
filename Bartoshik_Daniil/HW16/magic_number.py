class MagicNumber:
    def __init__(self, value):
        self.__value = value

    def __add__(self, other):
        if isinstance(self, MagicNumber):
            return MagicNumber(self.__value + other.__value)
        return NotImplemented

    def get_value(self):
        return self.__value

a = MagicNumber(6)
b = MagicNumber(4)
c = a+b

print(c.get_value())