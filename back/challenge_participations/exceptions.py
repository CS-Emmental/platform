from core.exceptions import EmmentalException


class EmmentalFlagSecretException(EmmentalException):
    def __init__(self, error_code: int):
        self.error_code = error_code
        self.external_message = "Unknown Error"
        self.internal_message = (
            "EmmentalFlagSecretException: The secret submitted was the wrong one"
        )
        self.status_code = 500

    def __str__(self):
        return self.internal_message
