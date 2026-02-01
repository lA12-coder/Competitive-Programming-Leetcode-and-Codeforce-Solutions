class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circularList = [num for num in range(1,n+1)]
        initial_index = 0
        while len(circularList) != 1:
                n = len(circularList)
                index = (initial_index+k-1) % n
                circularList.pop(index)
                initial_index = index
        return circularList[0]

                
                
            
            
        
        
        
        
