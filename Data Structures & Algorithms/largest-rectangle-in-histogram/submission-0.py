class Solution:
    def largestRectangleArea(self, heights):
        stack = []   # stores indices
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            # Use 0 height as sentinel at end
            h = 0 if i == n else heights[i]

            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]

                # Width calculation
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
