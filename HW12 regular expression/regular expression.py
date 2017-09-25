import re


def first_two_char(string):
    pattern = "(^| )(.{2})"
    first_two = list(map(lambda x: x[1], re.findall(pattern, string)))
    print(first_two)


def email_domain(string):
    addresses = re.split(", ", string)
    domains = list(map(lambda address: address.split("@")[1], addresses))
    print(domains)


def return_date(string):
    pattern = r"\d{2}[-]\d{2}[-]\d{4}" # 맞는 것은 다 가져오니까 사실 [-]로 할 필요없이 -만 하면됨.
    dates = re.findall(pattern, string)
    print(dates)


def start_with_vowel(string):
    pattern = r"\b[aeiou]\w*" # r"\b[aeiou].*" 왜 이거로 하면 안되지? space도 포함이 되기 때문이다.
    result = re.findall(pattern, string, re.I)
    print(result)


def is_cellphone_number(string):
    pattern = r"010-\d{3,4}-\d{4}"
    if re.match(pattern, string):
        return True
    return False


if __name__ == "__main__":
    string1 = "Earth is the third planet from the Sun"
    first_two_char(string1)

    string2 = "abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz"
    email_domain(string2)

    string3 = "Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009"
    return_date(string3)

    string4 = "Earth's gravity interacts with ohter objects in space, especially the Sun and the Moon"
    start_with_vowel(string4)

    lst = ["010-256-1354", "010-1234-5576", "070-642-0384", "010-290*-4858", "0105734123"]
    for number in lst:
        print(is_cellphone_number(number))