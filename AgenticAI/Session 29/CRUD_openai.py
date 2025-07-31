from MongoHelper import MongoDBHelper
import datetime
db = MongoDBHelper()
db.select_db()

def get_patient_by_phone(phone):
    db.select_db(collection='aiPatient')
    query = {'phone': phone}
    documents = db.fetch(query)
    if len(documents) > 0:
        return documents[0]
    
    

def add_patient(name, phone, email):
    db.select_db(collection='aiPatient')
    patient = get_patient_by_phone(phone)
    if patient:
        return 'Patient {} already exists with phone {}. Would you like to write the consultation instead?'.format(name, phone)
    patient = {
        'name': name,
        'phone': phone,
        'email': email,
        'created_at': datetime.datetime.now()
    }
    result = db.insert(doc=patient)
    if result.inserted_id:
        return '{} added successfully with {}'.format(name,phone)
    

def save_consultation(phone, medicines, remarks):
    db.select_db(collection='aiConsultation')
    query=  {
        'phone': phone,
        'medicines': medicines,
        'remarks': remarks,
        'created_at': datetime.datetime.now()
    }
    result = db.insert(doc=query)
    if result.inserted_id:
        return 'Consultation saved successfully for {}'.format(phone)
    else:
        return 'Failed to save consultation for {}'.format(phone)


