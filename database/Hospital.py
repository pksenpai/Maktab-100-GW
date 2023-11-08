import re
from datetime import datetime
from Validations import *


class HealthInsurance:
    def __init__(self, company, address, phone, email, payment_discount_percentage):
        # self.health_insurance_id = None
        self.company = company
        self.address = address
        self.phone = phone
        self.email = email
        self.payment_discount_percentage = payment_discount_percentage
        

class Appointment:
    def __init__(self, patient_id, doctor_id, date_time, reason):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date_time = date_time
        self.reason = reason


class PatientHistory:
    date = datetime.now()

    def __init__(self, patient_id, doctor_id, diagnosis, drug_used, prescription, note=None):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.diagnosis = diagnosis
        self.drug_used = drug_used
        self.prescription = prescription
        self.note = note


class PatientBill:
    date = datetime.now()

    def __init__(self, patient_history_id, total_cost, patient_payable, insurance_contribution, transaction_status):
        self.patient_history_id = patient_history_id
        self.total_cost = total_cost
        self.patient_payable = patient_payable
        self.insurance_contribution = insurance_contribution
        self.transaction_status = transaction_status

