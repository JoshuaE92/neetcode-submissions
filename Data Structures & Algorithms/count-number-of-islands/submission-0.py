class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        from collections import deque
        #base case
        if not grid:
            return 0

        visited=set()

        
        row=len(grid)
        col=len(grid[0])

        islands=0

        def bfs(r,c,visited):
            queue=deque()
            queue.append((r,c))
            
            visited.add((r,c))



            #pop from the queue
            #for all the child of the pop node
            #check if not in visited
            #add to que

            while queue:
                pr,pc=queue.popleft()

                directions=[(-1,0),(1,0),(0,-1),(0,1)]

                for r,c in directions:
                    mover,movec=pr+r,pc+c

                    
                    if mover in range(row) and movec in range(col) and (mover,movec) not in visited and grid[mover][movec]=="1":
                        visited.add((mover,movec))
                        queue.append((mover,movec))
                    


        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c,visited)
                    islands+=1
        return islands





        







        #bfs

        #loop through everything
        