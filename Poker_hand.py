from collections import Counter, OrderedDict


class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.values = [x.value for x in self.cards]
        self.suits = [x.suit for x in self.cards]
        self.true_values = sorted([x.true_value for x in self.cards])
        self.counter = Counter(self.values)
        self.value_amounts = self.counter.values()

    def pair(self):
        return max(self.value_amounts) == 2

    def two_pairs(self):
        return list(self.value_amounts).count(2) == 2

    def three_of_a_kind(self):
        return max(self.value_amounts) == 3

    def straight(self):
        first_value = self.true_values[0]
        return self.true_values == list(range(first_value, first_value + 5))

    def flush(self):
        return len(set(self.suits)) == 1

    def full_house(self):
        return 3 in self.value_amounts and 2 in self.value_amounts

    def four_of_a_kind(self):
        return max(self.value_amounts) == 4

    def straight_flush(self):
        return self.straight() and len(set(self.suits)) == 1

    def royal_flush(self):
        return self.true_values == list(range(10, 15)) and len(set(self.suits)) == 1

    def __str__(self):
        hand = OrderedDict()
        hand['Royal Flush'] = self.royal_flush()
        hand['Straight Flush'] = self.straight_flush()
        hand['Four of a Kind'] = self.four_of_a_kind()
        hand['Full House'] = self.full_house()
        hand['Flush'] = self.flush()
        hand['Straight'] = self.straight()
        hand['Three of a Kind'] = self.three_of_a_kind()
        hand['Two Pairs'] = self.two_pairs()
        hand['Pair'] = self.pair()

        for k, fn in hand.items():
            if fn:
                return k
        return 'High Card'


class Card:
    def __init__(self, c):
        self.value = c[:-1]
        self.suit = c[-1]
        self.get_true_value()

    def get_true_value(self):
        elders = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self.true_value = 0
        try:
            self.true_value = int(self.value)
        except ValueError:
            self.true_value = elders[self.value]


inp = input().split()
cards = []

for c in inp:
    card = Card(c)
    cards.append(card)

hand = Hand(cards)
print(hand)
