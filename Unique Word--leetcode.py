from typing import List
class Solution:
    def uniqueWords(self, Strs:List) -> int:
        dict = {}
        count = 0
        for x in Strs:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] +=1
        for value in dict.values():
            if value == 1:
                count += 1
        return count

Sol = Solution()
print(Sol.uniqueWords(["hello","hello", "world"]))
