class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = float('inf')
        for s in strs :
            if len(s) < mini :
                mini = len(s)
        print(mini)
        i = 0 
        ans = ""
        while i < mini :
            letter = strs[0][i]
            for j in range(1,len(strs)) :
                if strs[j][i] != letter :
                    return ans
                    break 
            ans += letter
            i += 1
        return ans
                
