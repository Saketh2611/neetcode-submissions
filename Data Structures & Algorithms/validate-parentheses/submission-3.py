class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = { '(' : ')' , '{' : '}' , '[' : ']' }
        close = 0
        for ch in s :
            if ch in maps.values():
                if len(stack) > 0 and maps[stack[-1]] == ch :
                    stack.pop()
                else :
                    close += 1
            else :
                stack.append(ch)
        if len(stack) == 0 and close == 0:
            return True 
        else :
            return False
        