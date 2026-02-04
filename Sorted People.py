from typing import List

# Using the built in sort method
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for name,_ in sorted(zip(names,heights), key=lambda x : -x[-1])]
    
    
# Using selection sort method
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Join each name to their respective height and store as a list of tuples.
        people = list(zip(names,heights))
        n = len(people)
        # Iterate over the unsorted list
        for i in range(n):
            min_index = i
            # find the minimum number from the unsorted list
            for j in range(i,n):
                if people[j][1] < people[min_index][1]:
                    min_index = j
            # Swap the minimum number with the current iteration value
            people[i],people[min_index] = people[min_index],people[i]
        
        return [people[i][0] for i in range(n-1,0-1,-1) if i>=0]
    

# Using Insertion sort method
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Join each name to their respective height and store as a list of tuples.
        people = list(zip(names,heights))
        n = len(people)
        
        # Iterate over the unsorted list
        for i in range(1,n):
            j = i
            
            # Compare the ith element with the sorted list and swap a position
            while j>0 and people[j][1] < people[j-1][1]:
                people[j],people[j-1] = people[j-1],people[j]
                j-=1
                
        # Return the names in the descending order 
        return [people[i][0] for i in range(n-1,-1,-1)]
        
        
        
print(Solution().sortPeople( names = ["Alice","Bob","Bob"], heights = [155,185,150])) #output: ['Bob', 'Alice', 'Bob']