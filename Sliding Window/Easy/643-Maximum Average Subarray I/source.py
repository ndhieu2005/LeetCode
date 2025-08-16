class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumK = 0
        n = len(nums)
        for i in range(k):
            sumK = sumK + nums[i]
        ans = sumK/k
        for j in range(k,n):
            sumK = sumK - nums[j-k] + nums[j]
            ans = max(ans,sumK/k)
        return ans
            