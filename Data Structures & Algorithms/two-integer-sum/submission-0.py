class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myhash={}
        retlist=[]
        for i in range(len(nums)):
            if target-(nums[i]) in myhash:
                retlist.append(myhash[target-(nums[i])])
                retlist.append(i)
                return retlist
            else:
                myhash[nums[i]]=i
            


        
        