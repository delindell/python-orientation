showroom = {'Mustang', 'Viper', 'Sportage', 'Civic'}
print(len(showroom))

showroom.add('Mustang')
print(showroom)


new_cars = {'Bronco', 'Yaris', 'Mustang'}
showroom.update(new_cars)
print(showroom)

showroom.discard('Bronco')
print(showroom)

junkyard = {'Accord', 'F-150', 'Silverado', 'Yaris', 'Mustang'}
cars_in_both = junkyard.intersection(showroom)
print(cars_in_both)

car_union = junkyard.union(showroom)
print(car_union)

car_union.discard('Silverado')
print(car_union)
