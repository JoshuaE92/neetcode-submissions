class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
        
    def helper(self,nums):
            num1=0
            num2=0
            

            for n in nums:
                
                    temp=max(num1+n,num2)
                    num1=num2
                    num2=temp
                
            return num2
            