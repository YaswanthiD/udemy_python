def my_func(name):
    print("Hello " + name)


my_func('Yaswanthi')


def my_func2(num1, num2):
    return num1+num2


print(my_func2(20, 30))


def even_odd(num):
    result = num % 2 == 0
    return "Heey it's even number", result


print(even_odd(1032))
print(even_odd(2000394783748365))


def seperating_list(num2):
    even_list = []
    odd_list = []

    # print("Heey it's an even number")
    for number in num2:
        if number % 2 == 0:
            even_list.append(number)
            # print("Heey it's an even number", number)
        else:
            odd_list.append(number)
            # print("Heey, it's an odd number", number)
    return even_list, odd_list
    # return odd_list


print(seperating_list([2, 34, 37, 23, 56, 89, 70, 66, 48, 36, 290, 568]))
# print(list_even)
# print(type(list_even))


minu = 240
hour = minu/60
print(hour)


# Tuple unpacking

tup_unpacking = [('Apple', 200), ('Google', 300), ('Microsoft', 400)]
for a, b in tup_unpacking:
    print(a)
    print(b, '\n')


# Quick check on tuple unpacking

work_hours = [('John', 20), ('Jack', 30), ('sam', 10)]


def employee_check(work_hours):
    current_hours = 0
    employee_of_month = ' '
    for employee, hours in work_hours:
        if hours > current_hours:
            current_hours = hours
            employee_of_month = employee
        else:
            pass
    return employee_of_month, current_hours


print(employee_check(work_hours))


# *args and **kwargs
# *args means when we were trying to call the parameters more than the arguments passed in the function
# then we would get an error to rectify it we have *args method
# for example we don't know how many parameters are going to call so
# instead of giving individual positional arguments we can put it as *args when passing the arguments
# so that we may call as many as parameters without passing a single argument

# example code for *args


def myfunc(*args):
    return sum(args)


print(myfunc(10, 20))


# *args returns the input as a tuple if we want to print the parameters that we have passed
# Here after the '*' we can give any name for eg:- we can call it as yash
def myfunc1(*yash):
    return yash


print(myfunc1(1, 2, 3, 4, 5, 6, 7, 8, 9, 0))


def myfunc2(*args):
    return args


print(myfunc2(1, 2, 3, 4, 5))


# **kwargs:- Keyword arguments
# These are also same as *args but the only difference is **kwargs is used for keywords
# If we print the given input then we will get the output as dictionary

def my_kwargs(**kwargs):
    return kwargs


print(my_kwargs(fruits='Apple', food='Biryani'))


def myfunc3(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {} '.format(args[0], kwargs['food']))


myfunc3(10, 20, 30, fruit='orange', food='eggs', animal='dog')

# a = input()
# ls = []
# for i in a:
#     ls.append(i)
# print(ls)

# def myfunc9(a):
#     for i in b:
#         for j in i:
#             if j % 2 == 0:
#                 return i.upper()
#             else:
#                 return i.lower()
#
#
# print(myfunc9(a))



# Map in Python is a function that works as an iterator to return a result after applying a function
# to every item of an iterable (tuple, lists, etc.). It is used when you want to apply a single transformation
# function to all the iterable elements. The iterable and function are passed as arguments to the map in Python.
def sq_nums(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in map(sq_nums, my_nums):
    print(i)
print(list(map(sq_nums, my_nums)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]


names = ['Satish', 'Loves', 'Yaswanthi']
print(list(map(splicer, names)))


# filter function
# Filter() is a built-in function in Python.
# The filter function can be applied to an iterable such as a list or a dictionary and create a new iterator.
# This new iterator can filter out certain specific elements based on the condition that you provide very efficiently.
# in Filter and map functions we can stop calling function parameters at the end of the function
# we can give call the parameters in the loop itself or while attaching it in the list itself.


def check_even(num):
    return num % 2 == 0


for i in filter(check_even, [1, 2, 3, 4, 5, 6]):
    print(i)

print(list(filter(check_even, [1, 2, 3, 4, 5])))

# Lambda expressions


def square(num): num ** 2


print(square(20))  # we can also def a function like this in short terms


result = lambda num: num ** 2  # Or we can use lambda function to get it in simpler way

print(result(10))


print(list(map(lambda num: num ** 2, my_nums)))
print(list(filter(lambda num: num % 2 == 0, my_nums)))
print(list(map(lambda mystring: mystring[0], names)))


# Nested statements and scope

x = 25


def printer():
    x = 50
    return x

print(printer())
print(x)

# LEGB
# L: Local
# E: Enclosing function locals
# G: Global
# B: Built-in
name = 'Yaswanthi'


def greet():
    name = 'Sam'

    def hello():
        print('Hello ' + name)

        hello()


print(greet())

# calling both local variable and global variable

x = 10


def func(x):
    print(f'X is {x}')

    x = 200
    print(f'I just locally changed X to {x}')


func(x)






























