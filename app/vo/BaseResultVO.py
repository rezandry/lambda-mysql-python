import json
import math


class BaseResultVO:

    def __init__(self, code=20, result={}, message='Success', error='', status_code_api=200):
        self.code = code
        self.__status_code_api = status_code_api
        self.result = result
        self.message = message
        self.error = error

    def _construct_response(self):
        self.result = self.result if self.result else {}
        response = {
            'status': {
                'status_code': self.code,
                'message_client': self.message,
                'message_server': self.error
            },
            'result': self.result
        }

        return json.loads(json.dumps(response, sort_keys=False, indent=4, separators=(',', ': ')))

    def response(self):
        return {
            'headers': {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': True},
            'statusCode': self.__status_code_api,
            'body': json.dumps(self._construct_response(), sort_keys=False, separators=(',', ': '))}
