import application
import json
import time

data = {
	"path": "/hello",
	"httpMethod": "GET",
	"headers": {},
	"queryStringParameters": {}
}

if data.get('body') or isinstance(data.get('body'), dict):
    data['body'] = json.dumps(data['body'])
start = time.time()
result_json = application.handler(data, None)
print(result_json)
result_body = json.loads(result_json['body'])
print(json.dumps(result_body, indent=4, sort_keys=True))
end = time.time()
print('Code executed in %.2fs' % (end - start))

