class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicti = {}
        for ch in s :
            if ch not in dicti :
                dicti[ch] = 1
            else :
                dicti[ch] += 1 
        
        for ch in t :
            if ch not in dicti :
                return False
                break
            else :
                if dicti[ch] == 0 :
                    return False
                    break
                else :
                    dicti[ch] -= 1

        for ch in dicti :
            if dicti[ch] != 0 :
                return False
                break 
                
        return True
