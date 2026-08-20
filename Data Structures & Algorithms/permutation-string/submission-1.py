class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)                # sort once
        k = len(s1)

        if k > len(s2):
            return False

        for i in range(len(s2) - k + 1):
            sub = sorted(s2[i:i+k])    # sort window
            if s1 == sub:
                return True

        return False
