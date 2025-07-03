from linkelist_search import FlightList
from search_object import Flight

flight1 = Flight(carrier='indigo',
                 flight_code='6E60',
                 source='Delhi',
                 destination='Mumbai',
                 duration='05.50',
                 departure='02.30',
                 arrival='08.20',
                 fare=6489)
flight2 = Flight(carrier='air india',
                flight_code='AI203',
                source='Delhi',
                destination='Bangaluru',
                duration='01.45',
                departure='07.10',
                arrival='08.55',
                fare=4820)
flight3 = Flight(carrier='vistara',
                flight_code='UK611',
                source='Bengaluru',
                destination='Kolkata',
                duration='02.35',
                departure='12.00',
                arrival='14.35',
                fare=5795)

flightlist = FlightList()
flightlist.add(flight1)
flightlist.add(flight2)
flightlist.add(flight3)

# flightlist.search('AI203')

flightlist.filter(source='Delhi',destination='Bangaluru')