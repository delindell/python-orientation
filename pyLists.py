import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6)) 

print(my_randoms)
# Generate a list of numbers 1...10
numbers_1_to_10 = range(1 , 11)

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = True
    for random_number in my_randoms:
        if random_number == number:
            print(f'{number} is in the random list')
