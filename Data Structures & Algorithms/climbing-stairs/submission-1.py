class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        ans = [1, 1]
        i = 2
        while i <= n:
            ans.append(ans[len(ans) - 1] + ans[len(ans) - 2])
            i += 1
        print(ans)
        return ans[len(ans) - 1]