class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0  # Handle empty string
        if n == 1: return 1  # Handle single char
        
        max_len = 0
        
        for i in range(n):
            visited = set()
            current_len = 0
            for j in range(i, n): # Start j from i to include the first char easily
                if s[j] in visited:
                    break # STOP immediately when duplicate found
                visited.add(s[j])
                current_len += 1
            
            if current_len > max_len:
                max_len = current_len
                
        return max_len