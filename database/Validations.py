import hashlib
import re


def valid_pass(password):
    pass_regex = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    print(password)
    if not re.match(pass_regex, password):
        # raise InvalidPassword('زمر عبور معتبر نیست')
        print('رمز عبور معتبر نیست')
    else:
        return hashlib.sha256(str(password).encode('utf-8')).hexdigest()