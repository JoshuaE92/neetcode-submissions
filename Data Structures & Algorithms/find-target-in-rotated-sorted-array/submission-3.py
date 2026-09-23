class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while(l<=r):
            m=(l+r)//2

            if nums[m]==target:
                return m

            #inside the left peice
            if nums[m]>=nums[l]:
                #ask what breaks the condition

                if target<nums[l] or target>nums[m]:
                    l=m+1
                else:
                    r=m-1
                
            else:
                if target>nums[r] or target<nums[m]:
                    r=m-1
                else:
                    l=m+1
        return -1
                


        