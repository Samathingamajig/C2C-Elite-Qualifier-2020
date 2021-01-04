from chatbot import Chatbot
import re

def age(chatbot: Chatbot):
  how_old_are_you = chatbot.random_phrases("how_old_are_you")
  chatbot.require_number(f"{how_old_are_you}?", "age")
  
  if chatbot.user.age == 0:
    chatbot.send("That's a very interesting age...")
  elif chatbot.user.age < 13:
    chatbot.send("You're kinda young to be using this chatbot, and even the internet in general.")
  elif chatbot.user.age == 15:
    chatbot.send("Hey, you're the same age as my creator!")
  elif chatbot.user.age < 20:
    chatbot.send("My creator is also a teenager, so that's cool.")
  elif chatbot.user.age > 150:
    chatbot.send("Is that even possible? I have no way to fact check this, but I'm pretty sure you're lying to me, and that makes me sad :(")
  else:
    chatbot.send("You're older than my creator!")

  chatbot.send(f"Well, I'm zero years old. To be more precise, I'm only a couple of weeks old.")