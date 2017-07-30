def first_perfect_square(alist):
    from math import sqrt
    for idx, num in enumerate(alist):
        if num == 0:
            return idx

        elif num % sqrt(num) == 0:
            return idx

    return -1

def first_perfect_square(alist):
    for idx, num in enumerate(alist):
        if num == 0:
            return idx
        elif num ** (1/2) - int(num**(1/2)) == 0: # num ** (1/2) returns float
            return idx
    return -1

print(first_perfect_square(list(range(5))))
print(first_perfect_square([2,4,6,8,10,12]))
print(first_perfect_square([6,8,10,12,9]))
print(first_perfect_square([1,1]))
print(first_perfect_square([42]))
print(first_perfect_square([]))
print("*"*20)

def num_perfect_squares(alist):
    if alist == []:
        return 0

    if alist[0] ** (1/2) - int(alist[0]**(1/2)) == 0:
        return 1 + num_perfect_squares(alist[1:])

    else:
        return num_perfect_squares(alist[1:])

print(num_perfect_squares([]))
print(num_perfect_squares([0]))
print(num_perfect_squares([0,1]))
print(num_perfect_squares(list(range(10))))
print(num_perfect_squares([3]*10))
print("*"*20)


def second_largest(alist):
    max_value = max(alist)
    alist.remove(max_value)
    return max(alist)

print(second_largest([3,-2,10,-1,5]))
print(second_largest([-2,1,1,-3,5]))
print(second_largest([1,2,3,3]))
print(second_largest(['alpha', 'gamma','beta','delta']))
print("*"*20)

'''
with  open("C:\\Users\\woni\\Desktop\\french.txt", 'r') as french:
    for line in french:
        print(line)


# print_french

print("*"*20)
# umbrella quandary problem

def umbrella(p):
    from random import random
    trip = 0
    umbrella = [1, 1]
    location = 0
    wet = False
    while (not wet):
        if random() < p:
            if umbrella[location] == 0:
                wet = True

            else:
                trip += 1
                umbrella[location] -= 1
                location = 1 -location
                umbrella[location] += 1

        else:
            trip += 1
            location = 1- location

    return trip

def test():
    p = 0.01
    trips = 0
    results = [None] * 99
    for idx in range(99):
        trips = 0
        for times in range(1000):
            trips += umbrella(p)

        results[idx] = trips/1000
        p += 0.01
    return results

probability_list = test()
for probability in range(1, 100):
    print(probability, "%:", probability_list[probability-1])
'''
