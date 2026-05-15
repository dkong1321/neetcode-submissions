class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0
        for word in words:
            count_word = Counter(word)
            good = True
            for c in count_word:
                if count_word[c] > count[c]:
                    good =False 
                    break
            if good:
                res += len(word)
        return res