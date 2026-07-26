class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        res = 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        prefix[0] = height[0]
        suffix[-1] = height[-1]
        for i in range(1, len(height)):
            prefix[i] = max(height[i], prefix[i - 1])
        
        for i in range(len(height) - 2, 0, -1):
            suffix[i] = max(suffix[i + 1], height[i])
        
        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            res += max(water, 0)
        return res