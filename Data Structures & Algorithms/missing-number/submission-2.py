class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        count=0
        nums.sort()
        for i in range(len(nums)):
            if count!=nums[i]:
                return count
            
            count+=1
        return len(nums)


        