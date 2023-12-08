
import collections

with open('input.txt') as f:
    lines = f.read().splitlines()

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards 
        self.strength = 0 
        self.bid = int(bid)
        self.hand_type = self.find_type()
        self.ranks = self.card_ranks()

    def card_ranks(self):
        ranks = []
        lookup = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        for c in self.cards:
            if c.isdigit():
                ranks.append(int(c))
            else:
                ranks.append(lookup[c])
        return ranks

    def __repr__(self):
        return f'{self.cards} {self.bid} {self.strength} {self.hand_type} {self.ranks}'

    def find_type(self):
        d = collections.defaultdict(int)
        for c in self.cards:
            d[c] += 1
        types = list(d.values())
        if 5 in types:
            self.strength = 7
            return 'five of a kind'
        if 4 in types:
            self.strength = 6
            return 'four of a kind'
        if 3 in types and 2 in types:
            self.strength = 5
            return 'full house'
        if 3 in types:
            self.strength = 4
            return 'three of a kind'
        if types.count(2) == 2:
            self.strength = 3
            return 'two pair'
        if 2 in types:
            self.strength = 2
            return 'pair'
        if types.count(1) == 5:
            self.strength = 1
            return 'high card'

def hand_sort(hand):
    return (hand.strength, hand.ranks[0], hand.ranks[1], hand.ranks[2], hand.ranks[3], hand.ranks[4])

hands = []
for line in lines:
    cards, bid = line.split()
    hands.append(Hand(cards, bid))

sorted_hands = sorted(hands, key=hand_sort)

total = 0
for i,hand in enumerate(sorted_hands):
    n = i + 1
    total += (n * hand.bid)

print(total)
