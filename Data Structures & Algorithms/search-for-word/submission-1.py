class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #if we create the word, return

        #if the len of cur is greater then the string

        #make the choice to take the current index

        #make the choice to skip the cu

        row=len(board)
        col=len(board[0])
        path=set()


        def find(r,c,i):

            if i==len(word):
                return True

            if r<0 or c<0 or r>=row or c>=col or board[r][c]!=word[i] or (r,c) in path:
                return False

            
            path.add((r,c))
            res=find(r,c+1,i+1)or find(r,c-1,i+1)or find(r+1,c,i+1)or find(r-1,c,i+1)
            path.remove((r,c))
            return res


        
        for r in range(row):
            for c in range(col):
                if find(r,c,0): return True
        
        return False





            

        
        


        