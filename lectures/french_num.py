def print_french(low, hi): # inclusive
    for i in range(low, hi + 1):
        print(i, num_in_french(i))

def digit(num, pos):
    return (num // 10**(pos-1)%10)

def num_in_french(num): # assumes 0 <= num <= 100

    ones_list = ["zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept",
                 "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze",
                 "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]

    tens_list = ["", "dix", "vingt", "trente", "quarante", "cinquante",
                 "soixante", "soixante", "quatre-vingt", "quatre-vingt"]

    if not (0 <= num <= 100):
        return ("Out of range! Try again")

    # part1: get the ones and tens digits of num
    digit_one_val = digit(num, 1)
    digit_ten_val = digit(num, 2)
    digit_hundred_val = digit(num, 3) # only 100 goes to 1, otherwise 0

    # part2
    if digit_hundred_val == 1:
        return ("cent")

    if digit_ten_val <2:
        return (ones_list[num])

    # part4: 70, 71...,79 and 90,91,...,99
    if digit_ten_val == 7 or digit_ten_val == 9:
        if num == 71:
            return (tens_list[7] + " et onze")
        if num == 91:
            return (tens_list[9] + "-onze")

        irregular = ["dix", " ", "douze", "treize", "quatorze",
                     "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]

        return (tens_list[digit_ten_val] +"-"+ irregular[digit_one_val])

    # part5: 20, 30, 40..
    if digit_one_val == 0:
        if digit_ten_val == 8:
            return (tens_list[8] + "s")

        elif digit_ten_val not in [7,9]:
            return (tens_list[digit_ten_val])

    # part6
    if digit_one_val == 1:
        if digit_ten_val == 8:
            return (tens_list[8] + "-un")

        elif digit_ten_val not in [7,9]:
            return (tens_list[digit_ten_val] + " et un")

    # par7
    return (tens_list[digit_ten_val] + "-" + ones_list[digit_one_val])

print_french(-2, 101)
