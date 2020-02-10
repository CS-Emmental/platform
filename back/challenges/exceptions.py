class EmmentalException(Exception):
    error_code = 0
    external_message = "Unknown Error"
    internal_message = "Something went wrong here"
    status_code = 500

class InconsistentTitleException(EmmentalException):
    error_code = 1
    external_message = "Unknown Error"
    internal_message = "Inconsistent title: title cannot be left blank"
    status_code = 500