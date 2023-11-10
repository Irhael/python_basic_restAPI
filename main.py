from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__) # This line is used to initialize the flask app
api = Api(app) # This line is used to initialize the flask_restful api

video_put_arguments = reqparse.RequestParser() # This line is used to create a parser to get the data sent to the server and the flask application.
video_put_arguments.add_argument("name", type=str, help="video_name not founded", required=True)
video_put_arguments.add_argument("views", type=int, help="video_views not founded", required=True)
video_put_arguments.add_argument("likes", type=int, help="video_likes not founded", required=True) # required=True means that the argument is required to send the request to the server and the flask application. If the argument is not sent, the request will not be sent and the server will return an error, like "name of the video"
videos = {}

def video_exists(video_id): # This function is used to verify if the video exists in the server and the flask application.
    if video_id not in videos:
        abort(404, message="Video not founded") # This line is used to return an error if the video does not exist in the server and the flask application.

class Video (Resource): # this class is used to create a resource. It will work like a route with methods that can be overrided.
    def get(self, video_id): # This method is used to send a get request to the server
        video_exists(video_id) # This line is used to verify if the video exists in the server and the flask application.
        return videos[video_id] # This line is used to return the object that will be converted to a json object. The object is a dictionary with the video_id as key and the video as value.


    def put(self, video_id):
        args = video_put_arguments.parse_args() # This line is used to get the arguments sent to the server and the flask application..
        videos[video_id] = args # This line is used to update the videos dictionary with the video_id as key and the video as value.
        return videos[video_id], 201 # This line is used to return the object that will be converted to a json object. The object is a dictionary with the video_id as key and the video as value. The 201 is the status code of the request. It means that the request was successful.
api.add_resource(Video, "/video/<int:video_id>")
# This line is used to add the resource created below to the api. The first parameter is the resource class and the second is the route, that will be used to access the resource.

if __name__ == "__main__": # verify if the file is being executed directly. that means, if the file is not being imported
    app.run(debug=True) # This line is used to run the server and the flask application. The debug=True is used to show the errors in the browser

# http://127.0.0.1:5000/ -> After run the program. This is my local default url to access the server and the flask application.



