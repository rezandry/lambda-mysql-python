import boto3
import json


class LambdaInvoke:

    def __init__(self):
        self.lambda_client = boto3.client('lambda',
                                          region_name='ap-southeast-1',
                                          aws_access_key_id='aws_access_key_id',
                                          aws_secret_access_key='aws_secret_access_key')
        self.__payload = None
        self.__lambda_name = None
        self.__region_name = ''

    def payload(self, payload):
        self.__payload = payload
        return self

    def lambda_name(self, lambda_name):
        self.__lambda_name = lambda_name
        return self

    def invoke_lambda(self):
        try:
            response = self.lambda_client.invoke(FunctionName=self.__lambda_name,
                                                 InvocationType='RequestResponse',
                                                 Payload=json.dumps(self.__payload))
            response = response['Payload'].read()
            response = json.loads(response)
            return response
        except Exception as e:
            print(e)
            response = 'Invocation Failed'
            return response
