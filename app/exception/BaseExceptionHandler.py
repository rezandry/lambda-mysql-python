from ..vo.BaseResultVO import BaseResultVO


class BaseExceptionHandler(Exception):

    code = 99
    message_client = 'Oops... Something wrong.'

    def __init__(self, error):
        self._vo = BaseResultVO(code=self.code, message=self.message_client,
                                error=error)

    def message(self):
        return self._vo