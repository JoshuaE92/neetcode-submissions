class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxval=-1*(float('inf'))
        sums=0

        for i in range(len(nums)):
            if sums<0:
                sums=0
            sums+=nums[i]
            maxval=max(maxval,sums)
        return maxval

         


        