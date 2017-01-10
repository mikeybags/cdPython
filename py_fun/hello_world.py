print "Hello World!"

#single line comments can be made by using a hash
''' multi line comments can be made in between triple quotes
(either single or double)
'''

#strings and assigning variables is easy!
print "Input your first name"
first_name = raw_input()
print "Input your last name"
last_name = raw_input()
print "Your name is", first_name, last_name
#we can also print name as follows
print "Your name is {} {}".format(first_name, last_name)

print "using the .capitalize() function to capitlize the first letter of this string".capitalize()
print "THIS STRING IS WRITTEN IN ALL CAPS, BUT WILL BE CONVERTED TO LOWERCASE BY THE .LOWER() FUNCTION".lower()
print "This String Had Capital Letters At The Beginning Of Every Word, But The .Swapcase() Function Is Going To Change It".swapcase()
print "this string is written in all lowercase, but the .upper() function will convert it to all caps.".upper()
my_string = "Testing use of the .find() funtion to find the index or where the substring '.find()' is in this sentence"
print my_string
print my_string.find(".find()")
hi_string = "Hi, my name is Mike...but will it remain Mike? I think the .replace(<old>, <new>, <max>) function has other ideas. But by using the max parameter, it will only change once. "
print hi_string
print hi_string.replace("Mike", "Scott Stewarte", 1)
#lists are arrays. They are within square brackets just like other languages.
x = [1, 2, 3, 4]
print x
x.append(5)
print "After using the .append() function, our list is now ", x
x.insert(0, 0)
print "After using the .insert(<index>, <new_element<>) function, our list is now", x
x.remove(0)
print "After using the .remove(<element>) function, our list is back to ", x, ". If the element didn't exist, the .remove() function would not have worked."
x.pop()
print "Using the .pop(<optional_index>) function. With no position passed, it just pops off the last element. The list is now", x
y = [3, 2, 4, 5, 1]
print "List y is", y
y.sort()
print "After using the .sort() function, list y is now", y
print "Slicing is kind of weird. It is in the format of x[<first_index>:<last_index>]. If both indexes are left blank, the entire list is printed. If just the first index is filled in, it will print from there until the end of the list. If just the last index is provided, it will print up to (but not including) that index. If both are included, it will print from (including) the first index, to (not including) the last index."
print y[2:4]
print "Can slicing be done on strings too? Let's find out!"
print first_name[1:]
print "len() is the same as .length in jS, just formatted differently. Let's see how many characters are in first_name"
print len(first_name)
print "max() returns the largest item in a sequence. min() obviously returns the smallest. But when comparing data types, numbers < dictionaries < lists < strings < tuples"
print max(first_name)
print "any() returns true if any item in a sequence (list, dictionary, string) is true. If you have empty strings or 0's, those are false. But any other number would return true."
print "all() returns true only if all items in a sequence are true."

#if else elif...elif instead of else if, but otherwise standard.
#for loop : for <counter> in <sequence or range>:
#while loop : while <expression>:
#interesting tidbit. Else can be used in a while loop to perform an action if a condition is not met and you want to do something when that happens


'''functions
functions are known as "first class". They can go whereever they want. They can be standalone, defined inside of class/instances/methods,
passed as arguments to functions (callbacks), returned from functions (closures), anonymous (which means stored in a variable/only used once, known as lambdas)

syntax is as follows
def add(a,b):
    x = a + b
    return x
'''
