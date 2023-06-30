# (a) Use for, .split(), and if to create a Statement that will print out words that start with 's'

st = 'Print only the words that start with s in this sentence'
split_words = st.split(' ')
# print(split_words)
for items in split_words:
    if items[0] == 's':
        print(items)

# Given answer and also another way

for i in st.split():
    if i[0] == "s":
        print(i)

# (b) Use range() to print all the even numbers from 0 to 10.

for i in range(0, 10):
    if i % 2 == 0:
        print(i)

# given answer and also to keep all the numbers that are even in the list

print(list(range(1, 100)))


# (c)Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
my_list = [items for items in range(1, 50) if items % 3 == 0]
print(my_list)


# (d) Go through the string below and if the length of a word is even print "even!"
st2 = 'Print every word in this sentence that has an even number of letters'
sw = st2.split()
for items in sw:
    sw_len = (len(items) % 2 == 0)
    if sw_len:
        print('even')

# Given answer
for i in st.split():
    if len(i) % 2 == 0:
        print('even')


# (d) Write a program that prints the integers from 1 to 100.
#  But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
#  For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# (e) Use List Comprehension to create a list of the first letters of every word in the string below:
st3 = 'Create a list of the first letters of every word in this string'
sp_w = st3.split()
# print(sp_w)
my_l = [items[0] for items in sp_w]
print(my_l)

# Given answer
my_l = [i[0] for i in st.split()]



