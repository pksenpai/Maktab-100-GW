from connect_to_db import connect
from Hospital import *




class InsertToHealthInsuranceTable:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.local_connection = None
        # self.result = None
        # self.err = None
        # self.health_insurace = None
        # self.exc_type = None
        # self.exc_val = None

    def __enter__(self):
        return self

    def insert_to_database(self, company, address, phone, email, payment_discount_percentage):
        self.health_insurace = HealthInsurance(company, address, phone, email,
                                               payment_discount_percentage)
        # self.health_insurace.health_insurance_id = None
        self.conn, self.cur, self.local_connection = connect(None, None)
        query = """INSERT INTO health_insurance(
        company, address, phone, email, payment_discount_percentage)
             values (%s,%s,%s,%s,%s);
             """
        data = (self.doctor.health_insurace.company, self.health_insurace.address, self.health_insurace.phone,
                self.health_insurace.email, self.health_insurace.payment_discount_percentage)
        self.cur.execute(query, data)
        self.conn.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # self.cur.close()
        # self.conn.close()

class InsertToDoctorTable:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.local_connection = None
        # self.result = None
        # self.err = None
        self.doctor = None
        # self.exc_type = None
        # self.exc_val = None

    def __enter__(self):
        return self

    def insert_to_database(self, first_name, last_name, gender, birth_date,
                            phone, email, address, password,
                            national_code, login_status,
                            medical_council_code, specialization):
        self.doctor = Doctor(first_name, last_name, gender, birth_date,
                             phone, email, address, password,
                             national_code, login_status,
                             medical_council_code, specialization)
        # self.doctor.doctor_id = None
        self.conn, self.cur, self.local_connection = connect(None, None)
        query = """INSERT INTO doctor(first_name, last_name, gender, birth_date
                                    , phone, email, address, password,
                                    national_code, login_status,
                                    medical_council_code, specialization)
             values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
             """
        data = (self.doctor.first_name, self.doctor.last_name, self.doctor.gender, self.doctor.birth_date,
                 self.doctor.phone, self.doctor.email, self.doctor.address, self.doctor.password,
                 self.doctor.national_code, self.doctor.login_status,
                 self.doctor.medical_council_code, self.doctor.specialization)

        self.cur.execute(query, data)
        self.conn.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # self.cur.close()
        # self.conn.close()

class InsertToPatientTable:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.local_connection = None
        # self.result = None
        # self.err = None
        # self.patient = None
        # self.exc_type = None
        # self.exc_val = None

    def __enter__(self):
        return self

    def insert_to_database(self, first_name, last_name, gender, birth_date,
                            phone, email, address,
                            national_code, health_insurance_id, password, login_status):
        self.patient = Patient(first_name, last_name, gender, birth_date,
                            phone, email, address,
                            national_code, health_insurance_id, password, login_status)
        # self.patient.patient_id = None
        self.conn, self.cur, self.local_connection = connect(None, None)
        query = """INSERT INTO patient(first_name, last_name, gender, birth_date,
                                        phone, email, address,
                                        national_code, health_insurance_id,
                                        password, login_status)
             values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
             """
        data = (self.patient.first_name, self.patient.last_name, self.patient.gender, self.patient.birth_date,
                 self.patient.phone, self.patient.email, self.patient.address,
                 self.patient.national_code, self.patient.health_insurance_id,
                 self.patient.password, self.patient.login_status)

        self.cur.execute(query, data)
        self.conn.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # self.cur.close()
        # self.conn.close()




