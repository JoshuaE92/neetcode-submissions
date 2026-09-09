class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #base case is if we hit m,n for row in col
        #if we hit the base case:
            #check if the path is in the path set if not
            #add the path to the path set
        
        #take every choice of move possible, up down left right, make sure to add to our cur path list of tup


        #init the bottomrow with ones

        #loop through all rows

            #loop throught the col backwars skping da right most

                #set the row r to the row r+1 +bottom r

            #bottomrow=newrow

        #return new row[0]

        botrow=[1]*n

        for i in range(m-1):
            newrow=[1]*n

            for j in range(n-2,-1,-1):
                newrow[j]=newrow[j+1]+botrow[j]
            
            botrow=newrow
        
        return botrow[0]
                    
        
       
        



                
            
