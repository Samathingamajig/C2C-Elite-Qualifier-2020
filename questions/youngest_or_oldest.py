from chatbot import Chatbot

def youngest_or_oldest(chatbot: Chatbot):
  response = chatbot.require_from_list("Are you the oldest or the youngest sibling?", None, "youngest", "oldest")
  if response == "youngest":
    chatbot.send("My creator is also the youngest sibling :D")
  elif response == "oldest":
    chatbot.send("You're lucky...")