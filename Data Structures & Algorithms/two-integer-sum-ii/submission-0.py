class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        n = len(numbers)
        right = n-1
        while left < right :
            if numbers[left] + numbers[right] == target :
                return [left+1 , right+1]
            elif  numbers[left] + numbers[right] > target : 
                right -= 1 
            else : 
                left += 1 
        
            
        