class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myHash={}
        for i in range(len(nums)):
            if(nums[i] in myHash):
                return True
            else:
                myHash[nums[i]]=1
            
        return False
        