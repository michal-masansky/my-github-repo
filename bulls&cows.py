import random
from time import time

# Secret random number
def random_num(num_digits):
    lst = list(range(10))
    result = []

    if num_digits not in range(1,10):
        print('Number of digits must be between 1 nad 9' )
    else:
        for i in range(num_digits):
            if i == 0:
                num = random.choice(lst[1:])
            else:
                num = random.choice(lst)
            result.append(num)
            lst.remove(num)

    return result

# Player's guess
def enter_num(num_digits):

    mode = True

    while mode:
        result = []
        try:
            num = int(input('Enter a number: '))
        except ValueError:
            print(f'Please enter number')
        else:
            for digit in str(num):
                result.append(int(digit))
            if len(set(result)) == num_digits:
                mode = False
                continue
        print(f'Enter {num_digits}-digits number')

    return result

# Compare player's and computers number
def compare_lists(lst1,lst2):
    num_cows = 0
    num_bulls = 0

    for i,member in enumerate(lst1):
        if lst2[i] == member:
            num_bulls += 1
        elif member in lst2:
            num_cows += 1

    return (num_bulls, num_cows)

# Counting time
def time_duration(start, end):

    hours = round((end - start) // 3600)
    minutes = round(((end - start) % 3600)//60)
    seconds = round((end - start) - (hours * 3600) - (minutes * 60))

    return hours, minutes, seconds



def main():
    lst2 = random_num(4)
    num_guess = 0
    print(lst2)
    lst1 = []
    time_start = time()

    while compare_lists(lst1,lst2)[0] <  4:
        lst1 = enter_num(4)
        num_guess += 1
        print('{} bulls, {} cows'.format(*compare_lists(lst1,lst2)))

    time_end = time()

    final_time = time_duration(time_start,time_end)

    print(f"Correct, you've guessed the right number in {num_guess} guesses!")
    print('Your time is {} hours, {} minutes and {} seconds'.format(*final_time))

    return

main()



