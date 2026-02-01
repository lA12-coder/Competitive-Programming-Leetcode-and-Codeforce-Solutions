from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        num_freq = sorted(num_freq, key=lambda x : num_freq[x])
        return [num_freq[i] for i in range(-1,-1-k,-1)]
        