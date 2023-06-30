def find_pythagorean_triplets(nums):
    n = len(nums)
    triplets = []
    squares = set([num * num for num in nums])

    for i in range(n - 1):
        for j in range(i + 1, n):
            sum_of_squares = nums[i] * nums[i] + nums[j] * nums[j]
            if sum_of_squares in squares:
                triplets.append((nums[i], nums[j], int(sum_of_squares ** 0.5)))

    return triplets


# Example usage
numbers = [3, 4, 5, 6, 8, 10, 12, 15, 18, 20]
triplets = find_pythagorean_triplets(numbers)
for triplet in triplets:
    print(triplet)

print(20**2)


# Pythogorean triplet
def find_py_triplets(n):
    len_of_n = len(n)
    lis = []
    l = set([num * num for num in n])
    for i in range(len_of_n - 1):
        for j in range(i+1, len_of_n):
            sq_of_nums = n[i]*n[i] + n[j]*n[j]
            if sq_of_nums in l:
                lis.append((n[i], n[j], int(sq_of_nums ** 0.5)))
    return lis


# print(find_py_triplets([1, 2, 3, 4, 5, 6, 7, 8]))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lis = find_py_triplets(numbers)
for s in lis:
    print(s)


# Palindrome

def palindrome_words(letter):
    l = "".join(letter.split())
    if l == l[::-1]:
        return True


palindrome_words('rotor')


# Program to find the version of the python that I'm using

import sys
import datetime
print(sys.version)
print(datetime.datetime.now())


# Find Area of the circle
import math
r = 1.1
area = math.pi*(r ** 2)
print(area)

# Print reverse name

first_name = 'Yaswanthi'
last_name = 'Dwarampudi'
print(last_name[::-1] + " " + first_name[::-1])

# Accepts a couple of numbers and converting them into list and tuple

num = 1, 2, 3, 4, 5
print("list: ", list(num))
print("tuple: ", tuple(num))


# Accept a fine name and print the extension of the file given

file_name = 'abc.py'
print("Extension is: ", str(file_name.split('.')[1]))


# Display 1st and last colors/items from the list

ls = ["Red", "Blue", "Green"]
print(ls[0], "&", ls[-1])


# Display examination date

exam_date = '11, 12, 2014'
print("/".join(exam_date.split(',')))


# Add the integers in the given format

n = 10
s1 = str(n)*2
s2 = str(n)*3
print(int(n) + int(s1) + int(s2))

