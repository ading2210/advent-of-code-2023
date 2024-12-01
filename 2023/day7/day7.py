import re
import pathlib
#from functools import cmp_to_key

lines = pathlib.Path("data.txt").read_text().split("\n")
joker_rule = False

def get_type(hand):
  if joker_rule and "J" in hand:
    possible_cards = "AKQT98765432"
    possible_types = [get_type(hand.replace("J", card)) for card in possible_cards]
    return max(possible_types)

  cards = {}
  for card in hand:
    if card in cards:
      cards[card] += 1
    else:
      cards[card] = 1
  
  counts = sorted(list(cards.values()), reverse=True)
  return counts

def card_strength(card):
  if joker_rule:
    card_rankings = "AKQT98765432J"
  else:
    card_rankings = "AKQJT98765432"
  return len(card_rankings) - card_rankings.find(card)

#custom comparator for list.sort
def hand_comparator(item):
  hand = item[0]
  hand_type = get_type(hand)
  card_strengths = [card_strength(card) for card in hand]

  return (hand_type, *card_strengths)

def get_total():
  hands = []
  for line in lines:
    line_split = line.split()
    hands.append([line_split[0], int(line_split[1])])
  hands.sort(key=hand_comparator)

  total = 0
  for i, (hand, bid) in enumerate(hands):
    rank = i + 1
    winnings = rank * bid
    total += winnings

  return total

def part1():
  print(get_total())

def part2():
  global joker_rule
  joker_rule = True
  print(get_total())

part1()
part2()