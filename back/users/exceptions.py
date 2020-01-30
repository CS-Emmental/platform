from core.exceptions import EmmentalException

class IncorrectCredentialsException(EmmentalException):
    error_code = 1
    error_message = 'Incorrect credentials'
    status_code = 500
    pass