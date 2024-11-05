from zeeland import Singleton, singleton


@singleton()
class TestSingleton:
    pass


instance1 = TestSingleton()
instance2 = TestSingleton()

assert instance1 is instance2


class TestSingletonWithArgs(metaclass=Singleton):
    def __init__(self, value):
        self.value = value


instance1 = TestSingletonWithArgs("test1")
instance2 = TestSingletonWithArgs("test2")

assert instance1 is instance2
assert instance1.value == "test1"
