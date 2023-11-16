from connect_to_db import connect
from Hospital import *


def insert_health_insurace(self, company, address, phone, email, payment_discount_percentage):
    with Database() as db:    
        query = """
                INSERT INTO health_insurance(
                company, address, phone, email, payment_discount_percentage)
                values (%s,%s,%s,%s,%s);
                """
                
        self.cur.execute(query, data)
        self.conn.commit()
        