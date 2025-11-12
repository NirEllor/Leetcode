from collections import Counter
from typing import List



class Solution:
    def majorityElementCostly(self, nums: List[int]) -> int:
        hash_map = Counter(nums)
        return max(hash_map, key=hash_map.get)

    def majorityElement(self, nums: List[int]) -> int:
        # Booyer Moore Algorithm
        cnt = 0
        element = None
        for num in nums:
            if cnt == 0:
                element = num
            cnt += (1 if num == element else -1)
        return element



s = Solution()
print(s.majorityElement([6,5,5]))
