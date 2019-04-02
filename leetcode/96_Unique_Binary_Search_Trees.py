class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1 for i in range(n+1)]
        for i in range(2, n+1):
            s = 0
            for k in range(i):
                s += dp[k]*dp[i-1-k]
            dp[i] = s
        return dp[-1]
        