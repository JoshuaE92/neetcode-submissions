class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        bottom=0
        top=len(matrix)-1
        while(bottom<=top):
            row=(top+bottom)//2
            if(matrix[row][0]<=target and matrix[row][-1]>=target):
                break;
            else:
                if(matrix[row][0]>target):
                    top=row-1
                elif(matrix[row][-1]<target):
                    bottom=row+1
        if not(bottom<=top):
            return False
        row=(top+bottom)//2
        l=0
        r=len(matrix[row])
        while(l<=r):
            m=(l+r)//2
            if(matrix[row][m]==target):
                return True
            if(matrix[row][m]>target):
                r=m-1
            elif(matrix[row][m]<target):
                l=m+1
        return False
            
                

                

                
                