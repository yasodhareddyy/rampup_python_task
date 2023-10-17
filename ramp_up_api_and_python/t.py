import json

import requests

#url = 'http://localhost:5000'
#url="https://dummyapi.online/api/movies/1"

#res=requests.get(url)
#print(res.json())
#create_data=requests.post("https://jsonplaceholder.typicode.com/posts/",data={"id":1,"movie":"xxxxxxxxxxxxxxxxxxxxxxxxx","rating":9.2,"image":"images/shawshank.jpg","imdb_url":"https://www.imdb.com/title/tt0111161/"})

#print(create_data.status_code)
# res=requests.get(f'{url}/books/4')
# print(res.json())
#
# data={"id":1011,"book_name":"aaaaaa","author":"bbbbbbbbb"}
# headers = {"Content-Type": "application/json"}
#
# res=requests.post(f'{url}/books',data=data,headers=headers)
#res.json()
# Define new data to create
new_data = {
    "userID": 1,
    "id": 1,
    "title": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx a POST request",
    "body": "This is the data we created."
}

# The API endpoint to communicate with
url_post = "https://jsonplaceholder.typicode.com/posts"

# A POST request to tthe API
post_response = requests.post(url_post, json=new_data)

# Print the response
post_response_json = post_response.json()
print(post_response_json)