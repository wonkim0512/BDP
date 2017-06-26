# palindrome checker

def palindrome():
    string = raw_input("Enter the sentence what you want to chech palindrome:")
    if string == string[-1::-1]:
        print "It is palindrome!"

    else:
        print "It is not palindrome"

palindrome()
