class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        def backtrack(i):
            if i == len(nums) :
                ans.append(path[:])
                return 

            path.append(nums[i]) #enter the current number 
            backtrack(i+1) #explore the next one  
            path.pop()    # after exploring try new (next) path by removing the old
            backtrack(i+1)  
        backtrack(0)
        return ans
        