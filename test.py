import unittest
import os
import sys
from chatbot import Chatbot
from contextlib import contextmanager

@contextmanager
def stdin_changer(input_file):
  old_stdin = sys.stdin
  try:
    sys.stdin = open(f"tests/{input_file}", "r")
    yield
  finally:
    sys.stdin.close()
    sys.stdin = old_stdin

class TestRequireBoolean(unittest.TestCase):
  def test_yes(self):
    chatbot = Chatbot("")
    (_, _, filenames) = next(os.walk("tests/rb/yes"))
    for file in filenames:
      with stdin_changer(f"rb/yes/{file}"):
        self.assertTrue(chatbot.require_boolean("a yes or no question", None))
  
  def test_none(self):
    chatbot = Chatbot("")
    (_, _, filenames) = next(os.walk("tests/rb/none"))
    for file in filenames:
      with stdin_changer(f"rb/none/{file}"):
        with self.assertRaises(EOFError):
          chatbot.require_boolean("a yes or no question", None)
  
  def test_no(self):
    chatbot = Chatbot("")
    (_, _, filenames) = next(os.walk("tests/rb/no"))
    for file in filenames:
      with stdin_changer(f"rb/no/{file}"):
        self.assertFalse(chatbot.require_boolean("a yes or no question", None))

if __name__ == "__main__":
  unittest.main()

