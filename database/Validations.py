import hashlib
import re
from connect_to_db import connect


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
    
    conn, cur, local_connection = connect(None, None)
    query = """
            SELECT national_code, password FROM %s
            WHERE national_code = %s AND password = %s;
            """
    cur.execute(query, input_data)
    validation = cur.fetchone()
    
    return validation
