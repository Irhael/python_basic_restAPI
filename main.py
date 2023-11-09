from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__) # This line is used to initialize the flask app
api = Api(app) # This line is used to initialize the flask_restful api

class Route(Resource): # this class is used to create a resource. It will work like a route with methods that can be overrided.
    def get(self): # This method is used to send a get request to the server
        return {"data": "This is a get method"} # This line is used to return a json object to the client
    
    def post(self):
        return {"data": "This is a post method"}

api.add_resource(Route, "/route")
# This line is used to add the resource created below to the api. The first parameter is the resource class and the second is the route, that will be used to access the resource.

if __name__ == "__main__": # verify if the file is being executed directly. that means, if the file is not being imported
    app.run(debug=True) # This line is used to run the server and the flask application. The debug=True is used to show the errors in the browser

# http://127.0.0.1:5000/ -> After run the program. This is my local default url to access the server and the flask application.



