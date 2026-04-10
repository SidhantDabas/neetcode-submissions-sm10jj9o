class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container = 0
        i, j = 0, len(heights) - 1
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            container = max(container, area)
            if heights[i] <= heights[j]:
                i= i + 1
            else: 
                j= j - 1
        return container
