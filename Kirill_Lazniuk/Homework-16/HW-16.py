class MagicNumber:
    def __init__(self, value):
        self.__value = value

    def __add__(self, other):
        if isinstance(other, MagicNumber):
            return MagicNumber(self.__value + other.__value)
        return NotImplemented

    def get_value(self):
        return self.__value 

    def __repr__(self):
        return f"MagicNumber({self.__value})"


a = MagicNumber(10)
b = MagicNumber(20)
c = a+b
print(c)
print(c.get_value())