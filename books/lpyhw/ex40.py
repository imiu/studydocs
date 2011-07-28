cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    """docstring for find_city"""
    if  state in themap:
        return themap[state]
    else:
        return "Not found"

cities['_find'] = find_city

for city in cities:
    print city

while True:
    print "State? (Enter to quit)"
    state = raw_input("> ")

    if not state:
        break

    city_found = cities['_find'](cities, state)
    print city_found
