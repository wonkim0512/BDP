def temparature():
    celsius = int(input('What is the celsius temparature?'))
    farenheit = 9/5 * celsius + 32
    print "The temparature is", farenheit, "degrees farenheit."

    if farenheit >= 90:
        print "Pretty hot"

    elif 30 <= farenheit < 90:
        print "Good."

    else:
        print "Cold!"

temparature()
