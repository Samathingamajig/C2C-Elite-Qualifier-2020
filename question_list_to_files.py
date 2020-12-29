import os

with open("questions/question_list.txt", "r") as question_list_file:
  questions = question_list_file.read().splitlines()
  for question in questions:
    if question.strip() == "": continue
    print(question, os.path.exists(f"questions/{question}.py"))
    if os.path.exists(f"questions/{question}.py"): continue
    with open(f"questions/{question}.py", "w") as question_file:
      question_file.write(f"""\
from chatbot import Chatbot

def {question}(chatbot: Chatbot):
  chatbot.send("Blank question {question}")\
""")
