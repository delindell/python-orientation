planet_list = ["Mercury", "Mars"]
more_planets = (['Jupiter', 'Saturn'])
planet_list.append(more_planets)
planet_list.extend(['Uranus', 'Neptune'])
planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')
planet_list.append('Pluto')

rocky_planets = planet_list[0:4]

planet_list.__delitem__(7)
