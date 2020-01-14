import json

from app.util.ApiUtils import ApiUtils


class Request:

    def __init__(self):
        self.__function = None
        self.__module = None
        self.__header = None
        self.__body = None
        self.__query = None

    @property
    def function(self):
        return self.__function

    @property
    def module(self):
        return self.__module

    @property
    def header(self):
        return self.__header

    @property
    def body(self):
        return self.__body

    @property
    def query(self):
        return self.__query

    @function.setter
    def function(self, param):
        function_data = ApiUtils.get_action_data(param)
        self.__function = function_data['function'] if function_data and function_data.get('function') else None

    @module.setter
    def module(self, param):
        module_data = ApiUtils.get_action_data(param)
        self.__module = module_data['class'] if module_data and module_data.get('class') else None

    @header.setter
    def header(self, param):
        self.__header = param.get('headers') if param and isinstance(param.get('headers'), dict) else {}

    @body.setter
    def body(self, param):
        if param.get('body'):
            __body = json.loads(param.get('body'))
            self.__body = __body if param and (isinstance(__body, dict) or isinstance(__body, list)) else {}

    @query.setter
    def query(self, param):
        self.__query = param.get('queryStringParameters') if param and isinstance(param.get('queryStringParameters'), dict) else {}

    @classmethod
    def load(cls, event):
        req = cls()
        req.function = event
        req.module = event
        req.query = event
        req.header = event
        req.body = event

        return req