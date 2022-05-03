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

    def get_storeOrderById(self, orderId):
        path = '/store/order/' + str(orderId)
        headers = {"Content-Type": "application/json"}
        req = requests.get(self.app.hostPetstore + path, headers=headers)
        return req

    def post_storeOrder(self, orderId, petId, quantity, status, complete):
        path = 'store/order'
        headers = {"Content-Type": "application/json"}
        body = {
                "id": orderId,
                "petId": petId,
                "quantity": quantity,
                "shipDate": "2022-05-03T21:03:36.568Z",
                "status": status,
                "complete": complete
            }
        req_body = json.dumps(body)
        req = requests.post(self.app.hostPetstore + path, data=req_body, headers=headers)
        return req
