import requests
import json

url = "https://jsonplaceholder.typicode.com/comments"

params = {
    "postId": 50
}

response = requests.get(url, params)
data = response.json()

print(json.dumps(data, indent=4, ensure_ascii=False))

with open("task 3.html", "w", encoding="utf-8") as fl:
    fl.write(response.text)