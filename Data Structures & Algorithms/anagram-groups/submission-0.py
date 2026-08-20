from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold groups. 
        # Key: The sorted tuple of characters (e.g., ('a', 'e', 't'))
        # Value: List of words belonging to that group (e.g., ["eat", "tea", "ate"])
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 1. Sort the string to create a standard key for comparison
            # "eat" -> ['a', 'e', 't']. We use tuple() because lists can't be dictionary keys.
            sorted_key = tuple(sorted(s))
            
            # 2. Append the original string to the correct list in the map
            anagram_map[sorted_key].append(s)
        
        # 3. Return just the lists of grouped anagrams
        return list(anagram_map.values())