class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self
        self.pets_list.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type. Valid types are {', '.join(Pet.PET_TYPES)}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Add pet to the class variable all
        Pet.all.append(self)

        # If an owner is provided, assign the pet to the owner
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            owner.add_pet(self)


# Example usage
try:
    owner1 = Owner("Alice")
    pet1 = Pet("Buddy", "dog", owner1)
    pet2 = Pet("Whiskers", "cat", owner1)

    owner1.add_pet(pet1)
    owner1.add_pet(pet2)

    print([pet.name for pet in owner1.get_sorted_pets()])
except Exception as e:
    print(e)
