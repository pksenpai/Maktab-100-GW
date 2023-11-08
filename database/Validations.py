import hashlib
import re
from connect_to_db import Database


def valid_pass(password):
    pass_regex = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    print(password)
    if not re.match(pass_regex, password):
        # raise InvalidPassword('زمر عبور معتبر نیست')
        print('رمز عبور معتبر نیست')
    else:
        return hashlib.sha256(str(password).encode('utf-8')).hexdigest()
    
def valid_login(input_data: tuple):
    input_data: (table_name, national_code, password)
    
    with Database() as db:
        query = """
                SELECT first_name, last_name FROM %s
                WHERE national_code = %s AND password = %s;
                """
        
        db.cur.execute(query, input_data)
        validation = db.cur.fetchone()
        
    return validation

def account_exist(input_data):
    """ national code already exist?!"""    
    input_data: (1, 2, 3)
    
    with Database() as db:
        query1= """
                SELECT national_code FROM %s
                WHERE national_code = %s;
                """
                    
        db.cur.execute(query1, input_data[0:2])
        validation1 = db.cur.fetchone()
        
        if input_data[0]=='doctor':
            query2= """
                    SELECT medical_council_code FROM %s
                    WHERE medical_council_code = %s;
                    """
            db.cur.execute(query1, (input_data[0],input_data[2]))
            validation2 = db.cur.fetchone()
        
        else:
            query2= """
                    SELECT health_insurance_id FROM %s
                    WHERE health_insurance_id = %s;
                    """
            db.cur.execute(query1, (input_data[0],input_data[2]))
            validation2 = db.cur.fetchone()

    return validation1, validation2
