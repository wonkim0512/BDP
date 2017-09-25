import re

string = "abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz"
addresses = re.split(", ", string)
domains = list(map(lambda address: address.split("@")[1], addresses))
print(domains)
