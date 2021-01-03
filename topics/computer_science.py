from chatbot import Chatbot
import re

def computer_science(chatbot: Chatbot):
  like_comp_sci = chatbot.require_boolean("Do you like Computer Science?", None)
  if not like_comp_sci:
    chatbot.require_string("Why not?", None)
    chatbot.send("I guess not everyone has the same tastes.")
  else:
    software_or_webdev_or_other = chatbot.require_from_list("What do you do the most work on? (Software, WebDev, or Other)", None, "Software", "WebDev", "Other")
    if software_or_webdev_or_other == "other":
      chatbot.require_string("What do you work on then?", None)
    chatbot.send(f"My favorite language is {chatbot.random_topics_list('programming_languages')}.")
    chatbot.require_string("What's yours?", None)
    favorite_editor = chatbot.require_string("What's your favorite code editor?", None, lowercase=True)
    if re.search(r"vs ?code|visual ?studio ?code", favorite_editor) is None:
      chatbot.require_string("Why do you prefer that editor over VSCode?", None)
    else:
      chatbot.send("My creator used that to make me!")