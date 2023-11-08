import Validations as val
import pickle


class User:
    def __init__(self, first_name, last_name, gender, 
                 birth_date, phone, email, address, 
                 password, national_code, login_status):

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_date = birth_date
        self.phone = phone
        self.email = email
        self.address = address
        self.password = password
        self.national_code = national_code
        self.login_status = False
    
    def login(self, user_type: str):                    
        """ Login users in their account """
        input_national_code = input("Enter your national code: ")
        input_password = hashlib.sha256(input("Enter your password: ").encode()).hexdigest()
        
        input_data = (user_type, input_national_code, input_password)
        name = val.valid_login(input_data)
        
        if name:
            self.login_status = True             
            print(f'Welcome {name} :D')


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

    def doctor_register():
        pass
    
    
class Patient(User):
    def __init__(self, first_name, last_name, gender, birth_date,
                 phone, email, address,
                 password, login_status,
                 national_code, health_insurance_id):
        super().__init__(first_name, last_name, gender, birth_date,
                         phone, email, address, password,
                         login_status, national_code)
        self.health_insurance_id = health_insurance_id

    def patient_register():
        pass
    
    