class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #Create identifiers for top bottom left and right
        
        #while(top>bottom, right>left )
        #read from left->right
        #move the top down
        #read from top to bottm
        #move the right
        #read from right to left
        #move the bottom
        #read from bottom to top
        #move the left


        top,left=0,0
        right=len(matrix[0])
        bottom=len(matrix)
        res=[]

        while(top<bottom and right>left):
            
            
            for t in range(left,right):
                res.append(matrix[top][t])
                
            
            top+=1

            #how to loop here, need to get last col


            if (not (top<bottom and right>left)):
                
                return res

            for n in range(top,bottom):
                res.append(matrix[n][right-1])

            right-=1
        
            if (not (top<bottom and right>left)):
                return res

            
            for r in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][r])
            bottom-=1

            if (not (top<bottom and right>left)):
                return res

            
            for l in range(bottom-1,top-1,-1):
                res.append(matrix[l][left])
            left+=1

            if (not (top<bottom and right>left)):
                    return res
            
            
        return res


            

        