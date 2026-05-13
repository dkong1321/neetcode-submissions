class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue
            
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] > abs(asteroid):
                    asteroid = 0
                    break
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                else:
                    stack.pop()
                    asteroid = 0
                    continue
            if asteroid:
                stack.append(asteroid)
        return stack