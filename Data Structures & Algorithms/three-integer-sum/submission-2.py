class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret=[]

        for i in range(len(nums)):
            target=0-(nums[i])
            l=i+1
            r=len(nums)-1
            if(i>0 and nums[i]==nums[i-1]):
                continue
            
            while(l<r):
                if(nums[l]+nums[r]>target):
                    r-=1
                elif(nums[l]+nums[r]<target):
                    l+=1
                elif(nums[l]+nums[r]==target):
                    now=[]
                    now.append(nums[i])
                    now.append(nums[l])
                    now.append(nums[r])
                    ret.append(now)
                    l+=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
                    

        return ret



    
        