def test_grade():
    for num in range(1, 11):
        print "Please input your score for test number " + str(num) + ":",
        score = input()
        if score > 90:
            print "Your grade is A"
        elif score > 80:
            print "Your grade is B"
        elif score > 70:
            print "Your grade is C"
        elif score > 60:
            print "Your grade is D"
        else:
            print "Your grade is F"
    print "End of the program. Bye!"

#test_grade()


# alternative method
def test_grade_2():
    for num in range(1,11):
        print "Please input your score for test number " + str(num) + ":",
        score = input()
        if score > 90:
            grade = "A"
        elif score > 80:
            grade = "B"
        elif score > 70:
            grade = "C"
        elif score > 60:
            grade = "D"
        else:
            grade = "F"
        print "Score: %d; Your grade is %s"%(score, grade)
    print "End of the program. Bye!"

test_grade_2()
