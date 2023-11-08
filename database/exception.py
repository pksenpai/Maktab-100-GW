class MyException(Exception):
    
    def AlreadyExist(user_input):
        return f'{user_input} is already exist! :('

    def InvalidPassword():
        return 'password is invalid! :('
    
    def InvalidGender():
        return 'gender is invalid! :('
    