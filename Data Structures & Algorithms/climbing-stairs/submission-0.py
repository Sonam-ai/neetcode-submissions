class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:return n
        prev=curr=1
        counter=1
        while counter<n:
            next=prev+curr
            counter+=1
            prev=curr
            curr=next

        return curr
        