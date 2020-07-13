zoo = ('Raccoon', 'Dog', 'Cat', 'Bird', 'Alligator', 'Kangaroo', 'Turtle', 'Sloth', 'Chimpanzee', 'Squirrel')

print(zoo.index('Dog'))

animal_to_find = 'Cat'
if animal_to_find in zoo:
    print(animal_to_find)

(first, second, third, fourth, fifth, sixth, seventh, eighth, nineth, tenth) = zoo
print(first, second, fifth, eighth, third)
print(second, fourth, nineth, sixth, tenth)

new_zoo = list(zoo)
print(new_zoo)

new_zoo.extend(('rabbit', 'parrot', 'Siverback Gorilla'))
print(new_zoo)

new_tuple_zoo = tuple(new_zoo)
print(new_tuple_zoo)
