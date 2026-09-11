import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        #use bisect to find out where the value would lie
        
        #merging all togetehr
        #if the start of my interval is less then then end of the left neighbor, and the cur interval end is greater then the start of the right most neighbor, we merge

        #merging left

        #if my start is less then the end of the left val thne we just merge

        #merging right

        #if my end is greater then the right guy start, merge vals based on who is larger

        #not merging at all, just place in the position


        res=[]

        for i in range(len(intervals)):
            #check for the it belongs b4
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
               
                return res+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:

                newInterval[0]=min(newInterval[0],intervals[i][0])
                newInterval[1]=max(newInterval[1],intervals[i][1])
            
        res.append(newInterval)
        return res
                





        