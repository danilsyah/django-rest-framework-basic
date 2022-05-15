import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint, json=[{"nama":"danil","age" : "27"}])

get_response = requests.get(endpoint, json={"product_id" : 123}) #http request

# print(get_response.text)
# print(get_response.json()['product_id'])
# print(get_response.status_code)
print(get_response.json())