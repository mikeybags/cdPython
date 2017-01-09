#program simulating 1000 coin tosses

def coin_toss():
    heads = 0
    tails = 0
    for num in range(1,5001):
        import random
        random_num = random.random()
        print "Attempt # " + str(num) + ": Flipping a coin...",
        if round(random_num) == 0:
            heads += 1
            face = "heads"
        else:
            tails += 1
            face = "tails"
        print "It's " + face + "! ... The count is " + str(heads) + " for heads and " + str(tails) + " for tails."
    print "Ending the program, thank you!"

coin_toss()
