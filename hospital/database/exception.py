class MyException(Exception):
    
    def AlreadyExist(user_input):
        return f'ERROR: {user_input} is already exist! :('

    def InvalidPassword():
        return 'ERROR: password is invalid! :('
    
    def InvalidGender():
        return 'ERROR: gender is invalid! :('
    
    def InvalidDateTime(date_time):
        return f'ERROR: {date_time} is NOT VALID date or time! :('
    
    def ReservedDateTime(date_time):
        return f'ERROR: {date_time} RESERVED before! please choose other date or time! :('
    
    def NotExistDateTime(date_time):
        return f'ERROR: {date_time} is NOT EXIST for visit a doctor! :('
    
