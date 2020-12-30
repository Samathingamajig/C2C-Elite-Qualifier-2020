import os
import re

with open("topics/topics_list.txt", "r") as topic_list_file:
  topics = topic_list_file.read().splitlines()
  for topic in topics:
    if topic.strip() == "": continue
    topic = re.sub(r"\W+", "_", topic).lower().strip("_")
    print(topic, os.path.exists(f"topics/{topic}.py"))
    if os.path.exists(f"topics/{topic}.py"): continue
    with open(f"topics/{topic}.py", "w") as topic_file:
      topic_file.write(f"""\
from chatbot import Chatbot

def {topic}(chatbot: Chatbot):
  chatbot.send("Blank topic {topic}")\
""")
