class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [0] * n
        # pref = [0] * n
        # suff = [0] * n

        # pref[0] = suff[n-1] = 1 
        # for i in range(1,n):
        #     pref[i] = nums[i -1] * pref[i -1]
        # for i in range(n - 2, -1, -1):
        #     suff[i] = nums[i + 1] * suff[i + 1]
        # for i in range(n):
        #     res[i] = pref[i] * suff[i]
        # return res
        res = [ 1 ] * len(nums)
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        return res

