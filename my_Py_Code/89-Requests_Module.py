#Requests Module in python

import requests
# response=requests.get('https://circ.in')
# print(response.status_code) #200 means the request was successful
# print(response.text) #prints the html content of the page

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "foo",
    "body": "bar",
    "userId": 1,
}

headers = {
    "Content-Type": "application/json; charset=UTF-8"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())