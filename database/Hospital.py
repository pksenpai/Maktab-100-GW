import re
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
    def __init__(self, first_name, last_name, gender, birth_date, phone, email, address, password, national_code, login_status):
#         # self.user_id = None
        self.first_name = first_name
        self.last_name = last_name
        self.password = valid_pass(password)
        self.phone = phone
        self.email = email
        self.gender = gender
        self.birth_date = birth_date
        self.address = address
        self.national_code = national_code
        self.login_status = False


class Doctor(User):
    def __init__(self, first_name, last_name, gender, birth_date
                 , phone, email, address, password,
                 national_code, login_status,
                 medical_council_code, specialization):
        super().__init__(first_name, last_name, gender, birth_date,
                         phone, email, address, password,
                         national_code, login_status)
        self.medical_council_code = medical_council_code
        self.specialization = specialization


class Patient(User):
    def __init__(self, first_name, last_name, gender, birth_date,
                         phone, email, address,
                         national_code, health_insurance_id, password, login_status):
        super().__init__(first_name, last_name, gender, birth_date,
                         phone, email, address,
                         national_code, login_status)
        self.health_insurance_id = health_insurance_id
        self.password = password




# first_name = 'soroush'
# last_name = 'zohoor'
# gender = 'm'
# birth_date = '1900'
# phone = '095941112'
# email = 'so@email'
# address = 'baghfeiz'
# national_code = 136548
# health_insurance_id = None
# password = "12345ImI"
# login_status = False
#
# p1 = Patient(first_name, last_name, gender, birth_date,
#                       phone, email, address,
#                       national_code, health_insurance_id, password, login_status
#                       )
# print(p1.__dict__)


