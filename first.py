##how to download google.com front page?
import requests
#request is third party library
response = requests.get("https://www.google.com/")
response.content
# with open("mygoogle.html", "w") as foo:
#     foo.write(response.text)
