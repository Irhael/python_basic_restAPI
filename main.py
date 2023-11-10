from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # This line is used to initialize the flask app
api = Api(app) # This line is used to initialize the flask_restful api
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # This line is used to set the database uri. The database is a sqlite database and the name of the database is database.db
db = SQLAlchemy(app) # This line is used to initialize the flask_sqlalchemy database

class VideoModel(db.Model): # This class is used to create a model to the database. The model is used to create the database tables.
    id = db.Column(db.Integer, primary_key=True) # This line is used to create a column in the database table. The column is used to store the id of the video. The column is an integer and it is the primary key of the table.
    name = db.Column(db.String(100), nullable=False) # This line is used to create a column in the database table. The column is used to store the name of the video. The column is a string with 100 characters and it is not nullable.
    views = db.Column(db.Integer, nullable=False) # This line is used to create a column in the database table. The column is used to store the views of the video. The column is an integer and it is not nullable.
    likes = db.Column(db.Integer, nullable=False) # This line is used to create a column in the database table. The column is used to store the likes of the video. The column is an integer and it is not nullable.

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"
        # This line is used to return a string with the name, views and likes of the video. The string will be used to represent the video object.
    
# db.create_all() # This line is used to create the database tables. The tables are created using the models created above.

video_put_arguments = reqparse.RequestParser() # This line is used to create a parser to get the data sent to the server and the flask application.
video_put_arguments.add_argument("name", type=str, help="video_name not founded", required=True)
video_put_arguments.add_argument("views", type=int, help="video_views not founded", required=True)
video_put_arguments.add_argument("likes", type=int, help="video_likes not founded", required=True) # required=True means that the argument is required to send the request to the server and the flask application. If the argument is not sent, the request will not be sent and the server will return an error, like "name of the video"

video_update_arguments = reqparse.RequestParser()
video_update_arguments.add_argument("name", type=str, help="video_name not founded")
video_update_arguments.add_argument("views", type=int, help="video_views not founded")
video_update_arguments.add_argument("likes", type=int, help="video_likes not founded")


resouce_fields = { # This line is used to create a dictionary with the fields of the video. That are the id, name, views and likes.
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video (Resource): # this class is used to create a resource. It will work like a route with methods that can be overrided.

    @marshal_with(resouce_fields) # This line is used to format the response of the server. The response will be a json object with that fields.
    def get(self, video_id): # This method is used to send a get request to the server
        result = VideoModel.query.filter_by(id=video_id).first() # This line is used to get the video from the database using video_id.
        if not result:
            abort(404, message="video_id not founded") # This line is used to return an error if the video is not founded in the database.
        return result
    
    @marshal_with(resouce_fields)
    def put(self, video_id):
        args = video_put_arguments.parse_args() # This line is used to get the data sent to the server and the flask application.
        result = VideoModel.query.filter_by(id=video_id).first() # This line is used to get the video from the database using video_id.
        if result:
            abort(409, message="video_id already exists") # This line is used to return an error if the video is already in the database.
        new_video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes']) # This line is used to create a new video object using the data sent to the server and the flask application.
        db.session.add(new_video) # This line is used to add the new video to the database.
        db.session.commit() # Commit the changes to the database.
        return new_video, 201
    
    @marshal_with(resouce_fields)
    def patch(self, video_id):
        args = video_update_arguments.parse_args() 
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="video_id not founded and can't be updated")
        for arg in args: # This line is used to update the video object with the data sent to the server.
            if args[arg]: # verify if the argument is not null.
                setattr(result, arg, args[arg]) # setattr is used to change the attribute of the object. The first parameter is the object, the second is the attribute and the third is the new value of the attribute.

        db.session.commit()
        return result
    
    @marshal_with(resouce_fields)
    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first() # .first() is used to get the first video with the id video_id
        db.session.delete(result) # This line is used to delete the video from the database.
        db.session.commit() 

api.add_resource(Video, "/video/<int:video_id>")
# This line is used to add the resource created below to the api. The first parameter is the resource class and the second is the route, that will be used to access the resource.

if __name__ == "__main__": # verify if the file is being executed directly. that means, if the file is not being imported
    app.run(debug=True) # This line is used to run the server and the flask application. The debug=True is used to show the errors in the browser





