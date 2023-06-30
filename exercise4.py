# Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    rad = (4/3) * 3.14 * rad ** 3
    return rad


print(vol(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def high_low(num, low, high):
    result = low < num < high
    return f'{num} is in the range between {low} and {7}'


print(high_low(5, 2, 7))


def high_low_bool(num, low, high):
    result = low < num < high  # we can also use range function
    return result


print(high_low_bool(5, 2, 7))


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def count_letters(string):
    lower_case = 0
    upper_case = 0
    for i in string:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
        else:
            pass
    print(f'sample string: {string}')
    print(f'upper case letters: {upper_case}')
    print(f'lower case letters: {lower_case}')


count_letters('Hello World')


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lis):
    return list(set(lis))


print(unique_list([1, 2, 3, 2, 3, 3, 2, 3, 4, 3, 4, 3, 3, 4, 3, ]))


# Write a Python function to multiply all the numbers in a list.

def multiply_nums(lis):
    res = 1
    for i in lis:
        res *= i
    return res


print(multiply_nums([1, 2, 3, -4]))


# Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
# e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the
# .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a
# string in Python, there are some clever ways to do it with slicing notation.


def is_palindome(s):
    s = s.replace(' ', '')

    return s == s[::-1]


print(is_palindome('ono ono'))


import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    print(alphaset)
    str1 = str1.replace(' ', '')
    print(str1)
    str1 = str1.lower()
    print(str1)
    str1 = set(str1)
    print(str1)
    return str1 == alphaset


print(ispangram("The quick brown fox jumps over the lazy dog"))



l, b, h = input()
area = 2 * (int(l) + int(b)) * int(h)
print(area)
























