"""
You are given an integer array ranks and a character array suits. You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].

The following are the types of poker hands you can make from best to worst:
    - "Flush": Five cards of the same suit.
    - "Three of a Kind": Three cards of the same rank.
    - "Pair": Two cards of the same rank.
    - "High Card": Any single card.

Return a string representing the best type of poker hand you can make with the given cards.

Note that the return values are case-sensitive.
"""

from collections import defaultdict

class Solution(object):
    def bestHand(self, ranks, suits):
        cards = defaultdict(lambda: 0)
        suit_count = defaultdict(lambda: 0)
        for i in range(5):
            cards[ranks[i]] += 1
            suit_count[suits[i]] += 1
        sorted(suit_count.items(), key=suit_count.get, reverse=True)
        sorted(cards.items(), key=cards.get, reverse=True)
        for i in suit_count:
            if suit_count[i] == 5:
                return "Flush"
        pair = False
        for i in cards:
            if cards[i] >= 3:
                return "Three of a Kind"
            if cards[i] == 2:
                pair = True
        if pair:
            return "Pair"
        return "High Card"