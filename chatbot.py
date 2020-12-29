import random
import os
from user import User
from time import sleep
from importlib import import_module
import re

questions = None

class Chatbot:
  def __init__(self, name_of_bot):
    self.name = name_of_bot
    self.user = User()
    self.sleep = lambda: sleep(0.3)
    global questions
    questions = import_module("questions") # I have to do this to avoid a circular import
  
  def start(self):
    questions.name(self)
    questions.age(self)
    questions.number_of_siblings(self)
    questions.number_of_pets(self)
  
  def random_phrases(self, *phrases):
    random_list = []
    for phrase in phrases:
      with open(f"{os.path.join('phrases', phrase)}.txt", "r") as file:
        options = file.read().splitlines() # file.readlines() keeps the '\n' character
        random_list.append(random.choice(options))
      if len(phrases) == 1:
        return random_list[0]
    return random_list
  
  def send(self, *strings):
    self.sleep()
    print(" ".join(strings))
  
  def require_number(self, prompt, key_to_modify_as_string):
    self.send(prompt)
    while not (respone_has_number := False):
      response = input()
      number = re.search(r"\d+", response)
      if number is not None:
        if key_to_modify_as_string is not None and key_to_modify_as_string != "":
          setattr(self.user, key_to_modify_as_string, int(number.group()))
        return int(number.group())
      self.send("Please answer with digits (0-9)")
  
  def require_from_list(self, prompt, key_to_modify_as_string, *options):
    self.send(prompt)
    regex = r"|".join(list(map(lambda s: s.lower(), options)))
    while not (response_has_valid_option := False):
      response = input().lower()
      answer = re.search(regex, response)
      if answer is not None:
        if key_to_modify_as_string is not None and key_to_modify_as_string != "":
          setattr(self.user, key_to_modify_as_string, answer.group())
        return answer.group()
      self.send(f"Please one of the following strings in your response: {', '.join(options)}")