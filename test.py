import requests # import requests module, that allows to send HTTP requests using Python

BASE = "http://127.0.0.1:5000/" # This is the base url to access the server and the flask application.

# put is used to update the data in the server and the flask application. The first parameter is the url to access the resource and the second is the data that will be updated.

data = [{"name": "video00", "likes": 14, "views": 200000}, 
        {"name": "video01", "likes": 10, "views": 10000000}, 
        {"name": "video02", "likes": 15, "views": 7000000}] 

# Using all the methods of the api

#Creating the videos

for video_stats in range (len(data)):
    response = requests.put(BASE + "video/" + str(video_stats), data[video_stats]) 
    print(response.json())

input()

#Getting the videos
for video_stats in range (len(data)):
    response = requests.get(BASE + "video/" + str(video_stats), data[video_stats]) 
    print(response.json())

input()

#Updating a video
response = requests.patch(BASE + "video/2", {"name": "ELITE", "views": 31337, "likes": 31337}) 
print(response.json())
# You dont need to update all the fields, you can update only one or two fields. Like this: {"name": "ELITE"} that only update the name of the video.

input()

#Checking if it was updated
for video_stats in range (len(data)):
    response = requests.get(BASE + "video/" + str(video_stats), data[video_stats]) 
    print(response.json())

input()

response = requests.delete(BASE + "video/2")
print(response)

input()

#Checking if it was deleted
for video_stats in range (len(data)):
    response = requests.get(BASE + "video/" + str(video_stats), data[video_stats]) 
    print(response.json())