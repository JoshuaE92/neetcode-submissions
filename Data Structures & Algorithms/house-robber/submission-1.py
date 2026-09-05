class Solution:
    def rob(self, nums: List[int]) -> int:
        #iterate and calculate the 

        r1=0
        r2=0

        for n in nums:
            temp=max(n+r1,r2)
            r1=r2
            r2=temp
        return r2
        

        