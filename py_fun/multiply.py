# This function will take in a list and a second parameter, and multiply each number in the list by that second parameter, and return a new list with that information

a = [2, 4, 10, 16]

def mult_list(list, mult_by):
    new_list = []
    for num in list:
        new_list.append(num * mult_by)
    return new_list

b = mult_list(a, 5)
print b


'''alternative (based on answer sheet)
def mult_list(arr, mult_by):
    for i in range(len(arr)):
        arr[i] = arr[i] * mult_by
    return arr
'''
