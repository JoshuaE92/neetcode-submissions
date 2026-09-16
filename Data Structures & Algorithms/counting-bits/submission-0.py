class Solution:
    def countBits(self, n: int) -> List[int]:
        ret=[]

        for i in range(n+1):
            x=i
            count=0
            while(x!=0):
                count+=x%2
                x=x>>1
            ret.append(count)
        return ret
            

        
        