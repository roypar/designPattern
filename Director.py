class Car:
    def __init__(self, registration):
        self.__model = None
        self.__type = None
        self.__price = 0
        self.registration = registration

    def setModel(self, model):
        self.__model = model

    def setType(self, type):
        self.__type = type

    def setPrice(self, price):
        self.__price = price

    def getSpecification(self):
        return f'Registration: {self.registration}, Model: {self.__model}, Type: {self.__type}, Price: {self.__price}'


class Builder:
    def getModel(self):
        pass

    def getType(self):
        pass

    def getPrice(self):
        pass


class JeepBuilder(Builder):
    def __init__(self):
        self.__model = "Thar"
        self.__Type = "SUV"
        self.__Price = 20

    def getModel(self):
        return self.__model

    def getType(self):
        return self.__Type

    def getPrice(self):
        return self.__Price


class SedanBuilder(Builder):
    def __init__(self):
        self.__model = "Astra"
        self.__Type = "Sedan"
        self.__Price = 30

    def getModel(self):
        return self.__model

    def getType(self):
        return self.__Type

    def getPrice(self):
        return self.__Price


class Director:
    __builder = None
    __Instantiated = False

    def __init__(self):
        if Director.__Instantiated is False:
            Director.__Instantiated = True
        else:
            raise Exception("Director Already Initiated")

    @classmethod
    def setBuilder(cls, givenBuilder):
        cls.__builder = givenBuilder
        return

    @classmethod
    def getCar(cls, registration):
        car = Car(registration)
        car.setModel(cls.__builder.getModel())
        car.setType(cls.__builder.getType())
        car.setPrice(cls.__builder.getPrice())
        return car


if __name__ == "__main__":
    director = Director()

    builder = JeepBuilder()
    Director.setBuilder(builder)

    c1 = Director.getCar("Wb26s5113")
    print(c1.getSpecification())

    builder = SedanBuilder()
    Director.setBuilder(builder)

    c1 = Director.getCar("MH99c2312")
    print(c1.getSpecification())

    director = Director()