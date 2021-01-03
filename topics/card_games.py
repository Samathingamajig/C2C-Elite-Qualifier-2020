from chatbot import Chatbot

def card_games(chatbot: Chatbot):
  like_card_games = chatbot.require_boolean("Do you like card games?", None)
  if not like_card_games:
    chatbot.require_string("Why don't you like them?", None)
    chatbot.send("Okay then...")
  else:
    my_fav_game = chatbot.random_topics_list('card_games')
    chatbot.send(f"My favorite card game is {my_fav_game}.")
    same_fav_game = chatbot.require_boolean("Is that also your favorite card game?", None)
    if not same_fav_game: chatbot.require_string("What's yours then?", None)
    chatbot.require_from_list("In general, do you prefer single player or multiplayer games?", None, "Single Player", "Multiplayer")
    chatbot.require_from_list("In general, do you prefer card games, board games, or video games?", None, "Card", "Board", "Video")