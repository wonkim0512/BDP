class asd(object):
    def __init__(self):
        self.items = [1,2]

    def __str__(self):
        return self.items.__str__()

    def type(self):
        return type(self.items.__str__())

asd = asd()
print(asd)
print(asd.type())
