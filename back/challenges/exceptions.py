class EmmentalException(Exception):
    error_code = 0
    external_message = "Unknown Error"
    internal_message = "Something went wrong here"
    status_code = 500

class EmptyFieldException(EmmentalException):
    error_code = 1
    external_message = "Unknown Error"
    internal_message = "Empty field: one field cannot be left blank"
    status_code = 500

class InconsistentTypeException(EmmentalException):
    error_code = 1
    external_message = "Unknown Error"
    internal_message = "Inconsistent type: an input did not respect the right type"
    status_code = 500

class InconsistentHintsException(EmmentalException):
    error_code = 1
    external_message = "Unknown Error"
    internal_message = "Inconsistent hints: hints must be positive with a sum inferior to 1"
    status_code = 500

class InconsistentFlagsException(EmmentalException):
    error_code = 1
    external_message = "Unknown Error"
    internal_message = "Inconsistent flags: flags must be positive with a sum inferior to 1"
    status_code = 500

class InconsistentFlagSecretException(EmmentalException):
    error_code = 1
    external_message = "Unknown Error"
    internal_message = "Inconsistent flag secret: The secret submitted was the wrong one"
    status_code = 500