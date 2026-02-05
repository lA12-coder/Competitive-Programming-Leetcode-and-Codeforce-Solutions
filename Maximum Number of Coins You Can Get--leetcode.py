from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)//3
        max_count = 0

        for i in range(n):
            max_count += piles.pop(-2)
            piles.pop(0)
            piles.pop(-1)
                
        return max_count
    
print(Solution().maxCoins(piles = [9,8,7,6,5,1,2,3,4]))
            