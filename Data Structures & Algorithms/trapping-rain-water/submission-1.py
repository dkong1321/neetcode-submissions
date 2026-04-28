class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) space O(n) time
        n = len(height)
        if n == 0:
            return 0

        # initialize empty array of length n
        leftMax = [0] * n
        rightMax = [0] * n
        # set left max to the first value on the left
        leftMax[0] = height[0]
        
        # Iterate through the array left to right to 
        # find the max left boundary
        for i in range(1,n):
            leftMax[i] = max(leftMax[i -1], height[i])
        # set the right max to the first value from the right
        rightMax[n-1] = height[n-1]
        # Iterate through the array right to left
        # fins the max right boundary 
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        res = 0
        for i in range(n):
            # Add all the 
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res
