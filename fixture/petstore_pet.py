import json
import requests

class PetstorePetHelper:
    def __init__(self, app):
        self.app = app

    def get_pet_id(self, petId):
        path = '/pet/' + str(petId)
        headers = {"Content-Type": "app;ication/json"}
        req = requests.get(self.app.hostPetstore + path, headers=headers)
        return req