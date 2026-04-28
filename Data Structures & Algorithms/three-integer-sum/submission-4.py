class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        brute force would be to iterate against this in 3 loops and return
        all values where the sum was 0. Lets assume this is bad and need to make 3 pointers
        we can't have any dupes so we might need to store these as a set
        """
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # nums[i] nums[l] nums[r]
            l = i + 1
            r = len(nums) -1
            # print(res)
            # print('l', l)
            while l<r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # don't need this since the other if statement will decrement r for me 
                    # while l < r and nums[r] == nums[r + 1]:
                    #     r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1

        return res