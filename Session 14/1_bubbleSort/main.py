from linkedlist import Flightlist
from object_sort import Flight

f1 =  Flight(carrier='indigo',
                 flight_code='6E60',
                 source='Delhi',
                 destination='Mumbai',
                 duration='05.50',
                 departure='02.30',
                 arrival='08.20',
                 fare=6489)

f2 = Flight(carrier='air india',
                flight_code='AI203',
                source='Delhi',
                destination='Mumbai',
                duration='01.45',
                departure='07.10',
                arrival='08.55',
                fare=4820)
                
f3 = Flight(carrier='vistara',
                flight_code='UK611',
                source='Bengaluru',
                destination='Kolkata',
                duration='02.35',
                departure='12.00',
                arrival='14.35',
                fare=5795)


flightlist = Flightlist()
flightlist.add(f1)
flightlist.add(f2)
flightlist.add(f3)


f2.show()