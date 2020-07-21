planet_list = ["Mercury", "Mars"]
planet_list.extend(['Jupiter', 'Saturn'])
planet_list.extend(['Uranus', 'Neptune'])
planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')
planet_list.append('Pluto')

rocky_planets = planet_list[0:4]

planet_list.__delitem__(7)

spacecraft_list = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ('Apollo', 'Venus'),
   ("Epcot", "Earth"),
   ("Droid", "Uranus"),
   ('Millenum Falcon', 'Mercury')
]

for planet in planet_list:
    for spacecraft in spacecraft_list:
        if planet == spacecraft[1]:
            print(f'{spacecraft[0]} visitied {planet}') 
