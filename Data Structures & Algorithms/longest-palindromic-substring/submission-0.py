class Solution:
    def longestPalindrome(self, s: str) -> str:
        #make variables
        #loop once for odd
        #loop again for even
        #return res

        res=""
        resLen=0

        for i in range(len(s)):
            r,l=i,i

            while(r<len(s) and l>=0 and s[r]==s[l]):
                if(r-l+1>resLen):
                    resLen=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1

            
            r=i+1
            l=i
            while(r<len(s) and l>=0 and s[r]==s[l]):
                if(r-l+1>resLen):
                    resLen=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
        return res


        