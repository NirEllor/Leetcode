from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_index = {}
        for idx, num in enumerate(nums):
            if target - num in nums_to_index:
                return [nums_to_index[target - num], idx]
            else:
                nums_to_index[num] = idx

s = Solution()
print(s.twoSum([2,7,11,15], 9))