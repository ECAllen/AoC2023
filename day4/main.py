
with open("input.txt") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    card_id, cards = line.split(":")
    winning_card,card = cards.split("|")
    winning_card = winning_card.strip()
    winning_card = winning_card.split()
    card = card.strip()
    card = card.split()

    winning_nums = [c for c in card if c in winning_card]
    if len(winning_nums) > 0:
        if len(winning_nums) == 1:
            points = 1
        else:
            points = 2**(len(winning_nums) - 1)
        total += points
print(total)

# Part 2
import re

class Card:
    def __init__(self, card_id, nums):
        self.card_id = card_id
        self.winning_nums = nums 
        self.num = 1

    def length(self):
        return len(self.winning_nums)

    def __repr__(self):
        return f"id: {self.card_id} num: {self.num} winnings: {self.winning_nums}"

total = 0
id_re = re.compile(r"(\d+)")
winnings = {}
for line in lines:
    card_id, cards = line.split(":")
    card_id = card_id.strip()
    card_id = int(id_re.search(card_id).group(1))
    winning_card,card = cards.split("|")
    winning_card = winning_card.strip()
    winning_card = winning_card.split()
    card = card.strip()
    card = card.split()

    winning_nums = [c for c in card if c in winning_card]
    winnings[card_id] = Card(card_id, winning_nums)

for card in winnings:
    if winnings[card].length() > 0:
        for i in range(winnings[card].num):
            for j in range(1, winnings[card].length() + 1):
                winnings[card+j].num += 1
                # print(winnings[card])
    # if card > 5:
    #    break
for card in winnings:
    total += winnings[card].num
       #  total += 2**(winnings[card].length() - 1) * winnings[card].num
# print(winnings)
print(total)

