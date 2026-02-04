from typing import List
from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count = Counter(arr1)
        result = []
        
        for num in arr2:
            result.extend([num]*arr1_count.pop(num))
                
        remaining = sorted(arr1_count.keys())
        for num in remaining:
            result.extend([num]*arr1_count[num])
        
        return result
        
print(Solution().relativeSortArray([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31], [2,42,38,0,43,21]))
        