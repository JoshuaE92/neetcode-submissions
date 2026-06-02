class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums=set(nums)
        maxval=0

        for num in setnums:
            if(not((num-1) in setnums)):
                count=1
                curval=num+1
                while(curval in setnums):
                    curval+=1
                    count+=1
                maxval=max(count,maxval)
        return maxval
        
                
            



        