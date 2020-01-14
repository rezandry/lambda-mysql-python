from app.config.Application import GLOBAL_VALUE


class ApiUtils:

    @classmethod
    def get_action_data(cls, param):
        return GLOBAL_VALUE.get(param['httpMethod'] + param['path'])