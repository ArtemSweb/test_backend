import json
import requests

class PetstorePetHelper:
    def __init__(self, app):
        self.app = app

    def get_petId(self, petId):
        path = '/pet/' + str(petId)
        headers = {"Content-Type": "application/json"}
        req = requests.get(self.app.hostPetstore + path, headers=headers)
        return req

    def post_pet(self, petId, petName):
        path = '/pet'
        headers = {"Content-Type": "application/json"}
        body = {
                  "id": petId,
                  "category": {
                    "id": 0,
                    "name": "Корги"
                  },
                  "name": petName,
                  "photoUrls": [
                    "string"
                  ],
                  "tags": [
                    {
                      "id": 0,
                      "name": "string"
                    }
                  ],
                  "status": "available"
                }
        req_body = json.dumps(body)
        req = requests.post(self.app.hostPetstore + path, data=req_body, headers=headers)
        return req

    def post_petId(self, petId, petName, status):
        path = f'/pet/{str(petId)}'
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {'name': petName, 'status': status}
        req = requests.post(self.app.hostPetstore + path, headers=headers, data=data)
        return req

