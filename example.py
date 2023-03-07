import requests

# Making a GET request
r = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# check status code for response received
# success code - 200
print(r)
#dev 2 change
# print content of request
print(r.content)