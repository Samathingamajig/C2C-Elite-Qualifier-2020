from chatbot import Chatbot

def candy(chatbot: Chatbot):
  like_candy = chatbot.require_boolean("Do you like candy?", None)
  if not like_candy:
    chatbot.require_string("Why do you not like candy?", None)
    chatbot.send("Well, I guess there's not much to talk about if you don't like candy.")
  else:
    chatbot.require_from_list("Do you prefer chocolate or fruit flavored candy?", None, "Chocolate", "Fruit")
    chatbot.require_string("What is your favorite candy?", None)
    chatbot.send(f"My favorite kind of candy is a {chatbot.random_topics_list('candies')}")    