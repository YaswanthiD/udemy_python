# eg = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# from random import shuffle
# shuffle(eg)
# print(eg)

# Let's import a module called random with shuffle method
from random import shuffle
# let's make a list of 2 empty places and 1 with a red ball
guess_list = ['O', ' ', ' ']


# define a function to shuffle the list
def shuffle_guess_list(guess_list):
    shuffle(guess_list)
    return guess_list


# print(shuffle_guess_list(guess_list))


# define a function for player to guess where the red ball is ?
# arised ques:- why don't we use direct integer over here
# The solution is if guess would be the integer, then it should be assigned with 0
# we have 0 as an index in the list so if we assign it as 0 then the input should directly take the 0 and
# no input will be taken by the user itself
# That is the reason why were assigning an empty string to the guess and after taking user input we were again
# converting it to integer
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number in between 0, 1, 2 :- ')
    return int(guess)


# print(player_guess())

# Let's check the user's guess
def check_guess(shuffle_guess_list, guess):
    if guess_list[guess] == 'O':
        print('Correct guess')
        print(guess_list)
    else:
        print('Better luck next time!!')
        print(guess_list)


# shuffling the list
mixed_list = shuffle_guess_list(guess_list)

# Get user's guess
guess = player_guess()

# Check user's guess
check_guess(mixed_list, guess)









