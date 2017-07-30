# class practice

class Car(object):
    carCount = 0
    __secretCount = 0
    def __init__(self, name):
        self.name = name
        Car.carCount += 1
        Car.__secretCount += 1

    def go(self):
        print(self.name, "goes forward.")

    def stop(self):
        print(self.name, "stops immediately.")

    def __add__(self, other):
        print("{} and {} have crashed".format(self.name, other.name))

    def __sub__(self, other):
        print("{} has surpassed {} just a second ago".format(self.name, other.name))

    #def __del__(self):
        #print(self.name, "is destroyed")

    def __gt__(self, other):
        if len(self.name) > len(other.name):
            print('{}is longer than {}'.format(self.name, other.name))

        else:
            print('{} is shorter than {}'.format(self.name, other.name))

    def __lt__(self, other):
        if self.name[0] > other.name[0]:
            print("{} is more energy efficient to {}".format(self.name, other.name))

        else:
            print("{} is more energy efficient to {}".format(other.name, self.name))


class Sedan(Car):
    def go(self): # overriding
        print(self.name, "smoothly goes forward.")

    def stop(self):
        print(self.name, "has advanced ABS system")

    def comfort(self, level):
        self.level = level
        print(self.name, "can adjust comfort level for ", self.level, "levels")

class SUV(Car):
    def go(self):
        print(self.name, "actively runs forward")

    def stop(self):
        print(self.name, "has driver safety helper system.")

    def sport(self, *args):
        print(self.name, "has ",len(args), "driving mode(s):", *[mode for mode in args])

    def sport1(self, **kwargs):
        print(self.name, "has ",len(kwargs), "driving mode(s):", *[mode for mode in kwargs])

    def sport2(self, **kwargs): # 'kwargs' is stored in dictionary
        print(self.name, "has ",len(kwargs), "driving mode(s):",
         *[mode for mode in kwargs])


class S600(Sedan):
    def __init__(self, name, grade = None): # it needs 'name'
        super(Sedan, self).__init__(name) # super(parent, self).__init__(arg which I will use)
        self.grade = int(input("What is your membership grade?(1st/2nd/3rd):")[0])

    def go(self):
        print(self.name, 'is really famous for its comfort driving')

    def stop(self):
        print(self.name, 'has fantastic breaking system')

    def BenzService(self):
        print(self.grade, "grade mambership has", 4-self.grade, 'benefits')



a = Car("My car")
a.go()
a.stop()
print("There are",a.carCount, "cars")
print("*"*20)

b = Sedan("A sedan")
b.go()
b.stop()
b.comfort(4)
print("There are",b.carCount, "cars")
print("*"*20)

c = SUV("A SUV")
c.go()
c.stop()
c.sport('sport', 'comfort', 'rainy', 'climbing')
c.sport1(mode1 = 'sport', mode2 = 'comfort')
c.sport2(mode = ['sport','comfort']) # how can I print sport comfort ? #############
print("There are",c.carCount, "cars")
print("*"*20)

d = S600('S600')
d.BenzService()
d.go()
d.stop()
print("There are",d.carCount, "cars")
#print(d.__secretCount) # secret count
print(d._Car__secretCount) # If you really want to access to the secret..
print("*"*20)

# overloading
b + c
b - c
b > c
b < c
#del c # why not just SUV ???##############################
print(Car.__subclasses__()) # Sedan, SUV
print(Car.__doc__)
print(Car.__dict__)
print(Car.__module__)
print(Car.__bases__)
print(Sedan.__name__) # what about b.__name__
################ practice #################
# class inheritance
class A(object):
    def __init__(self, x):
        self.x = x

    def fa(self):
        return 10 * self.x

class B(A):
    def fb(self):
        return 1000 * self.x

a = A(5)
print(a.fa())

b = B(5)
print(b.fb())
print(b.fa())
#print(a.fb()) # specialization

# Instance method and class method

class A(object):
    def foo(self):
        print("foo")

    @classmethod
    def class_foo(self):
        print("class_foo")

a = A()
a.foo()
a.class_foo()
#A.foo() # foo() is instanace method
A.class_foo()

class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.simplify()

    def simplify(self):
        g = Fraction.gcd(self.num, self.den)
        self.num = self.num // g
        self.den = self.den // g

    @staticmethod
    def gcd(a,b):
        while b != 0:
            a, b = b, a%b
        return a
