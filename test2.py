import requests # import requests module, that allows to send HTTP requests using Python

BASE = "http://127.0.0.1:5000/" # This is the base url to access the server and the flask application.

# put is used to update the data in the server and the flask application. The first parameter is the url to access the resource and the second is the data that will be updated.

response = requests.put(BASE + "video/1", {"likes": 10, "views": 10000000})

print(response.json()) 

