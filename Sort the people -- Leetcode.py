from typing import List

# Solved using bubble sort
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]):
        pair = list(zip(heights,names))
        for i in range(len(pair)):
            for j in range(len(pair)-i-1):
                if pair[j] > pair[j+1]:
                    pair[j], pair[j+1] = pair[j+1], pair[j]
                    
        sorted_names = [x[1] for x in list(reversed(pair))]
        return sorted_names

# Solved using simple sort function
class solution2:
    def sortPeople(self, names: List[str], heights: List[int]):
        pair = list(zip(heights, names))
        pair.sort(reverse=True)
        names = [names for heights, names in pair]
        return 

# solved using insertion sort
class solution3:
    def sortPeople(self, names: List[str], heights: List[int]):
        pair = list(zip(heights, names))
        for i in range(len(pair)):
            for j in range(i+1, len(pair)):
                if pair[i][0] > pair[j][0]:
                    pair[i], pair[j] = pair[j], pair[i]

        sorted_names = [x[1] for x in list(reversed(pair))]
        
        return sorted_names
                    
        
                    
                    
        
        
        
sol = solution3()
res = sol.sortPeople(["Mary","John","Emma"],[180,165,170])
print(res) 



