import Validations as val
import pickle


class User:
    def __init__(self, first_name, last_name, gender, 
                 birth_date, phone, email, address, 
                 password, national_code, login_status):

        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.birth_date = birth_date
        self.address = address
        self.password = password
        self.login_status = False
        self.national_code = national_code
    
    def login(self, user_type: str):
        """ Login users in their account """
        input_national_code = input("Enter your national code: ")
        input_password = hashlib.sha256(input("Enter your password: ").encode()).hexdigest()
         
        input_data = (user_type, input_national_code, input_password)
        user_data = val.valid_login(input_data)
        
        if input_data:
            input_data: tuple 
            national_code, password = user_data
            with open('auto_login.save', 'wb+') as al:
                pickle.dump(national_code + '\n' + password, al)
            
            query = f"""
                    UPDATE {user_type}
                    SET login_status = True
                    """
            cur.execute(query)
            
        conn.commit()


class Doctor(User):
    def __init__(self, first_name, last_name, gender, birth_date,
                 phone, email, address,
                 password, login_status,national_code,
                 medical_council_code, specialization):
        super().__init__(first_name, last_name, gender, birth_date,
                         phone, email, address, password,
                         login_status, national_code)
        self.medical_council_code = medical_council_code
        self.specialization = specialization


class Patient(User):
    def __init__(self, first_name, last_name, gender, birth_date,
                 phone, email, address,
                 password, login_status,
                 national_code, health_insurance_id):
        super().__init__(first_name, last_name, gender, birth_date,
                         phone, email, address, password,
                         login_status, national_code)
        self.health_insurance_id = health_insurance_id
