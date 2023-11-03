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


class User:
    def __init__(self, first_name, last_name, gender, birth_date, phone, email, address, password, national_code,
                 login_status):
        #         # self.user_id = None
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.birth_date = birth_date
        self.address = address
        self.password = valid_pass(password)
        self.login_status = False
        self.national_code = national_code


class Doctor(User):
    def __init__(self, first_name, last_name, gender, birth_date,
                 phone, email, address, password,
                 login_status, national_code,
                 medical_council_code, specialization):
        super().__init__(first_name, last_name, gender, birth_date,
                         phone, email, address, password,
                         login_status, national_code)
        self.medical_council_code = medical_council_code
        self.specialization = specialization


class Patient(User):
    def __init__(self, first_name, last_name, gender, birth_date,
                 phone, email, address,
                 password, login_status,
                 national_code, health_insurance_id):
        super().__init__(first_name, last_name, gender, birth_date,
                         phone, email, address, password,
                         login_status, national_code)
        self.health_insurance_id = health_insurance_id


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

#
# rst_name = 'soroush'
# last_name = 'zohoor'
# gender = 'm'
# birth_date = '1900'
# phone = '095941112'
# email = 'so@email'
# address = 'baghfeiz'
# national_code = '136548'
# health_insurance_id = None
# password = "12345ImI"
# login_status = False
#
# p1 = Patient(first_name, last_name, gender, birth_date,
#              phone, email, address, password, login_status,
#              national_code, health_insurance_id
#              )
# print(p1.__dict__)

# first_name = 'soroush'
# last_name = 'zohoor'
# gender = 'm'
# birth_date = '1900'
# phone = '095941112'
# email = 'so@email'
# address = 'baghfeiz'
# password = '1234Im65146'
# national_code = '13653548'
# login_status = False
# medical_council_code = '123852445'
# specialization = 'maghz o asaab'
# d1 = Doctor(first_name, last_name, gender, birth_date,
#             phone, email, address, password,
#             login_status,
#             national_code,
#             medical_council_code, specialization)
# print(d1.__dict__)

# patient_id = 1
# doctor_id = 1
# diagnosis = 'Maraz'
# drug_used = 'sianor'
# prescription = 'die'
# ph1 = PatientHistory(patient_id, doctor_id, diagnosis, drug_used, prescription)
# print(ph1.__dict__)
