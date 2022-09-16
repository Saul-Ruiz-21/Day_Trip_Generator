destinations = ['Japan', 'Russia', 'France', 'England']
restaurants = ['Steak house', 'Hibachi grill', 'BBQ', 'brewhouse']
entertainments = ['Arcade', 'Skyzone', 'Zoo', 'Ziplines']
transportations = ['Bike', 'Bus', 'Car', 'Helecopter']

import random

def random_destination():
    destination = 'Destination: ' + (random.choice(destinations))
    print(destination)
    return destination

def random_restaurants():
    restaurant = 'Restaurant: ' + (random.choice(restaurants))
    print(restaurant)
    return restaurant

def random_entertainment():
    entertainment = 'Entertainment: ' + (random.choice(entertainments))
    print(entertainment)
    return entertainment

def random_transportation():
    transportation = 'Transportation: ' + (random.choice(transportations))
    print(transportation)
    return transportation

def trip_lists():
    destination = random_destination() 
    restaurant = random_restaurants()
    entertainment =  random_entertainment()
    transportation = random_transportation()
    return [destination, restaurant, entertainment, transportation]



def not_satisfactory_trip():
    trip = trip_lists()
    question = input('Are you satified with this trip? ')
    while question == 'No':
        re_pick = input("Which option would you like to change? ")
        if re_pick == 'Destination':
            re_destination = trip + list(random_destination())
            return re_destination
        elif re_pick == 'Restaurant':
            return trip + list(random_restaurants()) 
        elif re_pick == 'Entertainment':
            return trip + list(random_entertainment())
        elif re_pick == 'Transportation':
            return trip + list(random_transportation())
        






















def run_trip_generator():
    not_satisfactory_trip()

run_trip_generator()