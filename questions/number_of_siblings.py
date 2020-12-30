from chatbot import Chatbot
from .youngest_or_oldest import youngest_or_oldest

def number_of_siblings(chatbot: Chatbot):
  how_many_siblings = chatbot.random_phrases("how_many_siblings")
  chatbot.require_number(f"{how_many_siblings}? (just a sum)", "number_of_siblings")

  if chatbot.user.number_of_siblings == 0:
    chatbot.send("It must be interesting being an only child.")
  elif chatbot.user.number_of_siblings == 1:
    chatbot.send("Nice.")
    youngest_or_oldest(chatbot)
  elif chatbot.user.number_of_siblings == 2:
    chatbot.send("That's the same number of siblings as my creator!")
  else:
    chatbot.send("That's a lot of people that you can depend on.")