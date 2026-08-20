import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. Negate values to simulate Max-Heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            # 2. Use heapq module syntax
            # x is the heaviest (most negative, e.g., -8)
            x = heapq.heappop(stones) 
            # y is the second heaviest (e.g., -7)
            y = heapq.heappop(stones) 
            
            # 3. Only push if they are not equal
            if x != y:
                # Math: -8 - (-7) = -1. Correctly gives the negative remaining weight.
                # Must use heappush to keep the list sorted as a heap
                heapq.heappush(stones, x - y)
        
        # 4. Return the result as a positive integer
        # If stones is empty (all destroyed), return 0
        return -stones[0] if stones else 0