import requests # import requests module, that allows to send HTTP requests using Pytho

BASE = "http://127.0.0.1:5000/" # This is the base url to access the server and the flask application.

response = requests.get(BASE + "route") # This line is used to send a get request to the server and the flask application. The BASE + "route" is the route to access the resource created in main.py. So http://127.0.0.1:5000/route is the url to access the resource.

print(response.json()) # This line is used to print the object returned by the server and the flask application. The response.json() is used to convert the object to a json object.