class EmmentalException(Exception):
    error_code = 0
    external_message = "Unknown Error"
    internal_message = "Something went wrong here"
    status_code = 500


class EmptyFieldException(EmmentalException):
    def __init__(self, error_code: int, blank_field: str):
        self.external_message = "Unknown Error"
        self.internal_message = (
            "Empty field: The following field was blank : " + blank_field
        )
        self.status_code = 500
        self.error_code = error_code

    def __str__(self):
        return self.internal_message


class EmmentalTypeException(EmmentalException):
    def __init__(self, error_code: int, incorrect_input: str):
        self.error_code = error_code
        self.internal_message = (
            "Inconsistent type: the following input did not respect the right type : "
            + blank_field
        )
        self.external_message = "Unknown Error"
        self.status_code = 500

    def __str__(self):
        return self.internal_message


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
