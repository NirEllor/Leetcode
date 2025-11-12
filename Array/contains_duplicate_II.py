from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for idx, num in enumerate(nums):
            if num in hash_map and abs(hash_map[num] - idx) <= k:
                return True
            else:
                hash_map[num] = idx
        return False


s = Solution()
s.containsNearbyDuplicate([1,2,3,1,2,3], k = 2)