class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left  = 0
        right  =  len(people)-1
        boat = 0

        # Iterate over the people list
        while left <  right:
            # check if there is the people's weight above the limit and
            #lower the right index by one to make the sum in less than or equals to the limit.
            if people[left]+people[right]>limit:
                boat+=1
                right -=1
            elif people[left]+people[right]<=limit:
                boat+=1
                left+=1
                right-=1
            
        else:
            if left==right:
                boat+=1
        return boat
