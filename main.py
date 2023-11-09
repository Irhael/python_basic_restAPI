from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__) # This line is used to initialize the flask app
api = Api(app) # This line is used to initialize the flask_restful api

if __name__ == "__main__": # verify if the file is being executed directly. that means, if the file is not being imported
    app.run(debug=True) # This line is used to run the server and the flask application. The debug=True is used to show the errors in the browser

# http://127.0.0.1:5000/ -> After run the program. This is my local default url to access the server and the flask application.

class SuperClass(Resource): # this class is used to create a resource. It will work like a route with methods that can be overrided.
    def get(self):
        return {"data": "Hello World"}