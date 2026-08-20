from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + '#' + s)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            # Read full length (can be multi-digit)
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            i = j + 1  # move past '#'

            ans.append(s[i:i + length])
            i += length  # move past the string

        return ans
