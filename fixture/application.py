from fixture.petstore_pet import PetstorePetHelper

class Application:
#переменные в petstore.swagger.io/v2
    hostPetstore = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.petstore_pet = PetstorePetHelper(self)