from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        result = []
        diagonal = [[] for _ in range(row+col-1)]
    
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonal[i+j].append(mat[i][j])
        
        for i in range(row+col-1):
            if i%2 != 0:
                result.extend(diagonal[i])
            else:
                result.extend(reversed(diagonal[i]))
                
        return result

print(Solution().findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]])) #Output = [1,2,4,7,5,3,6,8,9]