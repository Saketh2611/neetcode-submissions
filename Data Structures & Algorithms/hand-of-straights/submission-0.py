from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        
        # If total cards not divisible by groupSize
        if n % groupSize != 0:
            return False
        
        hand.sort()
        freq = Counter(hand)
        
        for card in hand:
            if freq[card] > 0:
                # Try to form a group starting from card
                for next_card in range(card, card + groupSize):
                    if freq[next_card] == 0:
                        return False
                    freq[next_card] -= 1
        
        return True
