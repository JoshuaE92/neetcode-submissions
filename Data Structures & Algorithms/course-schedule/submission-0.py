class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        premap={i:[] for i in range(numCourses)}

        for co,pre in prerequisites:
            premap[co].append(pre)


        visited=set()
        def dfs(co):
            if co in visited:
                return False
            
            if premap[co]==[]:
                return True
            
            visited.add(co)

            for pre in premap[co]:
                if not dfs(pre):
                    return False
                
            premap[co]=[]
            visited.remove(co)
            return True
        
        for co,pre in prerequisites:
            if not(dfs(co)):
                return False
        
        return True



            



        

    


        