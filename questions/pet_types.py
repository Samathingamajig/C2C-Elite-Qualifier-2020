from chatbot import Chatbot

def pet_types(chatbot: Chatbot):
  if chatbot.user.number_of_pets == 1:
    chatbot.require_string(f"What kind of animal is {chatbot.user.pet_names[0]}?", "pet_types", save_as_list=True)
  else:
    chatbot.require_from_list(f"What kind(s) of animals are your pets?", "pet_types")