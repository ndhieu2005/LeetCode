class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        right_pointer,left_pointer = 1,0
        ans = nums[left_pointer]
        while right_pointer < len(nums):
            for i in range(left_pointer,right_pointer):
                if nums[i] == nums[right_pointer]:
                    left_pointer = i + 1
                    break
            tmp = sum(nums[left_pointer:right_pointer + 1])
            if tmp > ans:
                ans = tmp
            right_pointer = right_pointer + 1
        return ans

                
