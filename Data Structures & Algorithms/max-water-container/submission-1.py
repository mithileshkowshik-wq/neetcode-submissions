class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        maxarea = 0

        while left < right:
            if (min(heights[left], heights[right])*(right - left) > maxarea):
                maxarea = min(heights[left], heights[right])*(right - left)
            if (heights[left] > heights[right]):
                right = right - 1
            elif (heights[left] < heights[right]):
                left = left + 1
            else:
                left = left + 1
                right = right - 1
        return maxarea

        