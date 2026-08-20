class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*(n)
        for i in range(n):
            for j in range(i+1,n):
                if nums[j] > nums[i] :
                    dp[j] = max(dp[j],1+dp[i])
        return max(dp)


        