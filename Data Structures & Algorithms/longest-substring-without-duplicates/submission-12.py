class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()

        l = 0
        res = 0
        # pwwkew
        for r in range(len(s)):
            print(s[r], r, "r")
            while s[r] in char_set:
                # kew
                char_set.remove(s[l])
                l += 1
                print(char_set)
                print(s[l],  l, "l")
            char_set.add(s[r])
            # curr index of r - l where l is what we removed + 1
            res = max(res, r - l + 1)
            
        return res