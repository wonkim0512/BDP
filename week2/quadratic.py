import math
def quadratic():
    print 'This program finds the real solutions to a quadratic\n'
    a, b, c = eval(raw_input("Please enter the coefficients (a, b, c):")) #python2: raw_input, python3: input
    discrim = b**2 - 4*a*c

    if discrim < 0 :
        print "The equation has no real roots!"

    elif discrim == 0:
        double_root = -b /(2*a)
        print "The equation has double root at ", double_root

    else:
        discroot = math.sqrt(discrim)
        root1 = (-b+discroot) / 2*a
        root2 = (-b-discroot) / 2*a
        print "The solutions are", root1, root2

quadratic()
