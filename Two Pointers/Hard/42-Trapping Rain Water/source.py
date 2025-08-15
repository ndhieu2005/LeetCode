class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        l,r = 0,n-1
        leftMax = height[l]
        rightMax = height[r]
        while l < r:
            if leftMax < rightMax:
                l = l + 1
                leftMax = max(leftMax,height[l])
                ans += leftMax - height[l]
            else:
                r = r - 1
                rightMax = max(rightMax,height[r])
                ans += rightMax - height[r]
        return ans        