# (14) Simulaton in Python
# Random Number Generation
current_x = 0
def prng_seed(s):
    global current_x
    current_x = s

def prng1(n):
    return (n+7)%12


def prng():
    global current_x
    current_x = prng1(current_x)
    return current_x


import random

print(random.randint(0, 150110))
print(random.random())
rand_lst = [random.randrange(1,101) for i in range(10)]
print(rand_lst)
choice = [random.choice(rand_lst) for i in range(5)]
print(choice)
print("*",random.choice(rand_lst),"*")
random.shuffle(choice)
print(choice)
for i in range(10):
    print(random.randrange(1788, 2012, 4))

'''
def roll():
    roll = prng()%6 + 1
    assert 1<= roll <= 6
    return roll

def dice_game():
    strikes = 0
    winnings = 0
    while strikes < 3:
        die1 = roll()
        die2 = roll()
        if die1 == die2:
            strikes += 1
        else:
            winnings += (die1 + die2)
    return winnings

def average_winnings(runs):
    total = 0
    for n in range(runs):
        total += dice_game()
    return total/runs

print([round(average_winnings(10),2) for i in range(5)])
'''

from random import shuffle
def student(pairs, samples):
    num_correct = 0
    matching = list(range(pairs))
    for i in range(samples):
        shuffle(matching)
        for j in range(pairs):
            if matching[j] == j:
                num_correct += 1
    return num_correct/samples

print(student(2, 100))
print(student(5, 1000))
print(student(20, 10000))
