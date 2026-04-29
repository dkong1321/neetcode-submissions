class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        visited = set()
        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord, 1)])
        while queue:
            word, steps = queue.popleft()
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    neighbor = word[:i] + char + word[i+1:]
                    if neighbor in wordSet and neighbor not in visited:
                        if neighbor == endWord:
                            return steps + 1
                        visited.add(neighbor)
                        queue.append((neighbor, steps+1))
        return 0