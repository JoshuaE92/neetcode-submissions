class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret=[]
        sub=[]
        total=0

        def sum(target,total,i,sub):
          
            if total==target:
                    yo=sub.copy()
                   
                    ret.append(yo)
                    return
                
            if total>target or i>=len(nums):
                    return
               
            
            sub.append(nums[i])
            total+=nums[i]
            sum(target,total,i,sub)
            sub.pop()
            total-=nums[i]
            sum(target,total,i+1,sub)
            
        sum(target,total,0,sub)
        return ret
                
            

                
        