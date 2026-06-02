class Solution:
    def isValid(self, s: str) -> bool:
        #for the len of characters, if u come across inside bracket appejnd
        #if u come across closing backed pop, check if same
        #if not same return false
        #at the end if its not empty return false
        #return true

        stack=[]
        for c in s:
            if(c=='(' or c=='{' or c=='['):
                stack.append(c)
            else:
                
                empty=not bool(stack)
                if(not empty):
                    pop=stack.pop()
                    if c==')' and pop!='(':
                        return False
                    if c==']' and pop!='[':
                        return False
                    if c=='}' and pop!='{':
                        return False
                else:
                    return False
        isempty=not bool(stack) 
        if(not isempty):
            return False
        return True;      
        