class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        count=0
        counts=Counter(nums)
        my_set=set(nums)

        for s in my_set:
            if s+k in counts and s+k!=s:
                count+=1
            else:
                if counts[s+k]>1:
                    count+=1
            
        return count
        
