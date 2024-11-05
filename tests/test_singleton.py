import pytest

from zeeland.singleton import AbstractSingleton, Singleton, singleton


class TestSingleton:
    def test_singleton_metaclass(self):
        class SingletonClass(metaclass=Singleton):
            pass

        instance1 = SingletonClass()
        instance2 = SingletonClass()
        assert instance1 is instance2

    def test_abstract_singleton(self):
        class ConcreteClass(AbstractSingleton):
            pass

        instance1 = ConcreteClass()
        instance2 = ConcreteClass()
        assert instance1 is instance2

    def test_singleton_decorator(self):
        @singleton()
        class DecoratedClass:
            pass

        instance1 = DecoratedClass()
        instance2 = DecoratedClass()
        assert instance1 is instance2

    def test_singleton_with_args(self):
        class SingletonWithArgs(metaclass=Singleton):
            def __init__(self, value):
                self.value = value

        instance1 = SingletonWithArgs("test1")
        instance2 = SingletonWithArgs("test2")
        assert instance1 is instance2
        assert instance1.value == "test1"  # First initialization value persists

    def test_multiple_singleton_classes(self):
        class SingletonA(metaclass=Singleton):
            pass

        class SingletonB(metaclass=Singleton):
            pass

        instance_a1 = SingletonA()
        instance_a2 = SingletonA()
        instance_b1 = SingletonB()
        instance_b2 = SingletonB()

        assert instance_a1 is instance_a2
        assert instance_b1 is instance_b2
        assert instance_a1 is not instance_b1
