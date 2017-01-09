'''x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(list):
    stars = ""
    for num in list:
        count = num
        while count > 0:
            stars += "*"
            count -= 1
        print stars
        stars = ""

draw_stars(x)
'''
#part 2
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars_2(list):
    stars = ""
    string = ""
    for i in list:
        if i >= 0 and i <= 9:
            count = i
            while count > 0:
                stars += "*"
                count -= 1
            print stars
            stars = ""
        else:
            count = len(i)
            while count > 0:
                string += i[0:1].lower()
                count -= 1
            print string
            string = ""

draw_stars_2(y)

#answer sheet method. Stop repeating yourself!

y = [4,'Tom',1,'Michael',5,7,'Jimmy Smith']
def draw_stars2(my_list):
    for item in my_list:
        output = ''
        if type(item) is int:
            for i in range(item):
                output += '*'
        elif type(item) is str:
            first_letter = item[0].lower()
            for i in range(len(item)):
                output += first_letter
        print output

draw_stars2(y)
