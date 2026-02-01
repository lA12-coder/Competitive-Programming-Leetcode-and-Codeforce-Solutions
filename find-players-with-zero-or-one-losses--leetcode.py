from typing import List, Dict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict_Lost:Dict[int,int] = {}
        lost0 = set()
        for i in range(len(matches)):
            if matches[i][0] not in dict_Lost:
                lost0.add(matches[i][0])
            if matches[i][1] in lost0:
                lost0.discard(matches[i][1])
            if matches[i][1] not in dict_Lost:
                dict_Lost[matches[i][1]] = 1
            else:
                dict_Lost[matches[i][1]] += 1

        return [sorted(list(lost0)), sorted([x for x in dict_Lost if dict_Lost[x] == 1])]



        