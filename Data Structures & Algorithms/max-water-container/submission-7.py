class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        brute force is to just calculate all the areas and return the max
        the lowest height is the limiting factor if left is lower that right we should move it if 
        right is lower we should move it 
        """
        l = 0
        r = len(heights)-1
        # [1,7,2,5,4,7,3,6]
        max_area = min(heights[l],heights[r]) * (r-l) # 1 * 8
        while l < r:
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
            curr_area = min(heights[l],heights[r]) * (r-l)
            max_area = max(max_area, curr_area)
            print(l, "left")
            print(r, "right")
            print(curr_area, max_area)
        return max_area
