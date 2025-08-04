class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        max_length = 0
        left_pointer = 0
        for right_pointer,char in enumerate(s):
            while char in subset:
                subset.remove(s[left_pointer])
                left_pointer += 1
            subset.add(char)
            max_length = max(max_length, right_pointer - left_pointer + 1)
        return max_length





