import random
import os
from user import User
from time import sleep
from importlib import import_module
import re
import math
import games

questions = None
topics = None

def print3(list_to_print):
  # Prints a list in groups a 3 then a newline
  print(",\n".join([", ".join(list_to_print[i*3:i*3+3]) for i in range(math.ceil(len(list_to_print)/3))]))

class Chatbot:
  def __init__(self, name_of_bot):
    self.name = name_of_bot
    self.user = User()
    self.sleep = lambda: sleep(0.3)
    global questions, topics
    # I have to do this to avoid a circular import
    questions = import_module("questions")
    topics = import_module("topics")
  
  def start(self):
    questions.name(self)
    questions.age(self)
    questions.number_of_siblings(self)
    questions.number_of_pets(self)

    while len(topics.topics_list) > 0:
      self.send()
      self.send(f"What do you want to talk about? Your available options are:")
      print3(topics.topics_list)
      self.send("You can also say \"Stop talking\" to continue on.")
      topic = self.require_from_list(None, None, *topics.topics_list, error="Please enter a valid topic from the list above.", stop="talking")
      if topic == "stop":
        break
      topics.topics_list = list(filter(lambda t: t.lower() != topic, topics.topics_list))
      topic = re.sub(r"\W+", "_", topic).strip("_")
      getattr(topics, topic)(self)
    
    self.send("\nIt's been great talking to you!")
    want_to_play_games = self.require_boolean("Do you want to play any games? (\"no\" will exit the program)", None)
    while want_to_play_games:
      self.send()
      self.send("What game do you want to play? Your available options are:")
      print3(games.games_list)
      self.send("(You can also say \"Stop gaming\" to exit)")
      game = self.require_from_list(None, None, *games.games_list, error="Please enter a valid game from the list above.", stop="gaming").lower()
      if game == "stop":
        break
      getattr(games, game)()
    self.send("Alright, goodbye forever!")

  
  def random_phrases(self, *phrases):
    return self._random_from_path("phrases", *phrases)
  
  def random_topics_list(self, *filenames):
    return self._random_from_path("topics_random", *filenames)

  def _random_from_path(self, base_path, *filenames):
    random_list = []
    for filename in filenames:
      with open(f"{os.path.join(base_path, filename)}.txt", "r") as file:
        options = file.read().splitlines() # file.readlines() keeps the '\n' character
        options = list(filter(lambda option: not option.startswith("#") and option.strip() != "", options))
        random_list.append(random.choice(options))
      if len(filenames) == 1:
        return random_list[0]
    return random_list
  
  def send(self, *strings):
    self.sleep()
    print(" ".join(strings))
  
  def require_number(self, prompt, key_to_modify_as_string):
    if prompt: self.send(prompt)
    while not (respone_has_number := False):
      response = input()
      number = re.search(r"\d+", response)
      if number is not None:
        if key_to_modify_as_string is not None and key_to_modify_as_string != "":
          setattr(self.user, key_to_modify_as_string, int(number.group()))
        return int(number.group())
      self.send("Please answer with digits (0-9)")
  
  def require_from_list(self, prompt, key_to_modify_as_string, *options, error=None, stop=False):
    if prompt: self.send(prompt)
    regex = r"|".join(list(map(lambda s: re.escape(s.lower()), options)))
    while not (response_has_valid_option := False):
      response = input().lower()
      answer = re.search(regex, response)
      if answer is not None:
        if key_to_modify_as_string is not None and key_to_modify_as_string != "":
          setattr(self.user, key_to_modify_as_string, answer.group())
        return answer.group()
      if stop is not False and re.search(r"stop\s*"+stop, response) is not None:
        return "stop"
      self.send(error or f"Please one of the following strings in your response: {', '.join(options)}")
  
  def require_list_of_size(self, prompt, key_to_modify_as_string, list_size):
    if prompt: self.send(f"{prompt}\n(separate with commas, and *don't* include the word 'and' for the last item)")
    while not (response_is_proper_list_size := False):
      response = input()
      listified = re.split(r",\s*", response)
      if len(listified) == list_size:
        if key_to_modify_as_string is not None and key_to_modify_as_string != "":
          setattr(self.user, key_to_modify_as_string, listified)
        return listified
      self.send(f"Please make a list of size {list_size} that is separated with commas\n(spaces are optional, but don't include 'and' for the last item)")
  
  def require_string(self, prompt, key_to_modify_as_string, lowercase=False, save_as_list=False):
    if prompt: self.send(prompt)
    while not (response_is_valid := False):
      response = input().strip()
      if lowercase: response = response.lower()
      if response != "":
        if key_to_modify_as_string is not None and key_to_modify_as_string != "":
          setattr(self.user, key_to_modify_as_string, response if not save_as_list else [response])
        return response if not save_as_list else [response]
      self.send("Please return a word/phrase that isn't just whitespace/blank.")
  
  def require_boolean(self, prompt, key_to_modify_as_string):
    if prompt: self.send(prompt)
    while not (response_is_boolean := False):
      response = input().strip().lower()
      match = re.search(r"yes|no", response)
      if match is not None:
        if match.group() == "yes": result = True
        else: result = False
        if key_to_modify_as_string is not None and key_to_modify_as_string != "":
          setattr(self.user, key_to_modify_as_string, result)
        return result
      self.send("Please respond with a yes or a no.")
