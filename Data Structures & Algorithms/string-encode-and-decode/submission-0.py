class Solution:

    def encode(self, strs: List[str]) -> str:
        return_string = ''
        for word in strs:
            return_string += str(len(word)) + "#" + word
        return return_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1 + length])
            i = j + 1 + length
        return res