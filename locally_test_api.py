import requests
import json

data =  {'message':'palindrome'}
rv = requests.post("http://127.0.0.1:5000/random_gen_endpoint",json=data)
resp =  json.loads(rv.content)['message']
print(resp)