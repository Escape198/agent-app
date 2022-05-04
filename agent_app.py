import requests
import mod_agent_app


code = mod_agent_app.auth_token
headers = mod_agent_app.headers


url = 'https://partner.agentapp.ru' + code[0]


if code[1] == 'post':
    method = requests.post
elif code[1] == 'get':
    method = requests.get
elif code[1] == 'put':
    method = requests.put
elif code[1] == 'delete':
    method = requests.delete


test = method(url, json=code[2], headers=headers)

print('#' * 15, test.status_code, test.json())

print(test)
