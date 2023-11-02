# from create_tables import *
from insert_data import *

# create_table_doctor()
# create_table_health_insurance()
# create_table_patient()
# create_table_appointment()
# create_table_patient_history()
# create_table_patient_bill()

## DELETE FROM table_name
## WHERE condition;


# with InsertToHealthInsuranceTable() as HI:
#     company = 'E'
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
#     national_code = 13653548
#     login_status = False
#     medical_council_code = 123852445
#     specialization = 'maghz o asaab'
#     DC.insert_to_database(first_name, last_name, gender, birth_date,
#                           phone, email, address, password,
#                           national_code, login_status,
#                           medical_council_code, specialization)

with InsertToPatientTable() as PT:
    first_name = 'soroush'
    last_name = 'zohoor'
    gender = 'm'
    birth_date = '1900'
    phone = '095941112'
    email = 'so@email'
    address = 'baghfeiz'
    national_code = 136548
    health_insurance_id = None
    password = "Am1234Im46"
    login_status = False

    PT.insert_to_database(first_name, last_name, gender, birth_date,
                          phone, email, address,
                          national_code, health_insurance_id, password, login_status
                          )
