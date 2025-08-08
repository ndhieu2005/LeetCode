from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        map_value = {'}':'{', ']':'[' , ')':'('}
        for c in s:
            if c in map_value:
                if stack and stack[-1] == map_value[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack


