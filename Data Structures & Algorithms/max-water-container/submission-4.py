class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_area = 0
        while left < right:
            lowest_side = min(heights[left],heights[right])
            max_area = max(max_area, (right-left)*lowest_side)
            # print(max_area)
            # print(lowest_side)
            # print(left,right)
            # print(heights[left],heights[right])
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_area