class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row=0
        rows=len(mat)
        col=0
        cols=len(mat[0])
        ret=[]

        up=True

      
        while(len(ret)!=(rows*cols)):

            if up==True:
                while(row>=0 and col<cols):
                    ret.append(mat[row][col])
                    row-=1
                    col+=1
                    

                
                if col==cols:
                    col-=1
                    row+=2
                else:
                    row+=1

                up=False
            else:
                while(col>=0 and row<rows):
                    ret.append(mat[row][col])
                    col-=1
                    row+=1

                
                if row==rows:
                    row-=1
                    col+=2
                else:
                    col+=1

                up=True
        return ret

                



            
          



        