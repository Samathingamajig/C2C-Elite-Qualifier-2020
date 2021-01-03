import random

def get_scores(mini_deck):
  score = 0
  aces = 0
   # print("mini_deck", mini_deck)
  for card in mini_deck:
     # print("card", card)
    if str.isdigit(card):
      score += int(card)
       # print("number")
    elif card == "A":
      aces += 1
       # print("ace")
    else:
      score += 10
       # print("face")
     # print("score:", score)
     # print("aces:", aces)
  scores = [score]
   # print("scores", scores)
  for _ in range(aces):
    temp_scores = scores[:]
    scores = []
    for score in temp_scores:
      scores.append(score + 1)
      scores.append(score + 11)
     # print("scores", scores)
  scores = [score for index, score in enumerate(scores) if score not in scores[index+1:]]
   # print("final_scores", scores)
  scores.sort()
   # print("set_scores", scores)
  return scores

def print_table(human_deck, comp_deck, player_still_hitting=False):
  human_scores = get_scores(human_deck)
  if len(human_scores) > 1:
    print("Your possible scores are: ", end="")
  else:
    print("Your score is:\t", end="")
  print(" or ".join(map(str, human_scores)))
  print(f"Your hand is:\t{' '.join(human_deck)}")
  if player_still_hitting:
    print(f"My score is at least: {' or '.join(map(str, get_scores([comp_deck[0]])))}")
    print(f"My hand is:\t{comp_deck[0]} X")
  else:
    comp_scores = get_scores(comp_deck)
    if len(comp_scores) > 1:
      print("My possible scores are ", end="")
    else:
      print("My score is:\t", end="")
    print(" or ".join(map(str, comp_scores)))
    print(f"My hand is:\t{' '.join(comp_deck)}")

deck = None
human_deck = None
comp_deck = None
human_final_score = None
comp_final_score = None
human_5_cards = False
comp_5_cards = False

def blackjack():
  global deck, human_deck, comp_deck, human_final_score, comp_final_score, human_5_cards, comp_5_cards
  deck = "A 2 3 4 5 6 7 8 9 10 J Q K".split(" ") * 4
  for _ in range(5):
    random.shuffle(deck)
  deck = iter(deck)
  human_deck = [next(deck), next(deck)]
  comp_deck = [next(deck), next(deck)]
  human_final_score = None
  comp_final_score = None
  human_5_cards = False
  comp_5_cards = False
  while (player_still_hitting := True):
    print()
    print_table(human_deck, comp_deck, player_still_hitting)
    print()
    hit = None
    while (awaiting_valid_response := True):
      response = input("Do you want to hit or stand? ").lower()
      if response[:3] == "hit":
        hit = True
        break
      elif response[:5] == "stand":
        hit = False
        break
      else:
        print("Invalid response, please try again")
    if hit:
      human_deck.append(next(deck))
    human_scores = get_scores(human_deck)
    valid_human_scores = [score for score in human_scores if score <= 21]
    invalid_human_scores = [score for score in human_scores if score not in valid_human_scores]
    if len(valid_human_scores) == 0 or 21 in valid_human_scores or not hit or len(human_deck) == 5:
      if len(valid_human_scores) > 0:
        human_final_score = max(valid_human_scores)
        if len(human_deck) == 5:
          human_5_cards = True
      else: human_final_score = min(invalid_human_scores)
      break
  
  while (comp_still_hitting := True):
    print()
    print_table(human_deck, comp_deck)
    print()
    comp_scores = get_scores(comp_deck)
    scores_17_through_21 = [score for score in comp_scores if 17 <= score <= 21]
    scores_less_than_17 = [score for score in comp_scores if score < 17]
    has_17_through_21 = len(scores_17_through_21) > 0
    has_less_than_17 = len(scores_less_than_17) > 0
    if human_final_score >= 21 or human_5_cards or human_final_score < max([*scores_17_through_21, *scores_less_than_17]):
      comp_final_score = max([*scores_17_through_21, *scores_less_than_17])
      break
    elif has_17_through_21:
      print("Since I have a score between 17 and 21, I must stand.\n")
      comp_final_score = max(scores_17_through_21)
      break
    elif not has_less_than_17:
      invalid_comp_scores = [score for score in comp_scores if score > 21]
      comp_final_score = min(invalid_comp_scores)
      break
    elif len(comp_deck) == 5:
      comp_final_score = max(scores_less_than_17)
      comp_5_cards = True
      break
    else:
      print(f"Since I have a score of 16 or below, I must hit.")
      comp_deck.append(next(deck))

  
  print("Final hands:")
  print_table(human_deck, comp_deck)
  print()
  print("Final Scores:")
  print(f"You:\t{human_final_score}")
  print(f"Me:\t{comp_final_score}")
  print()
  if (human_final_score > comp_final_score or comp_final_score > 21) and human_final_score <= 21:
    print("You win! Congratulations!")
  elif (comp_final_score > human_final_score or human_final_score > 21) and comp_final_score <= 21:
    print("I win! Good game!")
  else:
    print("We tied! Good game.") 
  if human_5_cards or comp_5_cards: print("(This win was because of drawing 5 cards and not going over 21)")

if __name__ == "__main__":
  blackjack()