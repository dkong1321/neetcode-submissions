class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in word_dict:
                word_dict[key] = [word]
            else:
                word_dict[key].append(word)
        
        return list(word_dict.values())