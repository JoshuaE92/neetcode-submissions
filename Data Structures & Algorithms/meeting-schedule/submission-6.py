"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sortbystart=sorted(intervals, key=lambda inter:inter.start)

        if(sortbystart):
            startCheck=sortbystart[0].start
            endCheck=sortbystart[0].end

            for i in range(1,len(sortbystart)):
                if (sortbystart[i].start>= startCheck and sortbystart[i].start<endCheck) or (sortbystart[i].end>=startCheck and sortbystart[i].end<=endCheck):
                
                    
                    return False
                startCheck=sortbystart[i].start
                endCheck=sortbystart[i].end

        
        return True


