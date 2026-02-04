from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list,zip(*matrix)))
            
print(Solution().transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]])) # Output: [[1,4,7],[2,5,8],[3,6,9]]