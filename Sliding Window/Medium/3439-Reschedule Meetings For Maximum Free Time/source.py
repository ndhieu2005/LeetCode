class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = eventTime
        A = startTime
        B = endTime
        count = len(A)
        F = [] #Free time array
        for i in range(count+1):
            if i == 0:
                F.append(A[i])
            elif i == count:
                F.append(n - B[i-1])
            else:
                F.append(A[i] - B[i-1])
        window_sum = sum(F[:k+1])
        maxSum = window_sum
        for i in range(count-k):
            window_sum = window_sum - F[i] + F [i+k+1]
            maxSum = max(window_sum,maxSum)
        return maxSum







        