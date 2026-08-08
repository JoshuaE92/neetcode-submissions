class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #turn the array into a set
        #iterate through the set
            #check if its is the start of someting:
                #target=curent value+1
                #lenght=1

                #while(target+length in the set):
                #lenght+=1

                #retval=max(lenght,retval)
            #return maxval

        retval=0
        my_set=set(nums)
        for val in my_set:
            if not (val-1 in my_set):
                target=val
                length=1

                while((target+length) in my_set):
                    length+=1
                retval=max(length,retval)
        return retval
        


        
            

        