import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    heap = []
    for value, count in counter.items():
        heapq.heappush(heap, (count, value))
        if len(heap) > k:
            heapq.heappop(heap)

    return [value for count, value in heap]



