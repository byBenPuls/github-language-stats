class NotFoundUserError(Exception):
    """
    Raised when user not found
    """
    def __init__(self, message: str = 'User not found'):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class RequestLimitError(Exception):
    """
    Raised when request limit exceeded
    """
    def __init__(self, message: str = 'Request limit exceeded'):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message
