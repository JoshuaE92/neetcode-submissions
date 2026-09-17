class Solution:
    def isHappy(self, n: int) -> bool:
        #make a set to hold any numbers wee seen
        #while(n!=1):
            #do teh computation, probally turn the num into a str
            #then loop though all the digits n add it up,

            #if the computed number is in seen ret false

        
        #ret true

        seen=set()

        while(n!=1):
            digits = [int(d) for d in str(abs(n))]
            comp=0

            for i in range(len(digits)):
                comp+=digits[i]*digits[i]

            if(comp in seen):
                return False
            
            seen.add(comp)

            n=comp
        return True

        