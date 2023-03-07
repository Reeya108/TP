##how to download google.com front page?
import requests

response = requests.get("https://www.google.com/")
response.content
# with open("mygoogle.html", "w") as foo:
#     foo.write(response.text)
