from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict=defaultdict(list)

        for string in strs:
            alpha=[0]*26
        
            for char in string:
                alpha[ord(char)-ord('a')]+=1
            mydict[tuple(alpha)].append(string)
        return(list(mydict.values()))
       
        



            


        