import json
import requests

class PetstoreStoreHelper:
    def __init__(self, app):
        self.app = app

    def get_storeInventory(self):
        path = '/store/inventory'
        headers = {"Content-Type": "application/json"}
        req = requests.get(self.app.hostPetstore + path, headers=headers)
        return req
