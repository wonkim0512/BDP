# -*- coding:utf-8 -*-

#1.
def first_perfect_square(numbers):
    for i in range(0,len(numbers)):
        if numbers[i] >= 0:
            if numbers[i]**0.5 - int(numbers[i]**0.5) == 0:
                return i
    return -1

#2.
def num_perfect_squares(numbers):
    count = 0
    for i in range(0, len(numbers)):
        if numbers[i] < 0:
            continue
        if (numbers[i] ** 0.5 - int(numbers[i] ** 0.5)) == 0:
            count = count + 1
    return(count)

#3.
def second_largest(lst):
    # Define the largest one(fst) and second largest one(snd) among the first two items.
    if (lst[0] < lst[1]):
        fst = lst[1]
        snd = lst[0]
    else:
        fst = lst[0]
        snd = lst[1]

    # Check the other items.
    for i in range(2, len(lst)):
        if snd >= lst[i]:  # If the item is smaller than 'second largest one(snd)', continue
            continue

        elif fst >= lst[i] > snd:  # If the item is smaller than 'The largest one(fst)'
            snd = lst[i]  # and bigger than 'second largest one(snd)'
            # then, assign item to snd
        else:
            snd = fst  # If the item is bigger than 'The largest one(fst)'.
            fst = lst[i]  # Therefore, the item becomes 'fst' and existed 'fst' becomes 'snd'.

    return snd  # Return the second largest one(snd).



#4.
# print french for the numbers between lo and hi (inclusive)
def print_french(lo, hi):
    for i in range(lo, hi + 1):
        print(i, " \t: ", num_in_french(i))


def digit(num, pos):
    return (num // 10 ** (pos - 1)) % 10


def num_in_french(num):  # assumes 0 <= num <= 100

    ones_list = ["zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept",
                 "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze",
                 "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]

    tens_list = ["", "dix", "vingt", "trente", "quarante", "cinquante",
                 "soixante", "soixante", "quatre-vingt", "quatre-vingt"]

    if not (0 <= num <= 100):
        return ("The given number: ", num, "is out of bound. Try again!")

    # Part 1: get the ones and tens digits of num
    one_val = digit(num, 1)
    ten_val = digit(num, 2)
    hundred_val = digit(num, 3)

    # Part 2: fill in code below for numbers 1, 2, 3, ..., 19 and 100
    if hundred_val == 1:
        return ("cent")
    if ten_val < 2:
        return (ones_list[num])

    # Part 4: case when the numbers are 70, 71, 72,...79, and 90, 91, 92,...99
    if (ten_val == 7 or ten_val == 9):
        if num == 71:
            return (tens_list[7] + " et onze")
        if num == 91:
            return (tens_list[9] + "-onze")
        #
        irregular = ["dix", " ", "douze", "treize", "quatorze",
                     "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
        return (tens_list[ten_val] + "-" + irregular[one_val])

    # Part 5: otherwise the case when the numbers are 20, 30, 40, ...
    if one_val == 0:
        if ten_val == 8:
            return (tens_list[ten_val] + "s")
        return (tens_list[ten_val])  # does 70, 90 not conflict?

    # Part 6: otherwise the case when the numbers are 21, 31, 41, ...
    if one_val == 1:
        if ten_val == 8:
            return (tens_list[ten_val] + "-un")
        return (tens_list[ten_val] + " et un")

    # Part 7: everything else, the most general case for 22, 23, ... 29,
    #           32, 33, ..., 39, 42, ...

    return (tens_list[ten_val] + "-" + ones_list[one_val])
