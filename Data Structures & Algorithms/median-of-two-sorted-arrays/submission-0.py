class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Always binary search on the smaller array to satisfy O(log(min(n, m)))
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
            
        n, m = len(A), len(B)
        total = n + m
        # Calculate the "halfway" point (integer division)
        # For odd total, 'half' includes the median itself.
        half = (total + 1) // 2 
        
        # Binary Search on A
        l, r = 0, n
        while l <= r:
            i = (l + r) // 2       # Cut position in A
            j = half - i           # Cut position in B
            
            # Handle edge cases (infinity helps simplify logic)
            # If cut is at 0, Left is -infinity. If at end, Right is +infinity.
            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < n else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < m else float("inf")
            
            # Check if partition is valid
            if A_left <= B_right and B_left <= A_right:
                # Correct partition found!
                
                # If total items are odd, median is the max of the left side
                if total % 2:
                    return max(A_left, B_left)
                
                # If total items are even, average the middle two
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            elif A_left > B_right:
                # A's left element is too big; we need to reduce A's contribution
                r = i - 1
            else:
                # B's left element is too big; we need to increase A's contribution
                l = i + 1