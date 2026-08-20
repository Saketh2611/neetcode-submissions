class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        max_freq = 0
        max_len = 0

        for r in range(len(s)):

            # If character already exists, increment
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            # Update max frequency
            if count[s[r]] > max_freq:
                max_freq = count[s[r]]

            # Shrink window if replacements exceed k
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            # Update answer
            if (r - l + 1) > max_len:
                max_len = r - l + 1

        return max_len
