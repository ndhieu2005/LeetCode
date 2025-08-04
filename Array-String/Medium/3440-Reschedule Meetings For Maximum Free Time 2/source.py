class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        previous = 0
        for i in range(n):
            gaps.append(startTime[i] - previous)
            previous = endTime[i]
        gaps.append(eventTime - previous)
        ans = 0
        #Case 1: block is getting shifted
        for i in range(len(gaps)-1):
            ans = max(ans,gaps[i]+gaps[i+1])
        #Case 2: block is getting moved to another relative order
        sgaps = gaps[:]
        sgaps.sort(reverse = True)
        top1 = sgaps[0]
        top2 = sgaps[1]
        top3 = sgaps[2]
        for i in range(n):
            leftgap = gaps[i]
            rightgap = gaps[i+1]
            mx = max(leftgap,rightgap)
            mn = min(leftgap,rightgap)
            event = endTime[i] - startTime[i]
            select1,select2 = 0,0
            if mx != top1:
                select1 = 1
            elif mn != top2:
                select2 = 1
            if select1:
                if top1>= event:
                    ans = max(ans,leftgap + rightgap + event)
            elif select2:
                if top2 >= event:
                    ans = max(ans,leftgap + rightgap + event)
            else:
                if top3 >= event:
                    ans = max(ans,leftgap + rightgap + event)
        return ans
            


