# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

# TODO define the fucntion with a param
# TODO 

def countdown(number):
# TODO create a list
    the_list = []
    for something in range(number, -1, -1):
        the_list.append(something)
        print(something)
    return(the_list)

# TODO counter variable
# TODO return the list 

# TODO call the fuction:

# print(countdown(5)) # [5,4,3,2,1,0]


# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(the_list):
    print(the_list[0])
    return the_list[1]
    

# print(print_and_return([1,2]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(the_list):
    print(the_list[0][1])
    # return the_list[0] + len(the_list)
    pass

# print(first_plus_length([[1,2,3],4,5])) # 6

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]

def values_greater_than_second(the_list):
    if len(the_list) < 2:
        return False
    new_list = []
    second_el = the_list[1]
    for i in the_list:
        if i > second_el:
            new_list.append(i)
    return new_list
        
        


# print(values_greater_than_second([5,2,3,2,1,4])) # [5,3,4]
# print(values_greater_than_second([5])) # False


# Example: values_greater_than_second([3]) should return False


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(size, value):
    the_new_list = []
    # the_new_list.append([value] * size)
    # print(the_new_list)
    return [value] * size
    # for i in range(size):
    #     the_new_list.append(value)
        
    # return the_new_list
        
    


print(length_and_value(4,7)) #should return [7,7,7,7]
print(length_and_value(6,2)) #should return [2,2,2,2,2,2]

