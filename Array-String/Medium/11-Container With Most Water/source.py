class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height) - 1
        res = min(height[i],height[j]) * (j-i)
        while i != j and i < len(height) and j > 0:
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
            tmp = min(height[i],height[j]) * (j-i)
            if tmp > res:
                res = tmp
        return res
        