from bisect import bisect_right
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        #Setup cho bài toán
        tiles.sort()
        n = len(tiles)
        starts = [s for s, e in tiles]
        ends = [ e for s,e in tiles]
        lens = [e -s + 1 for s,e in tiles]
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i+1] = dp[i] + lens[i] 
        
        #Thuật giải chính
        ans = 0
        for l in range(n):
            e = starts[l] + carpetLen - 1 
            r = bisect_right(ends,e)
            full = dp[r] - dp[l]
            partial = 0
            if r < n and starts[r] <= e:
                partial = e - starts[r] + 1
            cover = full + partial 
            ans = max(ans,cover)
            if ans >= carpetLen:
                return carpetLen
        return ans

        

        

        