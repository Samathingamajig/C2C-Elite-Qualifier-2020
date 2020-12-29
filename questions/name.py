from chatbot import Chatbot

def name(chatbot: Chatbot):
  greeting, my_name_is, whats_your_name = chatbot.random_phrases("greetings", "my_name_is", "whats_your_name")
  my_name_is = my_name_is.format(name=chatbot.name)
  chatbot.send(f"{greeting}. {my_name_is}. {whats_your_name}?")
  chatbot.user.name = input()
  chatbot.send(f"Well hello there, {chatbot.user.name}!")