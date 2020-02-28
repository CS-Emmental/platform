class EmmentalException(Exception):
    error_code = 0
    external_message = "Unknown Error"
    internal_message = "Something went wrong here"
    status_code = 500


class InconsistentDateException(EmmentalException):
    error_code = 1
    external_message = "Unknown Error"
    internal_message = "Inconsistent dates: creation date is after update date"
    status_code = 500

class EmptyFieldException(EmmentalException):
    error_code = 1
    external_message = "Unknown Error"
    internal_message = "Empty field: one field cannot be left blank"
    status_code = 500


class EmmentalTypeException(EmmentalException):
    error_code = 1
    external_message = "Unknown Error"
    internal_message = "Inconsistent type: an input did not respect the right type"
    status_code = 500
