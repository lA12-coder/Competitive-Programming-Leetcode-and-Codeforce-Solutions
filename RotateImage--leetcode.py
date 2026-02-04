from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]):
        """
          Do not return anything, modify matrix in-place instead.
        """
        matrix  = list(map(list,zip(*matrix)))
        for i in range(len(matrix)):
            matrix[i] = list(reversed(matrix[i]))         
        return matrix
    
print(Solution().rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))