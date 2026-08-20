from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequencies
        freq = Counter(nums)
        
        # Step 2: Create buckets (index = frequency)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, count in freq.items():
            buckets[count].append(num)
        
        # Step 3: Collect top k frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
