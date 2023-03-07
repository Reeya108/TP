import requests
#first change
# Making a GET request
r = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# check status code for response received
# success code - 200
print(r)
# print content of request
print(r.content)