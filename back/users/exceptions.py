from core.exceptions import EmmentalException


class IncorrectCredentialsException(EmmentalException):
    def __init__(self, error_code: int):
        self.error_code = error_code
        self.external_message = "Incorrect credentials"
        self.internal_message = "Given credentials do not match"
        status_code = 500

    def __str__(self):
        return self.internal_message
