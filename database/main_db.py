from create_tables import *
from insert_data import *
from connect_to_db import connect


# with InsertToHealthInsuranceTable() as HI:
#     company = 'A'
#     address = 'add333'
#     phone = '02148858254'
#     email = 'healthE@email'
#     payment_discount_percentage = 90
#     HI.insert_to_database(company, address, phone, email, payment_discount_percentage)


# with InsertToPatientHistoryTable() as PTH:
#     patient_id = 1
#     doctor_id = 1
#     diagnosis = 'Maraz'
#     drug_used = 'sianor'
#     prescription = 'die'
#     PTH.insert_to_database(patient_id, doctor_id, diagnosis, drug_used, prescription)

# with InsertToPatientBillTable() as PB:
#     patient_history_id = 1
#     total_cost = 200
#     patient_payable = 100
#     insurance_contribution = 50
#     transaction_status = True
#     PB.insert_to_database(patient_history_id, total_cost, patient_payable, insurance_contribution, transaction_status)
