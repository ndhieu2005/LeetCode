class Solution:
    def romanToInt(self, s: str) -> int:
        map_value = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500,"M": 1000}
        res = 0
        for i in range(len(s)-1,-1,-1):
            if i + 1 < len(s) and map_value[s[i]] < map_value[s[i+1]]:
                res = res - map_value[s[i]]
            else:
                res = res + map_value[s[i]]
        return res


        