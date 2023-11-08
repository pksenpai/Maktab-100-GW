from connect_to_db import Database
import exception as exc
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
        self.__password = password
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

    def doctor_register(self):
        self.national_code = input("Please enter your national code: ")
        self.medical_council_code = input("Please enter your medical_council_code: ")
        
        input_data = (table_name, self.national_code, self.medical_council_code)
        exist_national_code, exist_medical_council_code = val.account_exist(input_data)
        
        if exist_national_code:
            print(exc.already_exist(self.national_code))
            return 'menu_setter.core.back'
        
        elif exist_medical_council_code:
            print(exc.already_exist(self.medical_council_code))
            return 'menu_setter.core.back'
        
        else:    
            self.first_name = input("Please enter your first name: ")
            self.last_name = input("Please enter your last name: ")
            self.gender = input("Please enter your gender: ")
            self.birth_date = input("Please enter your birth_date: ")
            self.phone = input("Please enter your phone: ")
            self.email = input("Please enter your email: ")
            self.address = input("Please enter your address: ")
            self.specialization = input("Please enter your specialization: ")
            self.__password = input("Please enter your password: ")
            
            with Database() as db:
                query = """
                        INSERT INTO doctor(first_name, last_name, gender, birth_date,
                                            phone, email, address, password, login_status,national_code,
                                            medical_council_code, specialization)
                                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                        """
                data = (self.first_name, self.last_name, self.gender, self.birth_date,
                        self.phone, self.email, self.address, self.__password,
                        self.login_status, self.national_code,
                        self.medical_council_code, self.specialization)

                db.cur.execute(query, data)
                print(f"congratulation dr.{self.filename}!\nyour account created! :3")
    
    
    
#==========================================================
    
class Patient(User):
    def __init__(self, first_name, last_name, gender, birth_date,
                 phone, email, address,
                 password, login_status,
                 national_code, health_insurance_id):
        super().__init__(first_name, last_name, gender, birth_date,
                         phone, email, address, password,
                         login_status, national_code)
        
        self.health_insurance_id = health_insurance_id

    def patient_register(self):
        pass
    