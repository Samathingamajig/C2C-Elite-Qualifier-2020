from chatbot import Chatbot

def sodas(chatbot: Chatbot):
  like_soda = chatbot.require_boolean("Do you like soda?", None)
  if not like_soda:
    chatbot.require_string("Why do you not like soda?", None)
    chatbot.send("Well I guess that I can't talk to you about soda if you don't like it.")
  else:
    coke_pepsi_neither = chatbot.require_from_list("Are you more of a Coke person, a Pepsi person, or neither?", None, "Coke", "Pepsi", "Neither")
    if coke_pepsi_neither == "coke":
      coke_fav = chatbot.require_boolean("Is Coke your favorite soda in general?", None)
      if not coke_fav:
        chatbot.require_string("What is your favorite soda then?", None)
    elif coke_pepsi_neither == "pepsi":
      pep_fav = chatbot.require_boolean("Is Pepsi your favorite soda in general?", None)
      if not pep_fav:
        chatbot.require_string("What is your favorite soda then?", None)
    else:
      chatbot.require_string("What is your favorite soda?", None)
    chatbot.send(f"My favorite soda is {chatbot.random_topics_list('sodas')}.")