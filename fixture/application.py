from fixture.petstore_pet import PetstorePetHelper
from fixture.petstore_store import PetstoreStoreHelper
from fixture.petstore_user import PetstoreUserHelper
from fixture.get_datas import datasHelper

class Application:
#переменные в petstore.swagger.io/v2
    hostPetstore = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.get_datas = datasHelper(self)

        self.petstore_pet = PetstorePetHelper(self)
        self.petstore_store = PetstoreStoreHelper(self)
        self.petstore_user = PetstoreUserHelper(self)
