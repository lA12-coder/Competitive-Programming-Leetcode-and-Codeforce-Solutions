from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count =  Counter(nums)
        maj_elements = [x for x in num_count if num_count[x]>(len(nums)/2)]
        return max(maj_elements)