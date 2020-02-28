from core.exceptions import EmmentalException

class InconsistentHintsException(EmmentalException):
    error_code = 1
    external_message = "Unknown Error"
    internal_message = (
        "Inconsistent hints: hints must be positive with a sum inferior to 1"
    )
    status_code = 500


class InconsistentFlagsException(EmmentalException):
    error_code = 1
    external_message = "Unknown Error"
    internal_message = (
        "Inconsistent flags: flags must be positive with a sum inferior to 1"
    )
    status_code = 500
