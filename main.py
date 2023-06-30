# Formatted string literals

a = 'Yaswanthi'
print(f'Hii my name is {a}')  # we can also write the formatted strings like this

print('Hii my name is {}'.format(a))  # another way of formatting method

#  or we can also do this

print('Hii my name is {name}'.format(name='Yaswanthi'))

#  Float formatting "{value:width.precision f}" => {r:3.3f}
#  Here 3 is the number for width which takes place after is
#  3f is the floating point to how many decimal points we gonna markup

a = 20/3
print("The answer is {r:3.3f}".format(r=a))

dic = {"k1": ['a', 'b', 'c']}
# my_list = dic["k1"]
# letter = my_list[2]
# print(letter.upper())
# instead of doing all the above steps we can do the below step
print(dic["k1"][2].upper())
# To insert another key value pair in the dictionary
# dic['k2'] = ['d', 'e', 'f']
dic['k1'][1] = ['d']
print(dic)


#  tuples

tup = (1, 2, 3)
lis = [1, 2, 3]
tupp = tup + tuple(lis)
print(tupp)
print(tup[0])
print(tupp.count(1))
print(tupp.index(2))
#  tup[1] = 'one'
#  print(tup) # Tuple don't support item assignment


# Sets  => Set is an unordered collection of unique elements.
# set is defined with curly braces


my_set2 = {2, 3, 2, 3, 4, 4}
my_set3 = my_set2.add(1)
print(my_set3)


# I/O files

my_file = open('test.txt')
content = my_file.read()
content1 = my_file.readlines()
# print(content)  # In jupyter notebook when we try to read this file again this would not show us the result
#  and then if we reset it, and again if we read the file again we may get the o/p again
# to reset, the command we have to use is filename.seek(0)

myfile = my_file.close()
print(myfile)

# The below codes to

# with open('my_new_file.txt',mode = 'r') as f:
#     print(f.read())

# Exercise
dic = {
    'k1': [1, 2, {
        'k2': ['this is tricky', {
            'tough': [1, 2, ['hello']]
        }]
    }]
}
d = dic['k1'][2]['k2'][1]['tough'][2][0]
print(d)


# Exercise

a = (100/5)*(2**2)+40.25-20
print(a)

list3 = [1, 2, [3, 4, 'hello']]
l = list3[2][2]
print(l)

list4 = [5, 6, 3, 4, 8, 1]
print(sorted(list4))
print(list4.sort())

print(4**0.5 == 2)


#  If, elif, else
# Small project using python if, elif and else statements
"""receiver = input("Heey, there i'm here to help you. \nLet me know what do you want to EAT ?? Biryani or Ice cream ")
conformer = input("Is it a hot day or cold day ?? Press 'H' for Hot or 'C' for Cold ")

if receiver.lower() == 'biryani' and conformer.lower() == 'h':
    print("It's HOT today, so it's better to eat less masala food and drink plenty of water to get hydrated.\n"
          "Use Raita in biryani and i suggest you to drink buttermilk.")
elif receiver.lower() == 'biryani' and conformer.lower() == 'c':
    print("You can eat masala food and even though it's a cool day try to drink enough water to stay hydrated.\n"
          "Use Raita in biryani so that the masala that you have taken won't effect your stomach.")
elif receiver.lower() == 'ice cream' and conformer.lower() == 'h':
    print("It's ok to eat ice cream.")
elif receiver.lower() == 'ice cream' and conformer.lower() == 'c':
    print("We won't suggest you to eat ice cream, because it's cool today.\n"
          "If you eat more ice cream there is a much chance to get cold, fever or cough.\n"
          "So, better to avoid ice cream. Take care of yourself. Thank you ☺️")
else:
    print('Please enter the correct options..')"""


# for loop

"""
my_name = 'Yaswanthi'
for i in my_name:
    if i == 's':
        print('S')
    else:
        print(my_name)
"""

# tuple unpacking

my_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
for a,b in my_list:
    print(a)
    print(b)

my_list2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in my_list2:
    print(b)

# dictionary unpacking

my_dic = {'k1': 'one', 'k2': 'two', 'k3': 'three'}
for key, value in my_dic.items():
    print(value)

#  for loops
my_name = 'Yaswanthi'

result = ''

for letter in my_name:
    if letter == 's':
        result += 'S'
    else:
        result += letter

print(result)

# While loops

# i = 0
# while i < 100:
#     print(i)
#     i += 10

# break, continue and pass

i = 0
while i < 10:
    print(i)
    i += 1


# print('Yaswanthi\n'*10)

# Operators in python
# range function

range_of_num = range(1, 10, 2)  # one of the better way to generate numbers
print(set(range_of_num))


index_count = 1
name = 'Yaswanthi'
for letter in name:
    print(f'Your {index_count}th letter is "{letter}" ')
    index_count += 1

# Zip method
# zip method is usually used to unpack 2 or more different lists
# and combine one list with another lists
# let's have an example

mylist1 = [1, 2, 3, 4]
mylist2 = ['a', 'b,', 'c', 'd']
mylist3 = [True, False, False, True]

for i in zip(mylist1, mylist2, mylist3):
    print(i)

# output
# (1, 'a', True)
# (2, 'b,', False)
# (3, 'c', False)
# (4, 'd', True)

#  The enumerate() function returns indexes of all items in iterables (lists, dictionaries, sets, etc.)
#  whereas the zip() function is used to aggregate, or combine, multiple iterables.

# Enumerate

name = 'Yaswanthi'
for index, letter in enumerate(name):
    print(index)
    print(letter, "\n")

# in keyword

name = 'yaswanthi'
if 'a' in name:
    print('A')

# min, max values

list1 = [1, 2, 3, 4, 5]
print(min(list1))
print(max(list1))

# random function

from random import shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(mylist)
print(mylist)


#  randint() function is used to generate the random integers between the two given numbers passed as parameters.
#  Randint is an in-built function of random library in python.

from random import randint

print(randint(1, 29))

# input function

# name = input('Enter your name:-  ')

# list comprehensions

mystring = 'yaswanthi'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)


# Another way to append items in list without using for loop and append method
naam = 'yaswanthi'
mylist9 = [letter for letter in naam]
print(mylist9)

sq_of_list = [item**3 for item in range(0, 11)]
print(sq_of_list)

# can also perform if condition in the list itself

ifInList = [item**2 for item in range(1, 11) if item % 2 == 0]
print(ifInList)

# Conversion of Fahrenheit to Celsius

fahrenheit = [20, 98, 44, 56.7, 50]
celsius = 0
for deg in fahrenheit:
    celsius = (deg-32) * 5/9
    print(celsius)

# Celsius to Fahrenheit

celsius = [20, 98, 44, 56.7, 50]

fahrenheit = 0

for item in celsius:
    fahrenheit = (item*9/5)+32
    print(fahrenheit)

# Another way
fahrenheit = [item * 9/5 + 32 for item in celsius]
print(fahrenheit)

# item multiplication in list on different ways

l12 = []
for i1 in [20, 30, 40, 50, 10]:
    for j1 in [10, 50, 40, 30, 20]:
        l12.append(i1*j1)
        print(l12)


item_mul_in_list = [item1 * item2 for item1 in [20, 10] for item2 in [2, 3]]
print(item_mul_in_list)


list_mul = []
for i in [10, 20]:
    for j in [2, 3]:
        list_mul.append(i*j)
    print(list_mul)



























































































































































