from chatbot import Chatbot
import re

def pokemon(chatbot: Chatbot):
  like_pokemon = chatbot.require_boolean("Do you like Pokemon?", None)
  if not like_pokemon:
    chatbot.require_string("Why don't you like Pokemon?", None)
    chatbot.send("Can't talk about stuff you don't like then...")
  else:
    games_played = chatbot.require_string("What Pokemon games have you played? (say \"None\" if you haven't played any)", None, lowercase=True)
    if re.search(r"none", games_played) is not None: # the search for "none" results in None if "none" is not found
      chatbot.send("I would highly recommend playing at least one Pokemon game.")
      chatbot.require_string("What's the reason you haven't played any Pokemon games?", None)
    else:
      chatbot.send("That's great!")
    chatbot.require_string("What do you think of the anime?", None)
    chatbot.require_string("What do you think of the trading card game?", None)