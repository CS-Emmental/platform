from core.exceptions import EmmentalException

class EmmentalHintsException(EmmentalException):
    def __init__(self, error_code: int):
        self.error_code = error_code
        self.external_message = "Unknown Error"
        self.internal_message = (
            "EmmentalHintsException : hints must be positive with a sum inferior to 1"
        )
        self.status_code = 500

    def __str__(self):
        return self.internal_message


class EmmentalFlagsException(EmmentalException):
    def __init__(self, error_code: int):
        self.error_code = error_code
        self.external_message = "Unknown Error"
        self.internal_message = (
            "EmmentalFlagsException: flags must be positive with a sum inferior to 1"
        )
        status_code = 500

    def __str__(self):
        return self.internal_message
