class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=""
        for s in strs:
            length=len(s)
            encode+=str(length)+'#'+s
        return encode


    def decode(self, s: str) -> List[str]:
        i=0
        str_integer=""
        int_int=0
        array=[]
        
        while(i<len(s)):
            if s[i]=='#':
                int_int=int(str_integer)
                array.append(s[i+1:i+int_int+1])
                i=i+int_int+1
                str_integer=""
                int_int=0
                
            else:
                str_integer+=s[i]
                i+=1



        return array


