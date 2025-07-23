import requests

url = "http://localhost:5000/update"

def update():
    data = {
        "active": False,
        "lock": True,
        "message": "Unauthorized usage. App locked"
    }
    response = requests.post(url, json=data)
    print(response.json())

def allow():
    data = {
        "active": True,
        "lock": False,
        "message": "Go"
    }
    response = requests.post(url, json=data)
    print(response.json())

msg = input("msg: ")

if msg.lower() == "lock":
    update()
else:
    allow()

