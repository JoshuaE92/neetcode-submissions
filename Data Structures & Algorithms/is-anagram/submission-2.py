class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myHash={}

        len1=len(s)
        len2=len(t)

        if(len1!=len2):
            return False
        

        for i in range(len1):
            if(s[i] in myHash):
                myHash[s[i]]+=1
            else:
                myHash[s[i]]=1


        for i in range(len1):
            if (t[i] in myHash):
                if(myHash[t[i]]==0):
                    return False
                else:
                    myHash[t[i]]-=1
                 
                
            else:
                return False
            
        return True

        