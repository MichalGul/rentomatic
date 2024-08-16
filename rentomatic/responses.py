class ResponseTypes:
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"
    SUCCESS = "Success"


class ResponseFailure:
    def __init__(self, type_, message):
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return f"{msg.__class__.__name__}: {msg}"
        return msg

    @property
    def value(self):
        return {
            "type": self.type,
            "message": self.message
        }

    def __bool__(self):
        return False


class ResponseSuccess:
    def __init__(self, value):
        self.type = ResponseTypes.SUCCESS
        self.value = value

    def __bool__(self):
        return True


def build_response_from_invalid_request(invalid_request):
    message = "\n".join([f"{error['parameter']}: {error['message']}" for error in invalid_request.errors])
    return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, message)
