from chatbot import Chatbot
from .pet_names import pet_names
from .pet_types import pet_types

def number_of_pets(chatbot: Chatbot):
  pets = chatbot.require_number("How many pets do you have? (just a sum)", "number_of_pets")

  if pets == 0:
    chatbot.send(":(")
  elif pets == 1:
    chatbot.send("My creator also has one pet; a dog named Rudy.")
  elif pets <= 3:
    chatbot.send("Pets are great :D")
  else:
    chatbot.send("That's a lot of animals to have.")
  
  if pets > 0:
    pet_names(chatbot)
    pet_types(chatbot)
