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
        data = (self.health_insurace.company, self.health_insurace.address, self.health_insurace.phone,
                self.health_insurace.email, self.health_insurace.payment_discount_percentage)
        self.cur.execute(query, data)
        self.conn.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # self.cur.close()
        # self.conn.close()


def insert_to_database(self, patient_id, doctor_id, date_time, reason):
    self.appointment = Appointment(patient_id, doctor_id, date_time, reason)
    self.conn, self.cur, self.local_connection = connect(None, None)
    query = """INSERT INTO appointment(patient_id, doctor_id, date_time, reason)
            values (%s,%s,%s,%s);
            """
    data = (self.appointment.patient_id, self.appointment.doctor_id, self.appointment.date_time,
            self.appointment.reason)
    self.cur.execute(query, data)
    self.conn.commit()


class InsertToPatientHistoryTable:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.local_connection = None
        # self.result = None
        # self.err = None
        # self.patient_history = None
        # self.exc_type = None
        # self.exc_val = None

    def __enter__(self):
        return self

    def insert_to_database(self, patient_id, doctor_id, diagnosis, drug_used, prescription, note=None):
        self.patient_history = PatientHistory(patient_id, doctor_id, diagnosis, drug_used, prescription, note)
        self.conn, self.cur, self.local_connection = connect(None, None)
        query = """INSERT INTO patient_history(patient_id, doctor_id, diagnosis, drug_used, prescription, date, note)
             values (%s,%s,%s,%s,%s,%s,%s);
             """
        data = (self.patient_history.patient_id, self.patient_history.doctor_id, self.patient_history.diagnosis,
                self.patient_history.drug_used,
                self.patient_history.prescription,
                PatientHistory.date,
                self.patient_history.note)
        self.cur.execute(query, data)
        self.conn.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # self.cur.close()
        # self.conn.close()

class InsertToPatientBillTable:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.local_connection = None
        # self.result = None
        # self.err = None
        # self.patient_bill = None
        # self.exc_type = None
        # self.exc_val = None

    def __enter__(self):
        return self

    def insert_to_database(self, patient_history_id, total_cost, patient_payable, insurance_contribution, transaction_status):
        self.patient_bill = PatientBill(patient_history_id, total_cost, patient_payable, insurance_contribution, transaction_status)
        self.conn, self.cur, self.local_connection = connect(None, None)
        query = """INSERT INTO patient_bill(patient_history_id, total_cost, patient_payable, insurance_contribution, date, transaction_status)
             values (%s,%s,%s,%s,%s,%s);
             """
        data = (self.patient_bill.patient_history_id, self.patient_bill.total_cost, self.patient_bill.patient_payable,
                self.patient_bill.insurance_contribution,
                PatientBill.date,
                self.patient_bill.transaction_status)
        self.cur.execute(query, data)
        self.conn.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # self.cur.close()
        # self.conn.close()

