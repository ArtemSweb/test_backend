import json
import requests

class PetstoreUserHelper:
    def __init__(self, app):
        self.app = app

    def post_user(self, userId, userName, firstName, lastName, email, password, phone):
        path = '/user'
        headers = {"Content-Type": "application/json"}
        body = {
              "id": userId,
              "username": userName,
              "firstName": firstName,
              "lastName": lastName,
              "email": email,
              "password": password,
              "phone": phone,
              "userStatus": 0
            }
        req_body = json.dumps(body)
        req = requests.post(self.app.hostPetstore + path, data=req_body, headers=headers)
        return req