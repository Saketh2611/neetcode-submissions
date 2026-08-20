class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
      
        nums_1 = [-1*nums[i] for i in range(len(nums))]
        heapq.heapify(nums_1)
        while k > 1 :
            heapq.heappop(nums_1)
            k -= 1 
        return -1*(min(nums_1))

        