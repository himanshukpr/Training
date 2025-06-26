
"""
oops - object oriented programing

in real world:
    object
        anything or real thing which contains some attibutes or some behaviour is called the object
        a real thing
        an entity
    class
        drawing of an object

    Principle of oops
        1. think about the object
        2. create its representation i.w. class
        3. from class create a real object

in computer science
    object
        is a storage container (box)
        which we can customize as per out requirements

    class
        textual representation of the object
        i.e we code to create a class
"""

"""
one_way_flight_booking
    from
    to
    departure_day
    travelers
"""

class one_way_flight_booking:
    def __init__(self,from_location, to, departure_day, travelers):
        self.from_location =from_location
        self.to =to
        self.departure_day =departure_day
        self.travelers = travelers
        
    def display(self):
        print("from location:", self.from_location)
        print("to location:", self.to)
        print("departure day:", self.departure_day)
        print("travelers:", self.travelers)


obj = one_way_flight_booking('delhi','pune','28-june-2025',3)
obj.display()