from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myHash=defaultdict(list)
        retList=[]
        for i in range(len(strs)):
            opString=strs[i]
            sortChar=sorted(list(opString))
            sortStr="".join(sortChar)
            if(sortStr in myHash):
                myHash[sortStr].append(opString)
            else:
                myHash[sortStr].append(opString)

        
        for keys in myHash:
            retList.append(myHash[keys])
        return retList


            


        