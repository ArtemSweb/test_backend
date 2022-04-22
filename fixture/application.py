from fixture.petstore_pet import PetstorePetHelper
from fixture.petstore_store import PetstoreStoreHelper
from fixture.petstore_user import PetstoreUserHelper

class Application:
#переменные в petstore.swagger.io/v2
    hostPetstore = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.petstore_pet = PetstorePetHelper(self)
        self.petstore_store = PetstoreStoreHelper(self)
        self.petstore_user = PetstoreUserHelper(self)