class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force
        # res = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             res += 1
        # return res

        #  Seed the map with {0: 1} — represents the "empty prefix" before
        # we've seen any elements. This handles the case where a subarray
        # starting at index 0 sums exactly to k (currSum - k == 0).
        prefix = {0: 1}

        currSum = 0   # Running prefix sum as we iterate
        res = 0       # Count of valid subarrays found

        for num in nums:
            currSum += num # Extend the prefix sum to include this element

            # Core insight: a subarray nums[i..j] sums to k
            # iff prefixSum[j] - prefixSum[i-1] == k
            # ⟹ we need prefixSum[i-1] == currSum - k
            diff = currSum - k

            # If (currSum - k) exists in our map, those are valid left
            # endpoints — each occurrence is one valid subarray ending here
            res += prefix.get(diff, 0)

            # Record this prefix sum so future iterations can use it
            # as a left endpoint. +1 because the same sum can appear
            # multiple times (e.g. when zeros or negatives are present)
            prefix[currSum] = 1 + prefix.get(currSum, 0)

        return res
