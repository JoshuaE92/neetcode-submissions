class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        num_rows=len(mat)
        num_cols=len(mat[0])

        if(num_rows*num_cols!=r*c):
            return mat
        else:
            temp=[]
            new_mat=[[0 for _ in range(c)] for _ in range(r)]
         

            for i in range (num_rows):
                for j in  range(num_cols):
                    temp.append(mat[i][j])
     
                    
            k=0

            for ra in range(r):
                for ca in range(c):
                    new_mat[ra][ca]=temp[k]
                    k+=1
            
            return new_mat
                    





        
        