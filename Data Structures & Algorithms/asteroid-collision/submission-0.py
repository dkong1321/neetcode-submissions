class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        [2,4,-4,-1]
        2 and 4 going -> with -4 and -1 going <-
        lets make a queue contain the asteroids 
        if we add a negative and nothing there it should stay in the queue
        if there is a positive it will get popped it has to meet the next negative

        so if the asteroid is bigger it gets added back to the queue to meet the next asteroid
        """
        stack = []
        for asteroid in asteroids:
            # while we have something and the stack is positive and the ast is negative we 
            # have collision
            while stack and stack[-1] > 0 and asteroid <0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] > abs(asteroid):
                    asteroid = 0
                    break
                else:
                    stack.pop()
                    asteroid = 0
                    break
            if asteroid:
                stack.append(asteroid)
        return stack

            