class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = strs[0]
        for i in range(1,len(strs)):
            curr = strs[i]
            j = 0
            while j < len(res) and j < len(curr) and res[j] == curr[j]:
                 j= j +1
            res = res[:j]
        return res
