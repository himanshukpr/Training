'''
Flight
    carrier
    flight_code
    source
    destination
    duration
    departure
    arrival
    fare
'''

class Flight:
    def __init__(self,carrier, flight_code,source,destination,duration,departure,arrival,fare):
        self.carrier = carrier
        self.flight_code = flight_code
        self.source = source
        self.destination = destination
        self.duration = duration
        self.departure = departure
        self.arrival = arrival
        self.fare = fare
        self.pre = None
        self.next = None

    def show(self):
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~{self.flight_code}~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Carrier: {self.carrier}")
        print(f"Source: {self.source} and Destination: {self.destination}")
        print(f"Duration: {self.duration}")
        print(f"Departure: {self.departure} and Arrival: {self.arrival}")
        print(f"Fare: \u20b9 {self.fare}")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



flights ='''[ 
        Flight(carrier='indigo',
                 flight_code='6E60',
                 source='Delhi',
                 destination='Mumbai',
                 duration='05.50',
                 departure='02.30',
                 arrival='08.20',
                 fare=6489),
        Flight(carrier='air india',
                flight_code='AI203',
                source='Delhi',
                destination='Mumbai',
                duration='01.45',
                departure='07.10',
                arrival='08.55',
                fare=4820),
        Flight(carrier='vistara',
                flight_code='UK611',
                source='Bengaluru',
                destination='Kolkata',
                duration='02.35',
                departure='12.00',
                arrival='14.35',
                fare=5795),
        Flight(carrier='spicejet',
                flight_code='SG154',
                source='Hyderabad',
                destination='Jaipur',
                duration='02.50',
                departure='16.15',
                arrival='19.05',
                fare=5060),
        Flight(carrier='go first',
                flight_code='G8189',
                source='Ahmedabad',
                destination='Pune',
                duration='01.40',
                departure='10.25',
                arrival='12.05',
                fare=4380)
]

# found = False
# flight_code = input('enter code of flight you want to search: ')

# for index in range(len(flights)):
#     if flights[index].flight_code == flight_code:
#         flights[index].show()
#         found = True
#         break

# if found == False:
#     print("not found")


source = input('source: ')
destination = input('destination: ')
found = False
for index in range(len(flights)):
    if flights[index].source == source and flights[index].destination == destination:
        flights[index].show()
        found = True


if found == False:
    print(f'from: {source} and to: {destination} not found')
        
'''