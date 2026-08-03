class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf=0
        
        for i in range(len(prices)):
            l=i
            r=i+1

            while(r<len(prices)):
                curProf=prices[r]-prices[l]
                maxProf=max(maxProf,curProf)
                r+=1
            
        return maxProf
        