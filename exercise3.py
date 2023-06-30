# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
def lesser_even(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)


print(lesser_even(9, 7))


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True
# if both words begin with same letter

def animal_crackers(word):
    w1, w2 = word.split(' ')
    s1 = w1.lower()
    s2 = w2.lower()
    if s1[0] == s2[0]:
        return True
    else:
        return False


print(animal_crackers('Pink penguin'))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
def makes_twenty(n1, n2):
    if (n1 + n2 == 20) or (n1 == 20 or n2 == 20):
        return True
    else:
        return False


print(makes_twenty(20, 10))


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    # na1 = name[0].capitalize()
    # na2 = name[3].capitalize()
    # name_split_1 = name[1:3]
    # name_split_2 = name[4:len(name)]
    # return na1 + name_split_1 + na2 + name_split_2
    if len(name) <= 3:
        return name[:3].capitalize()
    elif len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Enter a name whose length is greater than '


print(old_macdonald('ABCDEFGH'))
print(old_macdonald('macdonald'))
print(old_macdonald('one'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    return ' '.join(text.split()[::-1])


print(master_yoda('I am ready'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200


def almost_there(number):
    if (abs(100 - number) <= 10) or (abs(200 - number) <= 10):
        return True
    else:
        return False


print(almost_there(300))


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def find_33(numbers):
    for i in range(0, len(numbers) - 1):
        if numbers[i] == 3 and numbers[i + 1] == 3:
            return True
    return False


print(find_33([1, 2, 3, 4, 4]))


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(s):
    result = ''
    for i in s:
        result += i * 3
    return result


print(paper_doll('One'))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally,
# if the sum (even after adjustment) exceeds 21, return 'BUST'


def black_jack(a, b, c):
    if (1 <= a <= 11) and (1 <= b <= 11) and (1 <= c <= 11):
        if a + b + c <= 21:
            return a + b + c
        elif a + b + c > 21 and (
                a == 11 or b == 11 or c == 11):  # can also write condition as elif sum((a,b,c)) <=31 and 11 in (a,b,c):
            return (a + b + c) - 10
        elif (a + b + c) > 21:
            return 'BUST'
    return 'Pick a number in between 1 and 11'


print(black_jack(5, 6, 7))
print(black_jack(9, 9, 9))
print(black_jack(9, 9, 11))
print(black_jack(10, 20, 30))


# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9).Return 0 for no numbers.


def summer_69(arr):
    add = True
    total = 0
    for i in arr:
        while add:
            if i != 6:
                total += i
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([1, 2, 6, 1, 9, 3, 6, 2, 9]))


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order


def spy_game(lis):
    code = [0, 0, 7, 'x']
    for i in lis:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


print(count_primes(200))

































































































































































