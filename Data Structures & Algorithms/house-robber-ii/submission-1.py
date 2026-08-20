class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # helper using YOUR dp idea
        def rob_linear(arr):
            m = len(arr)
            dp = [0] * (m + 1)
            dp[0] = 0
            dp[1] = arr[0]

            for i in range(2, m + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])

            return dp[m]

        # Case 1: exclude last house
        case1 = rob_linear(nums[:-1])

        # Case 2: exclude first house
        case2 = rob_linear(nums[1:])

        return max(case1, case2)
