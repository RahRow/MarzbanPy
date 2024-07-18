class BadResponse(BaseException):
    pass


class BearerRequired(BaseException):
    pass


class ExistenceError(BaseException):
    pass


class PermissionDenied(BaseException):
    pass


class ValidationError(BaseException):
    pass


class NotExistsError(BaseException):
    pass


class AuthenticationFailed(BaseException):
    pass
