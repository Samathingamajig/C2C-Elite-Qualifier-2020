from chatbot import Chatbot
import re

def dogs(chatbot: Chatbot):
  like_dogs = chatbot.require_boolean("Do you like dogs?", None)
  number_of_dogs = len(list(filter(lambda pet_type: re.search(r"dog", pet_type) is not None, chatbot.user.pet_types))) if chatbot.user.number_of_pets != 0 else 0
  if number_of_dogs == 1: index_of_dog = [i for i, pet_type in enumerate(chatbot.user.pet_types) if re.search(f"dog", pet_type)][0]
  if like_dogs:
    if number_of_dogs == 0:
      chatbot.send("You should consider getting a dog since you like them but don't have any yet.")
    elif number_of_dogs == 1:
      chatbot.send(f"That's great, considering that {chatbot.user.pet_names[index_of_dog]} is a dog.")
    else:
      chatbot.send(f"That's great, considering that you have {number_of_dogs} dogs.")
  else:
    if number_of_dogs == 0:
      chatbot.send("I guess that was clear by you not having any dogs.")
    elif number_of_dogs == 1:
      chatbot.send(f"That's strange, considering that you have a dog, {chatbot.user.pet_names[index_of_dog]}.")
    else:
      chatbot.send(f"That's strange, considering that you have {number_of_dogs} dogs.")
  
  played_fetch = chatbot.require_boolean("Have you ever played fetch with a dog?", None)
  if played_fetch:
    chatbot.send("That's great!")
    toy = chatbot.require_from_list("What kind of toy/object did you throw that got fetched?", None, "Tennis ball", "Rope", "Stick", "Bone", "Other")
    if toy == "other":
      chatbot.require_string("What did you throw then?", None)
      chatbot.send("Interesting, I never thought about using that.")
    else:
      chatbot.send("That's a classic :)")
  else:
    if number_of_dogs != 0:
      chatbot.send(f"But you have {'a dog' if number_of_dogs == 1 else str(number_of_dogs) + ' dogs'}!")
    else:
      chatbot.send("I guess that's expected if you don't have any dogs.")
  
  if like_dogs:
    chatbot.require_string("What's your favorite dog breed?", None)
    chatbot.send(f"My favorite dog breed is the {chatbot.random_topics_list('dog_breeds')}.")