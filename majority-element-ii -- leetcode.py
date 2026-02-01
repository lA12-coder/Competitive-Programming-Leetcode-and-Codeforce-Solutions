from collections import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_count =  Counter(nums)
        return [x for x in num_count if num_count[x]>(len(nums)/3)]
    
Sol = Solution()
print(Sol.majorityElement([1,2]))
        
