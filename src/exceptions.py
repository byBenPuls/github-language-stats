# TODO: это лишнее достаточно `class NotFoundUserError(Exception): pass`
# TODO сделать базовый класс ошибок своим
class NotFoundUserError(Exception):
    """
    Raised when user not found
    """


class RequestLimitError(Exception):
    """
    Raised when request limit exceeded
    """


class NotElementClassError(Exception):
    pass
