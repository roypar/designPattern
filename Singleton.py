class Singleton:
    instance = None

    def __init__(self, num):
        if Singleton.instance is None:
            self.type = num
            Singleton.instance = self
        else:
            raise Exception("Singleton has already been assigned")

    @classmethod
    def getInstance(cls):
        return cls.instance


if __name__ == "__main__":
    s1 = Singleton(5)
    print(s1)
    print(s1.type)

    s2 = Singleton.getInstance()
    print(s2)
    print(s2.type)
