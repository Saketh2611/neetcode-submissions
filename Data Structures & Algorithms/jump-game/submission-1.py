class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 0
        n = len(nums)

        for i in range(n):
            if i > maxreach:
                return False
            
            maxreach = max(maxreach, i + nums[i])

        return True
