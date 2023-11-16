from database import Database


def reserve(date_time, reason, name, gender):
    with Database() as db:
        query = """                   3###############3################################### HERE change the query
                SELECT payment_discount_percentage 
                FROM health_insurance
                WHERE national_code = %s AND password = %s; 
                """
        db.cur.execute(query, name)
        insurance_contribution = db.cur.fetchone()
        
        total_cost = 200
        payable_cost = total_cost - (100 / insurance_contribution * total_cost)
        
        print(f'<visit cost is {total_cost}>')
        print(f'<your insurance discount percentage is {insurance_contribution}>')
        print(f'<payable cost is {payable_cost}>')
        patient_payable = input('enter your cart in ... and pay it! :3')
        if patient_payable==payable_cost:
            print('you paied successfuly! <3')    
            transaction_status = True
            
            data = date_time, reason
            with Database() as db:
                query = """
                        INSERT INTO appointment(reserved_datetime, reason)
                        values (%s,%s);
                        """
                            
                db.cur.execute(query, data)
                db.conn.commit()
            
            if gender=='m':
                return f'mr.{name} your visit successfuly reserved at {date_time}'
            
            elif gender=='f':
                return f'ms.{name} your visit successfuly reserved at {date_time}'
            
def history(national_code):
    with Database() as db:
        query = """
                SELECT *
                FROM doctor INNER JOIN appointment ON doctor.doctor_id==appointment.appointment_id
                LEFT JOIN patient ON appointment.appointment_id=patient.patient_id;
                WHERE national_code = %s;
                """
        db.cur.execute(query, national_code)
        history = db.cur.fetchone()
        return history
    