import random

avaliableDestinations = {
    'Los Angeles': 'United States',
    'Las Palmas': 'Spain',
    'New York': 'United States',
    'Miami': 'United States',
    'Stockholm': 'Sweden',
    'Copenhagen': 'Denmark',
    'London': 'United Kingdom'
}

# countries = avaliableDestinations.value()
# destinations = avaliableDestinations.keys()


class Airport:
    def __init__(self, name, travelers, gate, helicopters=12):
        self.name = name
        self.travelers = travelers
        self.helicopters = helicopters
        self.gate = gate

    def gate_announcement(self):
        print(f'All travelers to {self.destination} go to gate!')
        print('Due to the virussituation all passangers need to use facemasks')

    def showTravelers(self):
        travelers = random.randint(222, 1222)
        print(travelers)

# gate_announcement() = ga


print(avaliableDestinations)

i1 = input(
    'Enter your desired destination and country  (destination, country)  \n:')

# e_kv(i1)
# avaliableDestinations['countries'].append(i1)
# avaliableDestinations['destinations'].append(i1)
