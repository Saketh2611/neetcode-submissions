class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        ans = []
        sets = []

        def backtrack(i):

            if sum(sets) == target:
                ans.append(sets[:])
                return

            if i == len(nums) or sum(sets) > target:
                return

            sets.append(nums[i])
            backtrack(i)
            sets.pop()

            backtrack(i + 1)

        backtrack(0)

        return ans