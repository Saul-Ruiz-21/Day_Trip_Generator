destinations = ['Japan', 'Russia', 'France', 'England']
restaurants = ['Steak house', 'Hibachi grill', 'BBQ', 'brewhouse']
entertainments = ['Arcade', 'Skyzone', 'Zoo', 'Ziplines']
transportations = ['Bike', 'Bus', 'Car', 'Helecopter']

import random

def random_destination():
    destination = 'Destination: ' + (random.choice(destinations))
    return destination

def random_restaurants():
    restaurant = 'Restaurant: ' + (random.choice(restaurants))
    return restaurant

def random_entertainment():
    entertainment = 'Entertainment: ' + (random.choice(entertainments))
    return entertainment

def random_transportation():
    transportation = 'Transportation: ' + (random.choice(transportations))
    return transportation

def trip_lists():
    destination = random_destination() 
    restaurant = random_restaurants()
    entertainment =  random_entertainment()
    transportation = random_transportation()
    return [destination, restaurant, entertainment, transportation]

def display_lists(options):
    for words in options:
        print(words)

trip = trip_lists()


def not_satisfactory_trip():
    question = input('Are you satified with this trip? ')
    while question == 'No':
        re_pick = input("Which option would you like to change? ")
        if re_pick == 'Destination':
            trip[0] = random_destination()
            display_lists(trip)
            question = input('Are you satified with this trip? ')
        elif re_pick == 'Restaurant':
            trip[1] = random_restaurants()
            display_lists(trip)
            question = input('Are you satified with this trip? ')
        elif re_pick == 'Entertainment':
            trip[2] = random_entertainment()
            display_lists(trip)
            question = input('Are you satified with this trip? ')
        elif re_pick == 'Transportation':
            trip[3] = random_transportation()
            display_lists(trip)
        
            
        

def satisfactory_trip():
    print('This is your final trip ')
    display_lists(trip)        

            
            
        






















def run_trip_generator():
    display_lists(trip)
    not_satisfactory_trip()
    satisfactory_trip()
    
run_trip_generator()