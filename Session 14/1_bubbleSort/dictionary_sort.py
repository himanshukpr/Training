flights = [{
    'carrier': 'indigo',
    'flight_code': '6E60B',
    'from': 'Delhi',
    'to': 'Mumbai',
    'duration': '05.50',
    'departure': '02.30',
    'arrival': '08.20',
    'fare': 6489
},{
    'carrier': 'air india',
    'flight_code': 'AI101',
    'from': 'Mumbai',
    'to': 'Bengaluru',
    'duration': '02.10',
    'departure': '09.45',
    'arrival': '11.55',
    'fare': 5340
},{
    'carrier': 'vistara',
    'flight_code': 'UK923',
    'from': 'Hyderabad',
    'to': 'Delhi',
    'duration': '02.30',
    'departure': '06.15',
    'arrival': '08.45',
    'fare': 5899
},{
    'carrier': 'spicejet',
    'flight_code': 'SG407',
    'from': 'Kolkata',
    'to': 'Chennai',
    'duration': '02.55',
    'departure': '14.10',
    'arrival': '17.05',
    'fare': 4725
},{
    'carrier': 'go first',
    'flight_code': 'G8712',
    'from': 'Pune',
    'to': 'Jaipur',
    'duration': '03.15',
    'departure': '19.30',
    'arrival': '22.45',
    'fare': 5030
}]


for i in range(len(flights)-1):
    for j in range(len(flights)-i-1):
        if flights[j]['fare'] > flights[j+1]['fare']:
            temp =  flights[j]
            flights[j] = flights[j+1]
            flights[j+1] = temp


for i in flights:
    print()
    print(i)