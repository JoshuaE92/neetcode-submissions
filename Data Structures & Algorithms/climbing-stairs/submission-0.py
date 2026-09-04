class Solution:
    def climbStairs(self, n: int) -> int:
        #base case of if computed value is the same as n
        #using the arra index as steps, iterate at steps, for each step u have 2 choices
        #use the array to store the values so when we make the second choice we dont have to recalculate our value

        
            
        one=1
        two=1
        for i in range(n-1):
                temp=one
                one=one+two
                two=temp
            
        return one
          
            
