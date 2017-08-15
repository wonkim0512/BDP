# module.py

def sum(a, b):
    return a+b

def mul(a, b):
    return a*b

def safe_sum(a,b):
    if type(a) != type(b):
        print("Not operand type!")
        return

    else:
        return sum(a,b) # Why do i need 'return' here?


if __name__ == "__main__":
    print(sum(2, 4))
    print(mul(2, 4))
