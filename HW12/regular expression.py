import re


def first_two_char(string):
    pattern = "((^| ) (.+))+"
    print(re.match(pattern, string))

# 시작 operator ^, findall

def email_domain(string):
    addresses = re.split(", ", string)
    domains = list(map(lambda address: address.split("@")[1], addresses))
    print(domains)


def start_with_vowel(string):
    words = re.split(" ", string)
    pattern = "^[aeiouAEIOU].*"
    vowel_words = []

    for word in words:
        if re.match(pattern, word):
            vowel_words.append(word)

    print(vowel_words)



if __name__ == "__main__":
    string1 = "Earth is the third planet from the Sun"
    first_two_char(string1)

    string2 = "abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz"
    email_domain(string2)

    string4 = "Earth's gravity interacts with ohter objects in space, especially the Sun and the Moon"
    start_with_vowel(string4)