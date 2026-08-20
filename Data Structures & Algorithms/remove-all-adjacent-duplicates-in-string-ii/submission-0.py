class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #create a strack 

        #interate for the chars in the string
        #check if the top of teh stack is teh same value
        #if so increase the value of that 
        #if not add it to the stack init the value

        #when u are done wit everything iterate through the stack
        #iterate for each element adn value
        #add to ur stirng the eleent times value

        stack=[]

        for c in s:
            if stack and stack[-1][0]==c:
                stack[-1][1]+=1
            else:
                stack.append([c,1])

            if stack[-1][1]==k:
                stack.pop()
            
        ret=""
        for s, n in stack:
            ret+=s*n
        return ret

            



        
        
        

        
            



           

            




            
        




        