class User:
  def __init__(self):
    self.name = None
    self.age = None
    self.gender = None
    self.number_of_siblings = None
    self.number_of_pets = None
    self.pet_names = None
    self.pet_types = None
    self.interests = None
  
  def json(self):
    return {
      "name": self.name,
      "age": self.age,
      "gender": self.gender,
      "number_of_siblings": self.number_of_siblings,
      "number_of_pets": self.number_of_pets,
      "pet_names": self.pet_names,
      "interests": self.interests,
    }