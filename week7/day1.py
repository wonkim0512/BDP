class BaseClass(object):
    def __init__(self):
        print('Base class instance!')

    def printBase(self):
        print("printing base")

class InheritingClass(BaseClass):
    def printInheriting(self):
        print("print inherting")

x = BaseClass()
y = InheritingClass()
x.printBase()
y.printBase()
y.printInheriting()
# x.printInheriting() # 'BaseClass' object has no attribute 'printInheriting'

print(BaseClass.__subclasses__())
# print(InheritingClass.__superclasses__())  # not exists

class Hero(object):
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def eat(self, food = None):
        if food == 'apple':
            self.hp += 5

        if food == 'banana':
            self.hp -= 15

        if not food:
            self.hp -= 50

IronMan = Hero('IronMan')
IronMan.eat('apple')
IronMan.eat('banana')
print(IronMan.hp)
IronMan.eat()
print(IronMan.hp)

class Calculator(object):
    secret = "I am class variable"
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def Add(self):
        result = self.a - self.b
        print("{} + {} = {} ...done!".format(self.a, self.b, result))

    def Sub(self):
        result = self.a - self.b
        print("{} - {} = {} ...done!".format(self.a, self.b, result))

    def Mul(self):
        result = self.a * self.b
        print("{} * {} = {} ...done!".format(self.a, self.b, result))

    def Div(self):
        result = self.a / self.b
        print("{} / {} = {} ...done!".format(self.a, self.b, result))

x = Calculator(4,2)
x.Add()
x.Sub()
x.Mul()
x.Mul()
x.Div()
x.Div()

class HousePark(object):
    lastname = "Park" # instance variable because every instance should have 'Park'
    def __init__(self, name):
        self.fullname = self.lastname +" "+ name

    def travel(self, where):
        print("{} travels to {}".format(self.fullname, where))

    def love(self, other):
        print("{} loves {}".format(self.fullname, other.fullname))

    def fight(self, other):
        print("{} and {} have troubles".format(self.fullname, other.fullname))

    def __add__(self, other):
        print("{} married with {}".format(self.fullname, other.fullname))

    def __sub__(self, other):
        print("{} and {} got divorced".format(self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = 'Kim'

    def travel(self, where, day):
        print("{} travels to {} for {} day(s).".format(self.fullname, where, day))

member1 = HousePark("Karen")
member2 = HouseKim("Won")
member1.travel("London")
member2.travel("Louisville", 7)
member1.love(member2)
member1 + member2
member2.fight(member1)  # it is possible becuase HouseKim is inherting HousePark
member2 - member1       # it is possible becuase HouseKim is inherting HousePark
