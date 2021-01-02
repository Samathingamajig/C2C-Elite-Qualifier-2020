from chatbot import Chatbot

def apples_the_fruit(chatbot: Chatbot):
  like_apples = chatbot.require_boolean("Do you like apples?", None)
  if not like_apples:
    chatbot.require_string("Why not?", None)
    chatbot.send("I guess that's okay.\nThere's not much more to talk about apples if you don't like them.")
  else:
    chatbot.send("Me too!")
    chatbot.require_from_list("What is your favorite color of apple?", None, "Red", "Green", "Mixed")
    number_of_apples = chatbot.require_number("How many apples do you eat weekly?", None)
    if number_of_apples <= 8:
      chatbot.send('They say "An apple a day keeps the doctor away" :D')
    elif number_of_apples <= 15:
      chatbot.send("The doctors must really want to stay away from you ;D")
    else:
      chatbot.send("The doctors must stay 5 billion lightyears away from you!")
    chatbot.require_string("What's your favorite kind of apple?", None)
    chatbot.send(f"Nice. Mine's {chatbot.random_topics_list('apple_types')}.")