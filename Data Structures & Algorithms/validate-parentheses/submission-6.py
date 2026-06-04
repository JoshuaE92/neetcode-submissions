class Solution:
    def isValid(self, s: str) -> bool:
        #create a stack
        #loop through the string
        #append values that are in "C[{"
        #Else pop value check if it is the coresponding
        #return false if they are not the saem
        #at the end return true if the stack is empty

        mystack=[]

        for c in s:
            
            if c in "([{":
                mystack.append(c)
            else:
                if(not(mystack)):
                    return False

                while(mystack):
                    val=mystack.pop()

                    if c==')' and val !='(':
                        return False
                    if c==']' and val !='[':
                        return False
                    if c=='}' and val !='{':
                        return False
                    else:
                        break
        if(not(mystack)):
            return True
        return False
                
                    
        