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
    
# TODO: слишком сложно
error_codes: dict = {
    '404': {
        'message': 'User not found',
        'exception': NotFoundUserError
    },
    '403': {
        'message': 'Request limit exceeded',
        'exception': RequestLimitError
    }
}
