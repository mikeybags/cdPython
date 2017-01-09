def odd_even():
    for count in range (1, 2001):
        if (count % 2 == 0):
            print "Number is {}. This is an even number.".format(count)
        elif (count % 2 != 0):
            print "Number is {}. This is an odd number.".format(count)

odd_even()

''' alternative way of printing

print "Number is " + str(count) + ".This is an ____ number"
