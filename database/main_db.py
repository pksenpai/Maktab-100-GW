from create_tables import *
from insert_data import *
from connect_to_db import connect


# create_table_doctor()
# create_table_health_insurance()
# create_table_patient()
# create_table_appointment()
# create_table_patient_history()
# create_table_patient_bill()

## DELETE FROM table_name
## WHERE condition;


# with InsertToHealthInsuranceTable() as HI:
#     company = 'A'
#     address = 'add333'
#     phone = '02148858254'
#     email = 'healthE@email'
#     payment_discount_percentage = 90
#     HI.insert_to_database(company, address, phone, email, payment_discount_percentage)

# with InsertToDoctorTable() as DC:
#     first_name = 'soroush'
#     last_name = 'zohoor'
#     gender = 'm'
#     birth_date = '1900'
#     phone = '095941112'
#     email = 'so@email'
#     address = 'baghfeiz'
#     password = '1234Im65146'
#     national_code = '13653548'
#     login_status = False
#     medical_council_code = '123852445'
#     specialization = 'maghz o asaab'
#     DC.insert_to_database(first_name, last_name, gender, birth_date,
#                           phone, email, address, password,
#                           login_status,
#                           national_code,
#                           medical_council_code, specialization)

# with InsertToPatientTable() as PT:
#     first_name = 'soroush'
#     last_name = 'zohoor'
#     gender = 'm'
#     birth_date = '1900'
#     phone = '095941112'
#     email = 'so@email'
#     address = 'baghfeiz'
#     national_code = '136548'
#     health_insurance_id = None
#     password = "Am1234Im46"
#     login_status = False
#
#     PT.insert_to_database(first_name, last_name, gender, birth_date,
#                           phone, email, address, password, login_status,
#                           national_code, health_insurance_id
#                           )
#
# with InsertToAppointmentTable() as AP:
#     patient_id = 1
#     doctor_id = 1
#     date_time = '02148858254'
#     reason = 'healthE@email'
#     AP.insert_to_database(patient_id, doctor_id, date_time, reason)
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

# def register_doctor():
#     first_name = input("Please enter your first name: ")
#     last_name = input("Please enter your last name: ")
#     gender = input("Please enter your gender: ")
#     birth_date = input("Please enter your birth_date: ")
#     phone = input("Please enter your phone: ")
#     email = input("Please enter your email: ")
#     address = input("Please enter your address: ")
#     password = input("Please enter your password: ")
#     national_code = input("Please enter your national code: ")
#     medical_council_code = input("Please enter your medical_council_code: ")
#     specialization = input("Please enter your specialization: ")
#     login_status = False
#
#     with InsertToDoctorTable() as DC:
#         DC.insert_to_database(first_name, last_name, gender, birth_date,
#                               phone, email, address, password,
#                               login_status,
#                               national_code,
#                               medical_council_code, specialization)
# register_doctor()



#
# def logout_doctor():
#
#     conn, cur, local_connection = connect(None, None)
#     query = """UPDATE doctor
#         SET login_status = FALSE
#         """
#     cur.execute(query)
#     conn.commit()

# def register_patient():
#     first_name = input("Please enter your first name: ")
#     last_name = input("Please enter your last name: ")
#     gender = input("Please enter your gender: ")
#     birth_date = input("Please enter your birth_date: ")
#     phone = input("Please enter your phone: ")
#     email = input("Please enter your email: ")
#     address = input("Please enter your address: ")
#     password = input("Please enter your password: ")
#     national_code = input("Please enter your national code: ")
#     health_insurance_id = input("Please enter your  health_insurance_id: ")
#     login_status = False
#     with InsertToPatientTable() as PT:
#         PT.insert_to_database(first_name, last_name, gender, birth_date,
#                               phone, email, address, password, login_status,
#                               national_code, health_insurance_id)
#
#
# register_patient()

# def login_patient():
#     user_name = input("Please enter your user name: ")
#     input_password = input("Please enter your password: ")
#
#     conn, cur, local_connection = connect(None, None)
#     query = """select  * FROM patient
#                 WHERE phone = %s AND password = %s;
#                 """
#     data = (user_name, input_password)
#     cur.execute(query, data)
#     result = cur.fetchone()
#     if result:
#         query = """UPDATE patient
#         SET login_status = True
#         """
#     cur.execute(query)
#     conn.commit()
#
#
# login_patient()
#
# def logout_patient():
#
#     conn, cur, local_connection = connect(None, None)
#     query = """UPDATE patient
#         SET login_status = FALSE
#         """
#     cur.execute(query)
#     conn.commit()


