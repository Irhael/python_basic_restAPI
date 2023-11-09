import requests # import requests module, that allows to send HTTP requests using Python

#testing post method

BASE = "http://127.0.0.1:5000/" # This is the base url to access the server and the flask application.

response = requests.post(BASE + "route") 

print(response.json()) 

# test2.py response: {'message': 'The method is not allowed for the requested URL.'}. This is cause the post methos is not overrided in the resource class yet. So the server give the default response for a post request.