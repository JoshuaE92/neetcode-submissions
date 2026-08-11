class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #set all of your elements

        #for 1-len:
            #topleft=saved, 
            
            #topleft=bottomleft

            #bottomleft=bottom right

            #bottomright=top right

            #topright=topleft variable



        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix)-1
    
        while(left<right and top<bottom):
            for  i in range (right-left):
                topleft=matrix[top][left+i]

                matrix[top][left+i]=matrix[bottom-i][left]

                matrix[bottom-i][left]=matrix[bottom][right-i]

                matrix[bottom][right-i]=matrix[top+i][right]

                matrix[top+i][right]=topleft

            left+=1
            right-=1
            top+=1
            bottom-=1

        
        return 








        