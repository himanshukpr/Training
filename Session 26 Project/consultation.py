'''
consultation
    bphigh, bplow, fever, weigth, sugar,remarks, medicine, follow_up

'''

import datetime

class Consultation:
    def __init__(self, bphigh=120, bplow=80, fever=98.8, weight=0, sugar=80, remarks='', medicine='', follow_up='',doctor_id='',patient_id=''):
        self.bphigh = bphigh
        self.bplow = bplow
        self.fever = fever
        self.weight = weight
        self.sugar = sugar
        self.remarks = remarks
        self.medicine = medicine
        self.follow_up = follow_up
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.created_at = datetime.datetime.now()

    def to_document(self):
        return vars(self)
