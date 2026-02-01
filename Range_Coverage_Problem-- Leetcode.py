from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
       target = set(range(left,right+1))
       covered = set()
       for a, b in ranges:
           covered.update(range(a,b+1))
       return target.issubset(covered)

