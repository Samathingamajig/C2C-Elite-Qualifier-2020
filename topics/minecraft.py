from chatbot import Chatbot

def minecraft(chatbot: Chatbot):
  like_minecraft = chatbot.require_boolean("Do you like Minecraft?", None)
  if not like_minecraft:
    chatbot.require_string("Why don't you like Minecraft?", None)
    chatbot.send(":(")
  else:
    own_game = chatbot.require_boolean("Do you own any copy of Minecraft?", None)
    if own_game:
      year_gotten = chatbot.require_number("What year did you buy (or get gifted) Minecraft (for the first time)?", None)
      if year_gotten < 2009: chatbot.send("Wow, you got the game before Notch started development. GG")
      elif year_gotten == 2009: chatbot.send("That's amazing that you got the game within the first year!")
      elif year_gotten < 2015: chatbot.send("Hello, veteran.")
      elif year_gotten <= 2021: chatbot.send("It's such a great game, good job!")
      else: chatbot.send("You must be from the future?")

      chatbot.require_from_list("What console (PC/Mobile/XBox/PlayStation/Wii U/Windows 10) did you first own Minecraft for?", None, "PC", "Mobile", "XBox", "PlayStation", "Wii U", "Windows 10")
      chatbot.require_string(f"What's your favorite block? Mine's {chatbot.random_topics_list('minecraft_blocks')}.")

    else:
      chatbot.send("Oh no. Hopefully you'll be gifted a copy or buy one soon!")