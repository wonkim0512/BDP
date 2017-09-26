from abc import ABC, abstractmethod


class A(object):
    def __init__(self, x):
        self.x = x

    def f(self):
        return 10 * self.x

    def g(self):
        return 100 * self.x

class B(A):
    def __init__(self, x = 42, y = 99):
        super().__init__(x)
        self.y = y

    def f(self):
        return 1000*self.x

    def g(self):
        return (super().g(), self.y)

class C(object):
    def foo(self):
        print("executing foo")

    @classmethod
    def class_foo(cls):
        print('executing class_foo')


class BaseClass(ABC):
    @abstractmethod
    def func1(self):
        pass

    @abstractmethod
    def func2(self):
        pass

class Child(BaseClass):

    def func1(self):
        print("func1")

    def func2(self):
        print("func2")

    def foo(self):
        print("executing foo")

def iteration_test(lst):
    it = iter(lst)
    for i in range(len(lst)):
        print(next(it))

if __name__ == "__main__":
    a = A(5)
    b = B(7)
    print(a.f())
    print(a.g())
    print(b.f())
    print(b.g())

    c = C()
    c.foo()
    c.class_foo() # instance is able to access to everthing!

    C.class_foo()
    #C.foo() #TypeError

    #parent1 = BaseClass() #TypeError: Can't instantiate abstract class BaseClass with abstract methods func1, func2
    child1 = Child()
    child1.func1()
    child1.func2()

    iteration_test([1,2,3,4,3,2,10])