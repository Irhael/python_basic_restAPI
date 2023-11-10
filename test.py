import requests # import requests module, that allows to send HTTP requests using Python

BASE = "http://127.0.0.1:5000/" # This is the base url to access the server and the flask application.

# put is used to update the data in the server and the flask application. The first parameter is the url to access the resource and the second is the data that will be updated.

data = [{"name": "video00", "likes": 14, "views": 200000}, 
        {"name": "video01", "likes": 10, "views": 10000000}, 
        {"name": "video02", "likes": 15, "views": 7000000}] 


for i in range (len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i]) #http://http://127.0.0.1:5000/video/video_id/data[i]
    print(response.json())

input()

response = requests.delete(BASE + "video/0")
print(response)

input()

response = requests.get(BASE + "video/2")
print(response.json()) 

input()

for i in range (len(data)):
    response = requests.get(BASE + "video/" + str(i), data[i]) 
    print(response.json()) 
    