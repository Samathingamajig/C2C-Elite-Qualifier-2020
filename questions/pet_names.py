from chatbot import Chatbot

def pet_names(chatbot: Chatbot):
  if chatbot.user.number_of_pets == 1:
    chatbot.require_string("What is the name of your pet?", "pet_names", save_as_list=True)
  else:
    chatbot.require_list_of_size("What are the names of your pets?", "pet_names", chatbot.user.number_of_pets)