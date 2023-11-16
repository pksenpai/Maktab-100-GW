import hashlib
import re
from exception import MyException as exc
from connect_to_db import Database


def valid_pass(password):
    PASSWORD_regex = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    if re.match(PASSWORD_regex, password):
        return hashlib.sha256(str(password).encode('utf-8')).hexdigest(), True
    else:
        return exc.InvalidPassword(), False        

def valid_gender(gender):
    if gender=='f' or gender=='m':
        return gender, True
    else:
        return exc.InvalidGender(), False

def valid_login(input_data: tuple):
    input_data: (table_name, national_code, password)
    
    with Database() as db:
        query = """
                SELECT gender, first_name, last_name 
                FROM %s
                WHERE national_code = %s AND password = %s;
                """
        
        db.cur.execute(query, input_data)
        validation = db.cur.fetchone()
        
    return validation

def valid_datetime(date_time):
    # day/month/year hour:min
    DATETIME_regex = r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$"
    if re.match(DATETIME_regex, date_time):
        with Database() as db:
            Dquery = """
                    SELECT present_datetime
                    FROM doctor
                    WHERE present_datetime = %s;
                    """
            db.cur.execute(Dquery, date_time)
            
            if db.cur.fetchone():
                Vquery = """
                        SELECT reserved_datetime 
                        FROM appointment
                        WHERE reserved_datetime = %s;
                        """ 
                db.cur.execute(Vquery, date_time)
                if not db.cur.fetchone():
                    return date_time, True
                else:
                    return exc.ReservedDateTime(), False
            else:
                return exc.NotExistDateTime(), False
    else:
        return exc.InvalidDateTime(), False
    
    
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
