class Solution:
    def trap(self, height: List[int]) -> int:
        """
        we could find the holes by starting l and r at 0
        iterate r until it finds a location where water can be trapped
        we know water can be trapped if there is a difference of (r - l) * min(height[l], height[r])
        """
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        water = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax= max(leftMax, height[l])
                water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water += rightMax - height[r]
        return water
        