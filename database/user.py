from connect_to_db import Database
from exception import MyException as exc
import Validations as val
import pickle


#=============================[USER]=============================>
class User:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.gender = None
        self.birth_date = None
        self.phone = None
        self.email = None
        self.address = None
        self.__password = None
        self.national_code = None
        self.login_status = False
    
    def login(self, user_type: str):                    
        """ Login users in their account """
        input_national_code = input("Enter your national code: ")
        input_password = hashlib.sha256(input("Enter your password: ").encode()).hexdigest()
        
        input_data = (user_type, input_national_code, input_password)
        gender, fName, lName = val.valid_login(input_data)
        
        if name:
            self.login_status = True
            if user_type=='doctor':       
                print(f'Welcome dr.{fname} {lName} :D')
            else:
                if gender=='f':
                    print(f'Welcome ms.{fname} {lName} :D')
                elif gender=='m':
                    print(f'Welcome mr.{fname} {lName} :D')
                    
#=============================[DOCTOR]=============================>

class Doctor(User):
    def __init__(self, first_name, last_name, gender, birth_date,
                 phone, email, address,
                 password, login_status,national_code,
                 medical_council_code, specialization):
        super().__init__(first_name, last_name, gender, birth_date,
                         phone, email, address, password,
                         login_status, national_code)
        self.medical_council_code = None
        self.specialization = None

    def doctor_register(self):
        self.national_code = input("Please enter your national code: ")
        self.medical_council_code = input("Please enter your medical_council_code: ")
        
        input_data = (table_name, self.national_code, self.medical_council_code)
        exist_national_code, exist_medical_council_code = val.account_exist(input_data)
        
        if exist_national_code:
            print(exc.AlreadyExist(self.national_code))
            return 'menu_setter.core.back'
        
        elif exist_medical_council_code:
            print(exc.AlreadyExist(self.medical_council_code))
            return 'menu_setter.core.back'
        
        else:  
            p_flag, g_flag = False, False
            
            while p_flag=='False':
                password = input("Please enter your password: ")
                valid_password, p_flag = val.valid_pass(password)
            
            while g_flag=='False':
                gender = input("Please enter your gender[f/m]: ")
                valid_gender, g_flag = val.valid_gender(gender)
                
            self.__password = valid_password
            self.gender = valid_gender
            self.first_name = input("Please enter your first name: ")
            self.last_name = input("Please enter your last name: ")
            self.birth_date = input("Please enter your birth_date: ")
            self.phone = input("Please enter your phone: ")
            self.email = input("Please enter your email: ")
            self.address = input("Please enter your address: ")
            self.specialization = input("Please enter your specialization: ")
            
            with Database() as db:
                query = """
                        INSERT INTO doctor(first_name, last_name, gender, birth_date,
                                            phone, email, address, password, login_status,national_code,
                                            medical_council_code, specialization)
                                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                        """
                data = (
                        self.first_name, self.last_name, self.gender, self.birth_date,
                        self.phone, self.email, self.address, self.__password,
                        self.login_status, self.national_code,
                        self.medical_council_code, self.specialization
                    )

                db.cur.execute(query, data)
                db.conn.commit()
                print(f"congratulation dr.{self.filename}!\nyour account created! :3")
    
    
    
#=============================[PATIENT]=============================>
    
class Patient(User):
    def __init__(self, first_name, last_name, gender, birth_date,
                 phone, email, address,
                 password, login_status,
                 national_code, health_insurance_id):
        super().__init__(first_name, last_name, gender, birth_date,
                         phone, email, address, password,
                         login_status, national_code)
        
        self.health_insurance_id = None

    def patient_register(self):
        self.national_code = input("Please enter your national code: ")
        self.health_insurance_id = input("Please enter your  health_insurance_id: ")
        
        input_data = (table_name, self.national_code, self.health_insurance_id)
        exist_national_code, exist_health_insurance_id = val.account_exist(input_data)
        
        if exist_national_code:
            print(exc.AlreadyExist(self.national_code))
            return 'menu_setter.core.back'
        
        elif exist_health_insurance_id:
            print(exc.AlreadyExist(self.health_insurance_id))
            return 'menu_setter.core.back'
                    
        else:
            p_flag, g_flag = False, False
            
            while p_flag=='False':
                password = input("Please enter your password: ")
                valid_password, p_flag = val.valid_pass(password)
            
            while g_flag=='False':
                gender = input("Please enter your gender[f/m]: ")
                valid_gender, g_flag = val.valid_gender(gender)
                
            self.__password = valid_password
            self.gender = valid_gender
            self.first_name = input("Please enter your first name: ")
            self.last_name = input("Please enter your last name: ")
            self.birth_date = input("Please enter your birth_date: ")
            self.phone = input("Please enter your phone: ")
            self.email = input("Please enter your email: ")
            self.address = input("Please enter your address: ")


            with Database() as db:
                query = """
                        INSERT INTO patient(first_name, last_name, gender, birth_date,
                                                phone, email, address, password, login_status,
                                                national_code, health_insurance_id)
                                                values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                        """
                data = (
                        self.first_name, self.last_name, self.gender, self.birth_date,
                        self.phone, self.email, self.address,
                        self.password, self.login_status,
                        self.national_code, self.health_insurance_id
                    )

                db.cur.execute(query, data)
                db.conn.commit()
                
                if self.gender=='f':
                    print(f"congratulation ms.{self.filename}!\nyour account created! :3")
                elif self.gender=='m':
                    print(f"congratulation mr.{self.filename}!\nyour account created! :3")
                    
    