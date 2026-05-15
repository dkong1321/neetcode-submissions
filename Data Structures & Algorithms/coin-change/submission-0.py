class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create all the amounts as with a default val
        dp = [amount+1] * (amount + 1)
        # We know that to get amount 0 we can return 0 coins
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >=0:
                    # we want to check if the dp[a] (coin count)
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1