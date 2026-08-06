class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myhash=set()
        ret=0
        l=0

        for r in range(len(s)):
            while(s[r] in myhash):
                myhash.remove(s[l])
                l+=1
            
            myhash.add(s[r])
            ret=max(ret,r-l+1)
        return ret