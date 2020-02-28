from core.exceptions import EmmentalException

class InconsistentHintsException(EmmentalException):
    def __init__(self, error_code: int):
        self.error_code = error_code
        self.external_message = "Unknown Error"
        self.internal_message = (
            "Inconsistent hints: hints must be positive with a sum inferior to 1"
        )
        self.status_code = 500

    def __str__(self):
        return self.internal_message


class InconsistentFlagsException(EmmentalException):
    def __init__(self, error_code: int):
        self.error_code = error_code
        self.external_message = "Unknown Error"
        self.internal_message = (
            "Inconsistent flags: flags must be positive with a sum inferior to 1"
        )
        status_code = 500

    def __str__(self):
        return self.internal_message


class InconsistentFlagSecretException(EmmentalException):
    def __init__(self, error_code: int):
        self.error_code = error_code
        self.external_message = "Unknown Error"
        self.internal_message = (
            "Inconsistent flag secret: The secret submitted was the wrong one"
        )
        self.status_code = 500

    def __str__(self):
        return self.internal_message
