# classmethod
class A(object):
    def instanceMethod(self):
        print("executing instance method")

    @classmethod
    def classMethod(cls): # according to PEP8. self is fine though.
        print("executing class method")

a = A()
a.instanceMethod()
a.classMethod()
A.classMethod()
#A.instanceMethod() # error


# staticmethod
class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.simplify()

    def __eq__(self, other):
        return (self.num == other.num) and (self.den == other.den)

    def simplify(self):
        g = Fraction.gcd(self.num, self.den)
        self.num //= g
        self.den //= g

    @staticmethod
    def gcd(a,b):
        while b != 0:
            a,b = b, a%b
        return a

f1 = Fraction(10, 12)
f2 = Fraction(5, 6)
print(f1 == f2)
print("*"*30)


# class inheritance
class School(object):
    member_count = 0

    def __init__(self, schoolname, location):
        self.schoolname = schoolname
        self.location = location
        School.member_count += 1

    def Location(self):
        print(self.schoolname + " is located in " + self.location)

class Teacher(School):
    def __init__(self, schoolname, subject):
        super().__init__(self, schoolname)
        self.subject = subject

    def Subject(self):
        print("I teach " + self.subject)

class Student(School):
    def __init__(self, schoolname, major):
        super().__init__(self, schoolname)
        self.major = major

    def Major(self):
        print("I study " + self.major)

Dr_Kang = Teacher("SNU", "Computer Schience")
Won = Student("SNU", "Economics")
Dr_Kang.Subject()
print(hasattr(Dr_Kang, "age"))
setattr(Dr_Kang, "age", 41)
print(hasattr(Dr_Kang, "age"))
print(getattr(Dr_Kang, "age"))
delattr(Dr_Kang, "age")
print(hasattr(Dr_Kang, "age"))

# staticmethod
class Test(object):
    num = 0

    @staticmethod
    def add(x, y): # no 'self'
        return x+y

print(Test.add(1,1)) # calling staticmethod through class

t = Test()
print(t.add(1,1)) # calling staticmethod through instance

class Test(object):
    num = 10

    @staticmethod
    def add(x,y):
        return x+y+self.num

print(Test.num)
t = Test()
#print(t.add(1,1))


# classmethod
class Test(object):
    num = 10

    @classmethod
    def add(cls,x,y): # we need 'cls' following pep8
        return x+y

print(Test.add(1,1))


# advanced example: difference between staticmethod and classmethod
class Date(object):
    word = "date: "

    def __init__(self, date):
        self.date = self.word + date

    @staticmethod
    def now():
        return Date('today')

    def show(self):
        print(self.date)

a = Date("2017/8/12")
a.show()
b = Date.now()
b.show()

class KoreanDate(Date):
    word = "날짜: "

a = KoreanDate.now()
a.show()

print("*"*30)
#####################################################
class Date(object):
    word = "date: "

    def __init__(self, date):
        self.date = self.word + date

    @classmethod
    def now(cls):
        return cls('today')

    def show(self):
        print(self.date)

a = Date("2017/8/12")
a.show()
b = Date.now()
b.show()

class KoreanDate(Date):
    word = "날짜: "

a = KoreanDate.now()
a.show()

# hash
print(hash("kim"))
s = set()
s.add(2/3)
print(s)
