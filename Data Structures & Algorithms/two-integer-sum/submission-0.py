class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_set = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_set:
                return [my_set[diff],i]
            my_set[nums[i]] = i 