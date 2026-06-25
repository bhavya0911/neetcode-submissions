class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        ans = [1, 1]
        i = 2
        while i <= n:
            ans.append(ans[i - 1] + ans[i - 2])
            i += 1
        print(ans)
        return ans[i - 1]